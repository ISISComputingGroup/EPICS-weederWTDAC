
from lewis.adapters.stream import StreamInterface
from lewis.core.logging import has_log
from lewis.utils.command_builder import CmdBuilder


#
# def do_ramp(self):
#     while self._device.voltage < self._device.trapezoid:
#         self._device.voltage += (self._device.ramprate/10)
#         time.sleep(0.1)
#     while self._device.voltage > self._device.trapezoid:
#         self._device.voltage -= (self._device.ramprate/10)
#         time.sleep(0.1)
@has_log
class WeederStreamInterface(StreamInterface):

    commands = {
        CmdBuilder("set_voltage").escape("V ").char().escape(" ").int().eos().build(),
        CmdBuilder("get_voltage").escape("V ").char().eos().build(),

    }
    in_terminator = "\r\n"
    out_terminator = "\r\r\n"

    def set_voltage(self, address, voltage_sp):
        self._device.voltage = voltage_sp
        print(f"Got voltage {voltage_sp} from {address}")

    def get_voltage(self, address):
        return f"V {address} {self._device.voltage}"

    def handle_error(self, request, error):
        print("An error occurred at request " + repr(request) + ": " + repr(error))

