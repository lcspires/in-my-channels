from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, TYPE_CHECKING

# Usando TYPE_CHECKING para evitar circular imports
if TYPE_CHECKING:
    from clientes.cliente import Cliente
    from bancos.agencia import Agencia
    from operacoes.operacao import Operacao

class Conta(ABC):
    """Classe abstrata representando uma conta bancária"""
    
    _numero_sequence = 1000  # Contador de sequência para números de conta
    
    def __init__(self, titular: 'Cliente', agencia: 'Agencia', saldo: float = 0.0):
        self._numero = self._gerar_numero()
        self._titular = titular
        self._agencia = agencia
        self._saldo = saldo
        self._operacoes: List['Operacao'] = []
    
    @classmethod
    def _gerar_numero(cls) -> int:
        # Corrigido: incrementa ANTES de retornar
        numero_atual = cls._numero_sequence
        cls._numero_sequence += 1
        return numero_atual
    
    @property
    def numero(self) -> int:
        return self._numero
    
    @property
    def titular(self) -> 'Cliente':
        return self._titular
    
    @property
    def agencia(self) -> 'Agencia':
        return self._agencia
    
    @property
    def saldo(self) -> float:
        return self._saldo
    
    @abstractmethod
    def sacar(self, valor: float) -> bool:
        pass
    
    @abstractmethod
    def depositar(self, valor: float) -> bool:
        pass
    
    def adicionar_operacao(self, operacao: 'Operacao') -> None:
        self._operacoes.append(operacao)
    
    def extrato(self) -> str:
        extrato = f"Extrato da Conta {self._numero}\n"
        extrato += f"Titular: {self._titular.nome}\n"
        extrato += f"Saldo: R$ {self._saldo:.2f}\n\n"
        extrato += "Operações:\n"
        
        for op in sorted(self._operacoes, key=lambda x: x.data, reverse=True)[:10]:
            extrato += f"{op.data.strftime('%d/%m/%Y %H:%M')} - {op}\n"
        
        return extrato
    
    def __str__(self) -> str:
        return f"Conta {self._numero} - {self._titular.nome}"