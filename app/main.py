import time
import json

from receiver.simulated_receiver import SimulatedReceiver
from protocol.decoder import ProtocolDecoder
from core.system_state import SystemState
from core.processor import Processor

from receiver.rf_receiver import RFReceiver

receiver = RFReceiver()

def main():
    USAR_RF = True
    if USAR_RF:
        from receiver.rf_receiver import RFReceiver
        receiver = RFReceiver()
    else:
        from receiver.simulated_receiver import SimulatedReceiver
        receiver = SimulatedReceiver()
    decoder = ProtocolDecoder()
    state = SystemState()
    processor = Processor(state)

    while True:
        pacote = receiver.receber()

        if not pacote:
            continue

        print("PACOTE:", pacote)

        try:
            dados = decoder.decodificar(pacote)

            processor.processar(dados)

            snapshot = state.get_snapshot()

            print("STATE:", snapshot)

            # 🔥 SALVA PARA O DASHBOARD
            with open("state.json", "w") as f:
                json.dump(snapshot, f)

        except Exception as e:
            print("ERRO:", e)

        print("-" * 50)

        time.sleep(1)


if __name__ == "__main__":
    main()