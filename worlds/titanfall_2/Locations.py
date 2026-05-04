'''
Helments list (46):

Gauntlet 1 

BT-7274 1
BT-7274 2

Blood and Rust 1
Blood and Rust 2
Blood and Rust 3
Blood and Rust 4
Blood and Rust 5
Blood and Rust 6

Into the Abyss (1) 1
Into the Abyss (1) 2
Into the Abyss (1) 3
Into the Abyss (1) 4

Into the Abyss (2) 1
Into the Abyss (2) 2
Into the Abyss (2) 3

Into the Abyss (3) 1
Into the Abyss (3) 2

Effect and Cause (1) 1
Effect and Cause (1) 2

Effect and Cause (2) 1
Effect and Cause (2) 2
Effect and Cause (2) 3
Effect and Cause (2) 4
Effect and Cause (2) 5
Effect and Cause (2) 6

The Beacon (1) 1
The Beacon (1) 2

The Beacon (2) 1
The Beacon (2) 2
The Beacon (2) 3
The Beacon (2) 4
The Beacon (2) 5
The Beacon (2) 6
The Beacon (2) 7
The Beacon (2) 8
The Beacon (2) 9

Trail by Fire 1
Trail by Fire 2
Trail by Fire 3

The Ark 1
The Ark 2
The Ark 3

The Fold Weapon 1
The Fold Weapon 2
The Fold Weapon 3
'''


'''
List of Missions:

The Pilot's Gauntlet

BT-7274

Blood and Rust

Into the Abyss

Effect and Cause

The Beacon

Trail by Fire

The Ark

The Fold Weapon
'''


'''
Bosses:

Kane

Ash

Richter

Viper

Slone

'''

from typing import List, Optional, Callable, NamedTuple
from BaseClasses import CollectionState

# Using None for Event IDs (like the final goal)
EventId: Optional[int] = None

class LocationData(NamedTuple):
    region: str
    name: str
    code: Optional[int]
    rule: Optional[Callable[[CollectionState], bool]] = None

