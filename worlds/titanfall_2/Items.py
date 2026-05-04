from typing import Dict, NamedTuple
from BaseClasses import ItemClassification

class ItemData(NamedTuple):
    category: str
    code: int
    count: int = 1
    classification: ItemClassification = ItemClassification.filler

item_table: Dict[str, ItemData] = {    
    # Tacticals
    'Cloak':       ItemData('Tactical',     72740000, 1, ItemClassification.filler),
    'Pulse Blade': ItemData('Tactical',     72740001, 1, ItemClassification.filler),
    'Grapple':     ItemData('Tactical',     72740002, 1, ItemClassification.filler),
    'Stim':        ItemData('Tactical',     72740003, 1, ItemClassification.filler),
    'A-Wall':      ItemData('Tactical',     72740004, 1, ItemClassification.filler),
    'Phase Shift': ItemData('Tactical',     72740005, 1, ItemClassification.filler),
    'Holo Pilot':  ItemData('Tactical',     72740006, 1, ItemClassification.filler),
    'Time Shift':  ItemData('Tactical',     72740007, 1, ItemClassification.progression),
    
    # Titan loadouts
    'Expedition': ItemData('Titan_Loadout', 72740008, 1, ItemClassification.filler),
    'Tone':       ItemData('Titan_Loadout', 72740009, 1, ItemClassification.filler),
    'Scorch':     ItemData('Titan_Loadout', 72740010, 1, ItemClassification.filler),
    'Brute':      ItemData('Titan_Loadout', 72740011, 1, ItemClassification.filler),
    'Ion':        ItemData('Titan_Loadout', 72740012, 1, ItemClassification.filler),
    'Ronin':      ItemData('Titan_Loadout', 72740013, 1, ItemClassification.filler),
    'Northstar':  ItemData('Titan_Loadout', 72740014, 1, ItemClassification.filler),
    'Legion':     ItemData('Titan_Loadout', 72740015, 1, ItemClassification.filler),
    
    # Tools
    'ARC Tool':     ItemData('Tool', 72740016, 1, ItemClassification.progression),
}