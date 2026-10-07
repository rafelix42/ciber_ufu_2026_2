"""Modelo que representa um equipamento/ativo de TI cadastrado no inventário."""
from typing import Optional

class Equipamento:
    def __init__(
            self,
            nome: str,
            responsavel: str,
            setor: str,
            descricao: str = "",
            id: Optional[int] = None
        ):
        self.nome = nome
        self.responsavel = responsavel
        self.setor = setor
        self.descricao = descricao
        self.id = id

    def exibir_detalhes(self):
        detalhes = "Equipamento: "
        detalhes += f"{self.nome}\nID: {self.id}\nResponsável: {self.responsavel}\n"
        detalhes += f"Setor: {self.setor}\nDescrição: {self.descricao}"
        return detalhes


class Notebook(Equipamento):
    def exibir_detalhes(self):
        detalhes = "Notebook: "
        detalhes += f"{self.nome}\nID: {self.id}\nResponsável: {self.responsavel}\n"
        detalhes += f"Setor: {self.setor}\nDescrição: {self.descricao}"
        return detalhes


class Servidor(Equipamento):
    def exibir_detalhes(self):
        detalhes = "Servidor: "
        detalhes += f"{self.nome}\nID: {self.id}\nResponsável: {self.responsavel}\n"
        detalhes += f"Setor: {self.setor}\nDescrição: {self.descricao}"
        return detalhes


class Roteador(Equipamento):
    def exibir_detalhes(self) -> str:
        detalhes = "Roteador: "
        detalhes += f"{self.nome}\nID: {self.id}\nResponsável: {self.responsavel}\n"
        detalhes += f"Setor: {self.setor}\nDescrição: {self.descricao}"
        return detalhes