def get_locations(player: int) -> List[LocationData]:
    
    location_table: List[LocationData] = [
        # --- The Pilot's Gauntlet ---
        LocationData('The Pilot\'s Gauntlet', 'Gauntlet: Helmet 1', 72741000),
        LocationData('The Pilot\'s Gauntlet', 'Mission Complete: The Pilot\'s Gauntlet', 72741001),

        # --- BT-7274 ---
        LocationData('BT-7274', 'BT-7274: Helmet 1', 72741002),
        LocationData('BT-7274', 'BT-7274: Helmet 2', 72741003),
        LocationData('BT-7274', 'Mission Complete: BT-7274', 72741004),

        # --- Blood and Rust ---
        LocationData('Blood and Rust', 'Blood and Rust: Helmet 1', 72741005),
        LocationData('Blood and Rust', 'Blood and Rust: Helmet 2', 72741006),
        LocationData('Blood and Rust', 'Blood and Rust: Helmet 3', 72741007),
        LocationData('Blood and Rust', 'Blood and Rust: Helmet 4', 72741008),
        LocationData('Blood and Rust', 'Blood and Rust: Helmet 5', 72741009),
        LocationData('Blood and Rust', 'Blood and Rust: Helmet 6', 72741010),
        LocationData('Blood and Rust', 'Boss: Kane', 72741011),
        LocationData('Blood and Rust', 'Mission Complete: Blood and Rust', 72741012),

        # --- Into the Abyss ---
        LocationData('Into the Abyss', 'Into the Abyss (1): Helmet 1', 72741013),
        LocationData('Into the Abyss', 'Into the Abyss (1): Helmet 2', 72741014),
        LocationData('Into the Abyss', 'Into the Abyss (1): Helmet 3', 72741015),
        LocationData('Into the Abyss', 'Into the Abyss (1): Helmet 4', 72741016),
        LocationData('Into the Abyss', 'Into the Abyss (2): Helmet 1', 72741017),
        LocationData('Into the Abyss', 'Into the Abyss (2): Helmet 2', 72741018),
        LocationData('Into the Abyss', 'Into the Abyss (2): Helmet 3', 72741019),
        LocationData('Into the Abyss', 'Into the Abyss (3): Helmet 1', 72741020),
        LocationData('Into the Abyss', 'Into the Abyss (3): Helmet 2', 72741021),
        LocationData('Into the Abyss', 'Boss: Ash', 72741022),
        LocationData('Into the Abyss', 'Mission Complete: Into the Abyss', 72741023),

        # --- Effect and Cause ---
        LocationData('Effect and Cause', 'Effect and Cause (1): Helmet 1', 72741024),
        LocationData('Effect and Cause', 'Effect and Cause (1): Helmet 2', 72741025),
        
        # Helmets in part 2 often require the Wrist Device
        LocationData('Effect and Cause', 'Effect and Cause (2): Helmet 1', 72741026, lambda state: state.has("Time Shift", player)),
        LocationData('Effect and Cause', 'Effect and Cause (2): Helmet 2', 72741027, lambda state: state.has("Time Shift", player)),
        LocationData('Effect and Cause', 'Effect and Cause (2): Helmet 3', 72741028, lambda state: state.has("Time Shift", player)),
        LocationData('Effect and Cause', 'Effect and Cause (2): Helmet 4', 72741029, lambda state: state.has("Time Shift", player)),
        LocationData('Effect and Cause', 'Effect and Cause (2): Helmet 5', 72741030, lambda state: state.has("Time Shift", player)),
        LocationData('Effect and Cause', 'Effect and Cause (2): Helmet 6', 72741031, lambda state: state.has("Time Shift", player)),
        LocationData('Effect and Cause', 'Mission Complete: Effect and Cause', 72741032),

        # --- The Beacon ---
        LocationData('The Beacon', 'The Beacon (1): Helmet 1', 72741033),
        LocationData('The Beacon', 'The Beacon (1): Helmet 2', 72741034),
        LocationData('The Beacon', 'The Beacon (2): Helmet 1', 72741035),
        LocationData('The Beacon', 'The Beacon (2): Helmet 2', 72741036),
        LocationData('The Beacon', 'The Beacon (2): Helmet 3', 72741037),
        LocationData('The Beacon', 'The Beacon (2): Helmet 4', 72741038),
        LocationData('The Beacon', 'The Beacon (2): Helmet 5', 72741039),
        LocationData('The Beacon', 'The Beacon (2): Helmet 6', 72741040),
        LocationData('The Beacon', 'The Beacon (2): Helmet 7', 72741041),
        LocationData('The Beacon', 'The Beacon (2): Helmet 8', 72741042),
        LocationData('The Beacon', 'The Beacon (2): Helmet 9', 72741043),
        LocationData('The Beacon', 'Boss: Richter', 72741044),
        LocationData('The Beacon', 'Mission Complete: The Beacon', 72741045),

        # --- Trial by Fire ---
        LocationData('Trial by Fire', 'Trial by Fire: Helmet 1', 72741046),
        LocationData('Trial by Fire', 'Trial by Fire: Helmet 2', 72741047),
        LocationData('Trial by Fire', 'Trial by Fire: Helmet 3', 72741048),
        LocationData('Trial by Fire', 'Mission Complete: Trial by Fire', 72741049),

        # --- The Ark ---
        LocationData('The Ark', 'The Ark: Helmet 1', 72741050),
        LocationData('The Ark', 'The Ark: Helmet 2', 72741051),
        LocationData('The Ark', 'The Ark: Helmet 3', 72741052),
        LocationData('The Ark', 'Boss: Viper', 72741053),
        LocationData('The Ark', 'Mission Complete: The Ark', 72741054),

        # --- The Fold Weapon ---
        LocationData('The Fold Weapon', 'The Fold Weapon: Helmet 1', 72741055),
        LocationData('The Fold Weapon', 'The Fold Weapon: Helmet 2', 72741056),
        LocationData('The Fold Weapon', 'The Fold Weapon: Helmet 3', 72741057),
        LocationData('The Fold Weapon', 'Boss: Slone', 72741058),
        LocationData('The Fold Weapon', 'Victory', EventId), # Goal
    ]
    
    return location_table