from typing import List, Dict
from contas.conta import Conta
from clientes.cliente import Cliente

class Agencia:
    """Classe representando uma agência bancária"""
    
    def __init__(self, codigo: str, nome: str, banco: 'Banco'):
        self._codigo = codigo
        self._nome = nome
        self._banco = banco
        self._contas: Dict[int, Conta] = {}
        self._clientes: Dict[str, Cliente] = {}
    
    @property
    def codigo(self) -> str:
        return self._codigo
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def banco(self) -> 'Banco':
        return self._banco
    
    def adicionar_conta(self, conta: 'Conta') -> None:
        if conta.numero in self._contas:
            raise ValueError(f"Conta {conta.numero} já existe")
        self._contas[conta.numero] = conta
        self._adicionar_cliente(conta.titular)
    
    def _adicionar_cliente(self, cliente: 'Cliente') -> None:
        if cliente.documento not in self._clientes:
            self._clientes[cliente.documento] = cliente
    
    def buscar_conta(self, numero: int) -> 'Conta':
        return self._contas.get(numero)
    
    def listar_contas(self) -> List['Conta']:
        return list(self._contas.values())
    
    def __str__(self) -> str:
        return f"Agência {self._nome} ({self._codigo}) - {len(self._contas)} contas"