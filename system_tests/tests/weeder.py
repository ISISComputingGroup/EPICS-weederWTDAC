import unittest
from time import sleep

from utils.test_modes import TestModes
from utils.channel_access import ChannelAccess
from utils.ioc_launcher import get_default_ioc_dir
from utils.testing import get_running_lewis_and_ioc, assert_log_messages, skip_if_recsim, unstable_test
from parameterized import parameterized

# Device prefix
DEVICE_A_PREFIX = "WEEDER_01"

EMULATOR_DEVICE = "WEEDER"

IOCS = [
    {
        "name": DEVICE_A_PREFIX,
        "directory": get_default_ioc_dir("WEEDER"),
        "emulator": EMULATOR_DEVICE,
        "emulator_id": DEVICE_A_PREFIX,
    },

]

TEST_MODES = [TestModes.RECSIM, TestModes.DEVSIM]


class WEEDERTests(unittest.TestCase):
    """
    General tests for the WEEDER.
    """

    def setUp(self):
        self._lewis, self._ioc = get_running_lewis_and_ioc(DEVICE_A_PREFIX, DEVICE_A_PREFIX)
        self.ca = ChannelAccess(default_timeout=20, default_wait_time=0.0, device_prefix=DEVICE_A_PREFIX)

        self.ca.set_pv_value("RAMPON:SP", "OFF")
        self.ca.assert_that_pv_is("RAMPING", "NO")

    def test_WHEN_set_voltage_THEN_get_voltage_back_correctly(self):
        self.ca.assert_setting_setpoint_sets_readback(100, "VOLT")

    def test_WHEN_set_rampon_THEN_get_rampon_is_on_(self):
        self.ca.assert_setting_setpoint_sets_readback("ON", "RAMPON")

    def test_WHEN_ramping_up_THEN_voltage_is_ramped_correctly(self):
        start_voltage = 0 # V

        target_voltage = 1  # V

        # secs - The test will take at least this long to run but if it's too small may get random timing problems
        # causing the test to fail
        ramp_time = 20

        ramp_rate = target_voltage * 60 / ramp_time  # V per min

        # Ensure setpoint is zero initially
        self.ca.set_pv_value("VOLT:SP", start_voltage)
        self.ca.assert_that_pv_is("OUT_SP", 0.0)

        # Set up ramp and set a setpoint so that the ramp starts.
        self.ca.assert_setting_setpoint_sets_readback(ramp_rate, "RAMP:RATE")
        self.ca.set_pv_value("RAMPON:SP", "ON")
        self.ca.set_pv_value("VOLT:SP", target_voltage, wait=True)

        # Verify that setpoint does not reach final value within first half of ramp time
        self.ca.assert_that_pv_is_not("OUT_SP", target_voltage, timeout=ramp_time/2)

        # ... But after a further ramp_time, it should have.
        # We give it another 3 seconds here in case it hasn't finished ramping.
        self.ca.assert_that_pv_is("OUT_SP", target_voltage, timeout=ramp_time+3)

