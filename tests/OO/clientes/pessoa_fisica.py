from .cliente import Cliente
from datetime import date
import re

class PessoaFisica(Cliente):
    """Classe representando uma pessoa física"""
    
    def __init__(self, nome: str, cpf: str, data_nascimento: date):
        super().__init__(nome, cpf, data_nascimento)
    
    @property
    def documento(self) -> str:
        return self._formatar_cpf(self._documento)
    
    def validar_documento(self) -> bool:
        return self._validar_cpf(self._documento)
    
    @staticmethod
    def _validar_cpf(cpf: str) -> bool:
        # Implementação simplificada de validação de CPF
        cpf = re.sub(r'[^0-9]', '', cpf)
        return len(cpf) == 11
    
    @staticmethod
    def _formatar_cpf(cpf: str) -> str:
        cpf = re.sub(r'[^0-9]', '', cpf)
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"