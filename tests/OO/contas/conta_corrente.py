from contas.conta import Conta

class ContaCorrente(Conta):
    """Classe representando uma conta corrente"""
    
    TAXA_MANUTENCAO = 10.00
    LIMITE_SAQUE = 500.00
    
    def __init__(self, titular, agencia, saldo=0.0, limite_cheque_especial=0.0):
        super().__init__(titular, agencia, saldo)
        self._limite_cheque_especial = limite_cheque_especial
    
    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            return False
        
        if valor > self._saldo + self._limite_cheque_especial:
            return False
        
        if valor > self.LIMITE_SAQUE:
            return False
        
        self._saldo -= valor
        
        # Importação local para evitar circular import
        from operacoes.saque import Saque
        saque = Saque(valor, self)
        self.adicionar_operacao(saque)
        return True
    
    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            return False
        
        self._saldo += valor
        
        # Importação local para evitar circular import
        from operacoes.deposito import Deposito
        deposito = Deposito(valor, self)
        self.adicionar_operacao(deposito)
        return True
    
    def aplicar_taxa_manutencao(self):
        if self._saldo >= self.TAXA_MANUTENCAO:
            self._saldo -= self.TAXA_MANUTENCAO
            
            # Importação local para evitar circular import
            from operacoes.saque import Saque
            taxa = Saque(self.TAXA_MANUTENCAO, self, "Taxa de manutenção")
            self.adicionar_operacao(taxa)
    
    def __str__(self):
        return f"Conta Corrente {self.numero} - {self.titular.nome}"