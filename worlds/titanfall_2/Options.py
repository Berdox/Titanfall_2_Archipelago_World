from dataclasses import dataclass
from Options import Choice, Range, Toggle, DeathLink, DefaultOnToggle, PerGameCommonOptions

class Goal(Choice):
    """
    Determines the victory condition for the game.
    Fold Weapon: Complete the final mission and defeat Slone.
    Boss Rush: Defeat all 5 Apex Predators (Kane, Ash, Richter, Viper, Slone).
    """
    display_name = "Goal"
    option_fold_weapon = 0
    option_boss_rush = 1
    default = 0

class TitanLoadoutLogic(Choice):
    """
    Determines how Titan Loadouts affect logic.
    Normal: You may need specific loadouts to progress past certain bosses.
    Minimal: Any single Titan Loadout is enough to clear all Titan-based logic.
    None: Titan Loadouts are never required for logic (effectively making them filler).
    """
    display_name = "Titan Loadout Logic"
    option_normal = 0
    option_minimal = 1
    option_none = 2
    default = 0

class Difficulty(Choice):
    """
    Sets the expected difficulty level for logic. 
    Higher difficulties may assume more advanced movement or combat skills.
    """
    display_name = "Difficulty"
    option_easy = 0
    option_regular = 1
    option_master = 2
    default = 1

class ExtraBatteries(Range):
    """
    The number of Extra Battery filler items to add to the pool.
    Useful for filling up the item pool if you have many locations.
    """
    display_name = "Extra Batteries"
    range_start = 0
    range_end = 50
    default = 20

class RandomizeTacticals(DefaultOnToggle):
    """
    If enabled, Pilot Tacticals (Cloak, Stim, Grapple, etc.) will be 
    shuffled into the multiworld.
    """
    display_name = "Randomize Tacticals"

@dataclass
class TitanfallOptions(PerGameCommonOptions):
    goal: Goal
    titan_loadout_logic: TitanLoadoutLogic
    difficulty: Difficulty
    extra_batteries: ExtraBatteries
    randomize_tacticals: RandomizeTacticals
    death_link: DeathLink