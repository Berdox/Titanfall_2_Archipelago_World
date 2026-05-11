from worlds.generic.Rules import forbid_items_for_player, add_rule
from .Items import TitanfallItem
from .Locations import get_locations

def create_rules(self):
    multiworld = self.multiworld
    player = self.player
    options = self.options
    
    # Locations in 'Effect and Cause' that require the time-swap mechanic
    time_travel_locations = [
        "Effect and Cause (2): Helmet 1",
        "Effect and Cause (2): Helmet 2",
        "Effect and Cause (2): Helmet 3",
        "Effect and Cause (2): Helmet 4",
        "Effect and Cause (2): Helmet 5",
        "Effect and Cause (2): Helmet 6",
    ]
    for loc_name in time_travel_locations:
        add_rule(multiworld.get_location(loc_name, player), 
                 lambda state: state.has("Time Shift", player))

    # 2. Locations in 'The Beacon' that require the ARC Tool
    beacon_locations = [
        "The Beacon (2): Helmet 1"
    ]
    for loc_name in time_travel_locations:
        add_rule(multiworld.get_location(loc_name, player),
                lambda state: state.has("ARC Tool", player))

    # 3. Boss Requirements
    '''
    bosses_requiring_titan = ["Boss: Ash", "Boss: Richter", "Boss: Viper"]
    for boss in bosses_requiring_titan:
        add_rule(multiworld.get_location(boss, player), 
                 lambda state: has_any_titan_loadout(state, player))
    '''

    # 4. Final Mission Requirements
    '''
    fold_weapon_checks = [
        "The Fold Weapon: Helmet 1",
        "The Fold Weapon: Helmet 2",
        "The Fold Weapon: Helmet 3",
        "Boss: Slone"
    ]
    for loc_name in fold_weapon_checks:
        add_rule(multiworld.get_location(loc_name, player), 
                 lambda state: state.has("SERE Kit", player))
    '''
    # 5. Victory Condition Rule
    add_rule(multiworld.get_location("Victory", player),
             lambda state: state.can_reach_location("Boss: Slone", player))


# --- Helper Functions ---

def has_any_titan_loadout(state, player: int) -> bool:
    """Checks if the player has at least one Titan loadout unlocked."""
    titan_loadouts = [
        "Expedition", "Tone", "Scorch", "Ion", 
        "Ronin", "Northstar", "Legion", "Brute"
    ]
    return any(state.has(loadout, player) for loadout in titan_loadouts)

# Could do a 100% option where you have to collect everything thing
def get_required_loadout_count(self) -> int:
    if self.options.difficulty == 0: # Easy
        return 1
    elif self.options.difficulty == 2: # Hard
        return 4
    return 2