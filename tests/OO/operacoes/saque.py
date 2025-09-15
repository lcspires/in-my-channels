from operacoes.operacao import Operacao

class Saque(Operacao):
    """Classe representando uma operação de saque"""
    
    def __init__(self, valor: float, conta: 'Conta', descricao: str = "Saque"):
        # Validação adicional para saque
        if valor <= 0:
            raise ValueError("Valor do saque deve ser positivo")
        
        super().__init__(-valor, conta, descricao)  # Valor negativo para saque
    
    def __str__(self) -> str:
        return f"Saque: -R$ {abs(self.valor):.2f}"