from lewis.adapters.stream import StreamInterface, Cmd
from lewis.utils.command_builder import CmdBuilder
from lewis.core.logging import has_log
from lewis.utils.replies import conditional_reply

@has_log
class WeederStreamInterface(StreamInterface):

    commands = {
        CmdBuilder("set_voltage").escape("V ").char().escape(" ").int().eos().build(),
        CmdBuilder("get_voltage").escape("V ").char().eos().build(),
        CmdBuilder("get_trapezoid").escape("T ").char().eos().build(),
        CmdBuilder("set_trapezoid").escape("T ").char().escape(" ").int().eos().build(),
        CmdBuilder("get_scurve").escape("S ").char().eos().build(),
        CmdBuilder("set_scurve").escape("S ").char().escape(" ").int().eos().build(),
        CmdBuilder("set_padding").escape("P ").char().escape(" ").int().eos().build(), #default val = 2
        CmdBuilder("get_padding").escape("P ").char().eos().build(),
        CmdBuilder("set_ramprate").escape("R ").char().escape(" ").int().eos().build(), #default val=50
        CmdBuilder("get_ramprate").escape("R ").char().eos().build(),
        CmdBuilder("set_wait").escape("W ").int().eos().build(),
        CmdBuilder("set_default").escape("D ").char().escape(" ").int().eos().build(),
        CmdBuilder("get_default").escape("D ").char().eos().build(),
        #CmdBuilder("set_calibrate").escape("C ").char().escape(" ").char().escape(" ").int().eos().build(), #ask
        CmdBuilder("set_echo").escape("X ").char().escape(" ").int().eos().build(),

#arg("[0-9]{4}")
    }

    def set_voltage(self, address, voltage_sp):
        self._device.voltage = voltage_sp
        print(f"Got voltage {voltage_sp} from {address}")

    def get_voltage(self, address):
        return f"V {address} {self._device.voltage}"

    def set_trapezoid(self, address, trapezoid_sp):
        self._device.trapezoid = trapezoid_sp
        print(f"Get trapezoid {trapezoid_sp} from {address}")

    def get_trapezoid(self,address):
        return f"T {address} {self._device.trapezoid}"

    def set_scurve(self, address, scurve_sp):
        self._device.scurve = scurve_sp
        print(f"Get S curve {scurve_sp} from {address}")

    def get_scurve(self, address):
        return f"S {address} {self._device.scurve}"

    def set_padding(self, address, padding_sp):
        self._device.padding = padding_sp
        print(f"Get padding {padding_sp} from {address}")

    def get_padding(self,address):
        return f"P {address} {self._device.padding}"

    def set_ramprate(self, address, ramprate_sp):
        self._device.ramprate = ramprate_sp
        print (f"Get ramp rate {ramprate_sp} from {address}")

    def get_ramprate(self,address):
        return f"R {address} {self._device.padding}"

    def set_wait(self, wait_sp):
        self._device.wait = wait_sp
        print (f"Get wait time {wait_sp} ")

    def get_wait(self, wait_sp):
        return f"W {self._device.wait}"

    def set_default(self, address, default_sp):
        self._device.default = default_sp
        print(f"Get default voltage {default_sp} from {address}")

    def get_default(self, address):
        return f"D {address} {self._device.default}"

    # def set_calibrate(self, address, calibrate_sp):
    #     self._device.calibrate = calibrate_sp
    #     print(f"Get calibration coefficients {calibrate_sp} from {address}")
    #
    # def get_calibrate(self, address):
    #     return f"V{self._device.calibrate}"

    def set_echo(self, address, echo_sp):
        print(f"Get reception confirmation {echo_sp} from {address}")

  #  def set_error(self, address, error_sp):
   #     print(f"Get calibration coefficients {calibrate_sp} from {address}")
#
#    def set_calibrate(self, address, calibrate_sp):
   #     print(f"Get calibration coefficients {calibrate_sp} from {address}")


    in_terminator = "\r\n"
    out_terminator = "\r\r\n"


    def handle_error(self, request, error):
        print("An error occurred at request " + repr(request) + ": " + repr(error))

