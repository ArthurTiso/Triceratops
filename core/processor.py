from datetime import datetime, timedelta


class Processor:
    def __init__(self, state):
        self.state = state
        self.ultimo_peso = 0
        self.tempo_ultimo_dado = None

    def processar(self, dados: dict):
        agora = datetime.now()

        # Atualiza estado base
        self.state.atualizar(dados)

        # Detecta início
        if self.state.status == "IDLE" and dados["flag"] == 0:
            self.state.set_status("RUNNING")

        # Detecta quebra
        if dados["peso_atual"] < dados["peso_max"]:
            self.state.set_status("BROKEN")

        # Atualiza tempo do último dado
        self.tempo_ultimo_dado = agora

        # Detecta inatividade (ex: 10s sem dado)
        if self.tempo_ultimo_dado:
            if agora - self.tempo_ultimo_dado > timedelta(seconds=10):
                self.state.set_status("INACTIVE")

        self.ultimo_peso = dados["peso_atual"]