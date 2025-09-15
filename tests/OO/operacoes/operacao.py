from abc import ABC
from datetime import datetime
from typing import TYPE_CHECKING

# Usando TYPE_CHECKING para evitar circular imports
if TYPE_CHECKING:
    from contas.conta import Conta

class Operacao(ABC):
    """Classe abstrata representando uma operação bancária"""
    
    def __init__(self, valor: float, conta: 'Conta', descricao: str = ""):
        self._valor = valor
        self._conta = conta
        self._data = datetime.now()
        self._descricao = descricao or self.__class__.__name__
    
    @property
    def valor(self) -> float:
        return self._valor
    
    @property
    def conta(self) -> 'Conta':
        return self._conta
    
    @property
    def data(self) -> datetime:
        return self._data
    
    @property
    def descricao(self) -> str:
        return self._descricao
    
    def __str__(self) -> str:
        sinal = "+" if self.valor > 0 else "-"
        return f"{self.descricao}: {sinal}R$ {abs(self.valor):.2f}"