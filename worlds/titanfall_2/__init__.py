from typing import ClassVar, Dict, Any, Type
from BaseClasses import ItemClassification, Region, Location, Item, Tutorial
from Options import PerGameCommonOptions
from worlds.AutoWorld import World, WebWorld

from .Items import item_table, group_table, TitanfallItem  # Assuming Items.py uses similar dict/list structure
from .Locations import get_locations, TitanfallLocation
from .Rules import create_rules
from .Options import TitanfallOptions, titanfall_option_groups

class Titanfall2Web(WebWorld):
    theme = "slate"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Titanfall 2 randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Berdox"]
    )]
    option_groups = titanfall_option_groups

class Titanfall2World(World):
    """
    Titanfall 2 is a fast-paced first-person shooter featuring high-mobility pilot 
    combat and heavy-hitting Titan warfare. Complete missions and defeat the 
    Apex Predators to stop the Fold Weapon.
    """

    game = "Titanfall 2"
    web = Titanfall2Web()

    # Mapping based on your provided dictionary-style ItemData
    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_table = get_locations(0) # Get the list of LocationData
    location_name_to_id = {loc.name: loc.code for loc in location_table if loc.code is not None}
    
    item_name_groups = group_table
    
    options_dataclass: ClassVar[Type[PerGameCommonOptions]] = TitanfallOptions
    options: TitanfallOptions

    required_client_version = (0, 4, 4)

    def get_filler_item_name(self) -> str:
        # Returns the name of the filler item, similar to how Hike uses coins
        return "Extra Battery"

    def create_item(self, name: str) -> "TitanfallItem":
        item_data = item_table[name]
        classification = item_data.classification

        # Example of dynamic classification like Hike's Running Shoes
        if self.options.difficulty == 2 and name in self.item_name_groups["Tacticals"]:
            classification = ItemClassification.progression

        return TitanfallItem(name, classification, item_data.code, player=self.player)

    def create_items(self) -> None:
        itempool = []
        
        # 1. Create items from the main table
        for name, data in item_table.items():
            # Skip tacticals if randomize_tacticals is off (except Time Shift)
            if data.category == 'Tactical' and not self.options.randomize_tacticals:
                if name != "Time Shift":
                    continue
            
            for _ in range(data.count):
                itempool.append(self.create_item(name))

        # 2. Add extra items based on range options (similar to feathers/buckets in Hike)
        # itempool += [self.create_item("Extra Battery") for _ in range(self.options.extra_batteries)]

        # 3. Fill the rest with junk
        junk = len(self.location_name_to_id) - len(itempool)
        if junk > 0:
            itempool += [self.create_item(self.get_filler_item_name()) for _ in range(junk)]

        self.multiworld.itempool += itempool

    def create_regions(self) -> None:
        # Follows Hike's simplified region structure
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        
        main_region = Region("Typhon", self.player, self.multiworld)

        for loc in self.location_name_to_id.keys():
            main_region.locations.append(TitanfallLocation(self.player, loc, self.location_name_to_id[loc], main_region))

        self.multiworld.regions.append(main_region)
        menu_region.connect(main_region)

        # Goal logic modeled after Short Hike's goal block
        if self.options.goal == "fold_weapon":
            # Victory requires reaching the end of the campaign logic
            self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
        elif self.options.goal == "boss_rush":
            # Victory requires defeating all Apex Predators
            self.multiworld.completion_condition[self.player] = lambda state: (
                state.can_reach_location("Boss: Kane", self.player) and
                state.can_reach_location("Boss: Ash", self.player) and
                state.can_reach_location("Boss: Richter", self.player) and
                state.can_reach_location("Boss: Viper", self.player) and
                state.can_reach_location("Boss: Slone", self.player)
            )

    def set_rules(self):
        # Passes the world object and the location table to Rules.py
        create_rules(self)

    def fill_slot_data(self) -> Dict[str, Any]:
        options = self.options

        settings = {
            "goal": int(options.goal),
            "difficulty": int(options.difficulty),
            "titan_logic": int(options.titan_loadout_logic.value),
            "death_link": bool(options.death_link),
        }
    
        slot_data = {
            "settings": settings,
        }
    
        return slot_data