from contas.conta import Conta

class ContaPoupanca(Conta):
    """Classe representando uma conta poupança"""
    
    TAXA_RENDIMENTO = 0.005  # 0.5% ao mês
    
    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            return False
        
        if valor > self._saldo:
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
    
    def aplicar_rendimento(self):
        rendimento = self._saldo * self.TAXA_RENDIMENTO
        self._saldo += rendimento
        
        # Importação local para evitar circular import
        from operacoes.deposito import Deposito
        deposito = Deposito(rendimento, self, "Rendimento poupança")
        self.adicionar_operacao(deposito)
    
    def __str__(self):
        return f"Conta Poupança {self.numero} - {self.titular.nome}"