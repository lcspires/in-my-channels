from abc import ABC, abstractmethod
from datetime import date

class Cliente(ABC):
    """Classe abstrata representando um cliente"""
    
    def __init__(self, nome: str, documento: str, data_nascimento: date):
        self._nome = nome
        self._documento = documento
        self._data_nascimento = data_nascimento
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    @abstractmethod
    def documento(self) -> str:
        pass
    
    @property
    def data_nascimento(self) -> date:
        return self._data_nascimento
    
    @abstractmethod
    def validar_documento(self) -> bool:
        pass
    
    def __str__(self) -> str:
        return f"{self._nome} ({self.documento})"