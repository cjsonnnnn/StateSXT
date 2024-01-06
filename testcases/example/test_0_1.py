import pytest

from utils.wrapper import Wrapper
from . import TestExample


@pytest.mark.dev
class TestExample01(TestExample):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)

    @Wrapper.result_receiving
    @Wrapper.unpagshe(*("0.1", "_SN_0_1_Scenario_001_Data"))
    def test_scenario001(self, *args):
        """Test Scenario: 1-1"""

        # change language   (1-1)
        self.soft_assert(self.assertIsNone, self.ep.changeLanguage(lang=args[0]))

        self.assert_all()