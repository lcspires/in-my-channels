from operacoes.operacao import Operacao

class Deposito(Operacao):
    """Classe representando uma operação de depósito"""
    
    def __init__(self, valor: float, conta: 'Conta', descricao: str = "Depósito"):
        # Validação adicional para depósito
        if valor <= 0:
            raise ValueError("Valor do depósito deve ser positivo")
        
        super().__init__(valor, conta, descricao)  # Valor positivo para depósito
    
    def __str__(self) -> str:
        return f"Depósito: +R$ {self.valor:.2f}"