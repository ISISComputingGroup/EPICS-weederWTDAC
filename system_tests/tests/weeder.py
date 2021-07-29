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

    def test_WHEN_set_voltage_THEN_get_voltage_back_correctly(self):
        self.ca.assert_setting_setpoint_sets_readback(100, "VOLT")

    def test_WHEN_set_trapezoid_ramping_voltage_THEN_get_ramping_voltage_correctly(self):
        self.ca.assert_setting_setpoint_sets_readback(100, "RAMPVOLT_T")

    def test_WHEN_set_scurve_ramping_voltage_THEN_get_ramping_voltage_correctly(self):
        self.ca.assert_setting_setpoint_sets_readback(100, "RAMPVOLT_S")

    def test_WHEN_set_padding_THEN_get_padding_correctly(self):
        self.ca.assert_setting_setpoint_sets_readback(100, "PADDING")

    def test_WHEN_set_ramp_rate_THEN_get_ramp_rate_correctly(self):
        self.ca.assert_setting_setpoint_sets_readback(100, "RAMPRATE")

    # def test_WHEN_set_wait_THEN_get_wait_correctly(self):
    #     self.ca.assert_setting_setpoint_sets_readback(100, "WAIT")

    def test_WHEN_set_default_voltage_THEN_get_default_voltage_correctly(self):
        self.ca.assert_setting_setpoint_sets_readback(100, "DEFAULT")

    # def test_WHEN_set_calibrate_THEN_get_calibrate_correctly(self):
    #     self.ca.assert_setting_setpoint_sets_readback(100, -100, "CALIBRATE")
