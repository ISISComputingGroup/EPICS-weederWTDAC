from collections import OrderedDict

from lewis.devices import StateMachineDevice

from .states import DefaultState


class SimulatedWeeder(StateMachineDevice):
    def _initialize_data(self):
        self.connected = True
        self.speed = 1
        self.voltage = 0

        # When the device is in an error state it can respond with junk
        self.is_giving_errors = False
        self.out_error = "}{<7f>w"
        self.out_terminator_in_error = ""

    def _get_state_handlers(self):
        return {
            "default": DefaultState(),
        }

    def _get_initial_state(self):
        return "default"

    def _get_transition_handlers(self):
        return OrderedDict([])
