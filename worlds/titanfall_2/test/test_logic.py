from .bases import Titanfall2TestBase

class TestTitanfallLogic(Titanfall2TestBase):
    options = {
        "randomize_tacticals": True,
        "difficulty": "regular"
    }

    def test_time_shift_access(self) -> None:
        """Test that Effect and Cause (2) helmets strictly require Time Shift"""
        locations = [
            "Effect and Cause (2): Helmet 1",
            "Effect and Cause (2): Helmet 2",
            "Effect and Cause (2): Helmet 3"
        ]
        items = [["Time Shift"]]
        self.assertAccessDependency(locations, items)

    def test_arc_tool_access(self) -> None:
        """Test locations that require the ARC Tool"""
        # Replace these with the actual location names you defined in Locations.py
        locations = ["The Beacon (2): Helmet 1", "The Beacon (2): Helmet 2"]
        items = [["ARC Tool"]]
        self.assertAccessDependency(locations, items)

    def test_victory_condition(self) -> None:
        """Test that the game can be won once 'Victory' is achieved"""
        self.assertFalse(self.can_reach_location("Victory"))
        self.collect_by_name("Victory")
        # Check if the completion condition is met
        self.assertTrue(self.multiworld.completion_condition[self.player](self.multiworld.state))