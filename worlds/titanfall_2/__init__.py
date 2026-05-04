from typing import ClassVar, Dict, Any, Type, List
from BaseClasses import ItemClassification, Tutorial
from worlds.AutoWorld import World, WebWorld

from .Items import item_table, TitanfallItem
from .Locations import get_locations
from .Regions import create_regions
from .Options import TitanfallOptions
from .Rules import create_rules

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

class Titanfall2World(World):
    """
    Titanfall 2 is a fast-paced first-person shooter featuring high-mobility pilot 
    combat and heavy-hitting Titan warfare. Complete missions and defeat the 
    Apex Predators to stop the Fold Weapon.
    """

    game = "Titanfall 2"
    web = Titanfall2Web()

    # Updated mapping: dictionary key is the name, item_data.code is the ID
    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {loc.name: loc.code for loc in get_locations(0) if loc.code is not None}
    
    options_dataclass: ClassVar[Type[TitanfallOptions]] = TitanfallOptions
    options: TitanfallOptions

    required_client_version = (0, 4, 4)

    def create_item(self, name: str) -> TitanfallItem:
        # Pulling from the dictionary using the name as the key
        item_data = item_table[name]
        return TitanfallItem(name, item_data.classification, item_data.code, self.player)

    def create_items(self) -> None:
        itempool: List[TitanfallItem] = []
        
        # 1. Iterate through the dictionary items
        for name, data in item_table.items():
            # Add the number of copies specified by 'count'
            for _ in range(data.count):
                itempool.append(self.create_item(name))

        # 2. Fill the remaining empty locations with filler
        total_locations = len(self.location_name_to_id)
        junk_needed = total_locations - len(itempool)
        
        if junk_needed > 0:
            for _ in range(junk_needed):
                itempool.append(self.create_item("Extra Battery"))

        self.multiworld.itempool += itempool

    def create_regions(self) -> None:
        create_regions(self.multiworld, self.player)

        # Victory Condition
        self.multiworld.completion_condition[self.player] = lambda state: \
            state.has("Victory", self.player)

    def set_rules(self) -> None:
        create_rules(self)

    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "goal": self.options.goal.value,
            "death_link": bool(self.options.death_link.value),
        }