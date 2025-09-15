from .cliente import Cliente
from datetime import date
import re

class PessoaJuridica(Cliente):
    """Classe representando uma pessoa jurídica"""
    
    def __init__(self, nome: str, cnpj: str, data_abertura: date):
        super().__init__(nome, cnpj, data_abertura)
    
    @property
    def documento(self) -> str:
        return self._formatar_cnpj(self._documento)
    
    def validar_documento(self) -> bool:
        return self._validar_cnpj(self._documento)
    
    @staticmethod
    def _validar_cnpj(cnpj: str) -> bool:
        # Implementação simplificada de validação de CNPJ
        cnpj = re.sub(r'[^0-9]', '', cnpj)
        return len(cnpj) == 14
    
    @staticmethod
    def _formatar_cnpj(cnpj: str) -> str:
        cnpj = re.sub(r'[^0-9]', '', cnpj)
        return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"