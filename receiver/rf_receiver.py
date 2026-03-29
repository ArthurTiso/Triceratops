from rpi_rf import RFDevice
from receiver.base_receiver import BaseReceiver


class RFReceiver(BaseReceiver):
    def __init__(self, gpio=17):
        self.rfdevice = RFDevice(gpio)
        self.rfdevice.enable_rx()

    def receber(self):
        if self.rfdevice.rx_code_timestamp is not None:
            codigo = self.rfdevice.rx_code
            self.rfdevice.rx_code_timestamp = None

            # 🔥 TEMPORÁRIO: simula protocolo
            pacote = f"***1000{codigo:04d}{codigo:04d}0000000100###"

            return pacote

        return None

    def cleanup(self):
        self.rfdevice.cleanup()