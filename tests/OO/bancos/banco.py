from typing import List, Dict
from bancos.agencia import Agencia

class Banco:
    """Classe representando um banco"""
    
    total_bancos = 0  # Variável de classe
    
    def __init__(self, nome: str, codigo: str):
        self._nome = nome
        self._codigo = codigo
        self._agencias: Dict[str, Agencia] = {}
        Banco.total_bancos += 1
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def codigo(self) -> str:
        return self._codigo
    
    @property
    def agencias(self) -> List['Agencia']:
        return list(self._agencias.values())
    
    def adicionar_agencia(self, agencia: 'Agencia') -> None:
        if agencia.codigo in self._agencias:
            raise ValueError(f"Agência {agencia.codigo} já existe")
        self._agencias[agencia.codigo] = agencia
    
    def buscar_agencia(self, codigo: str) -> 'Agencia':
        return self._agencias.get(codigo)
    
    def __str__(self) -> str:
        return f"Banco {self._nome} ({self._codigo}) - {len(self._agencias)} agências"
    
    def __repr__(self) -> str:
        return f"Banco(nome='{self._nome}', codigo='{self._codigo}')"
    
    @classmethod
    def get_total_bancos(cls) -> int:
        return cls.total_bancos