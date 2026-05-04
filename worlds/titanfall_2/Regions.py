from typing import List, Dict, Optional, NamedTuple
from BaseClasses import MultiWorld, Region, Entrance
from .Locations import LocationData, get_locations

class TitanfallRegionData(NamedTuple):
    name: str
    connecting_regions: List[str]

def create_regions(multiworld: MultiWorld, player: int):
    # What mission moves onto the next one
    mission_flow = {
        'Menu': ['The Pilot\'s Gauntlet'],
        'The Pilot\'s Gauntlet': ['BT-7274'],
        'BT-7274': ['Blood and Rust'],
        'Blood and Rust': ['Into the Abyss'],
        'Into the Abyss': ['Effect and Cause'],
        'Effect and Cause': ['The Beacon'],
        'The Beacon': ['Trial by Fire'],
        'Trial by Fire': ['The Ark'],
        'The Ark': ['The Fold Weapon'],
        'The Fold Weapon': []
    }

    for region_name in mission_flow.keys():
        new_region = Region(region_name, player, multiworld)
        multiworld.regions.append(new_region)

    locations_by_region = get_locations(player)
    for loc in locations_by_region:
        # Find the region object we just created
        region = multiworld.get_region(loc.region, player)
        region.add_locations({loc.name: loc.code}, TitanfallLocation)

    # 4. Create Entrances (The "Connectors")
    for source, targets in mission_flow.items():
        source_region = multiworld.get_region(source, player)
        for target in targets:
            entrance = Entrance(player, f"{source} -> {target}", source_region)
            source_region.exits.append(entrance)
            entrance.connect(multiworld.get_region(target, player))

# Custom Location class for Titanfall
from worlds.AutoWorld import Location
class TitanfallLocation(Location):
    game: str = "Titanfall 2"