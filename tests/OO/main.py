import os
import sys

# Adiciona o diretório raiz ao path do Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from bancos.banco import Banco
from bancos.agencia import Agencia
from clientes.pessoa_fisica import PessoaFisica
from clientes.pessoa_juridica import PessoaJuridica
from contas.conta_corrente import ContaCorrente
from contas.conta_poupanca import ContaPoupanca
from datetime import date

def main():
    """Função principal do sistema bancário"""
    
    print("=" * 60)
    print("SISTEMA BANCÁRIO ORIENTADO A OBJETOS")
    print("=" * 60)
    
    try:
        # Criando o banco
        banco = Banco("Banco Python", "001")
        print(f"✅ Banco criado: {banco}")
        
        # Criando agência
        agencia = Agencia("0001", "Centro", banco)
        banco.adicionar_agencia(agencia)
        print(f"✅ Agência criada: {agencia}")
        
        # Criando clientes
        joao = PessoaFisica("João Silva", "12345678901", date(1990, 5, 15))
        maria = PessoaFisica("Maria Santos", "98765432100", date(1985, 8, 22))
        empresa = PessoaJuridica("Tech Solutions Ltda", "12345678000195", date(2010, 3, 10))
        
        print(f"✅ Clientes criados: {joao.nome}, {maria.nome}, {empresa.nome}")
        
        # Criando contas - com debug dos números
        print("\n🔢 CRIANDO CONTAS:")
        conta_joao = ContaCorrente(joao, agencia, 1000.00, 500.00)
        print(f"   Conta João: {conta_joao.numero}")
        
        conta_maria = ContaPoupanca(maria, agencia, 5000.00)
        print(f"   Conta Maria: {conta_maria.numero}")
        
        conta_empresa = ContaCorrente(empresa, agencia, 20000.00, 2000.00)
        print(f"   Conta Empresa: {conta_empresa.numero}")
        
        # Adicionando contas à agência
        print("\n📋 ADICIONANDO CONTAS À AGÊNCIA:")
        agencia.adicionar_conta(conta_joao)
        print(f"   ✅ Conta {conta_joao.numero} adicionada")
        
        agencia.adicionar_conta(conta_maria)
        print(f"   ✅ Conta {conta_maria.numero} adicionada")
        
        agencia.adicionar_conta(conta_empresa)
        print(f"   ✅ Conta {conta_empresa.numero} adicionada")
        
        print(f"✅ Total de contas na agência: {len(agencia.listar_contas())}")
        
        # Realizando operações
        print("\n💵 REALIZANDO OPERAÇÕES BANCÁRIAS")
        print("-" * 40)
        
        # Operações na conta do João
        print(f"\n📊 Conta do João ({conta_joao.numero}) - Saldo inicial: R$ {conta_joao.saldo:.2f}")
        conta_joao.depositar(500.00)
        print(f"   Depósito de R$ 500,00 → Saldo: R$ {conta_joao.saldo:.2f}")
        
        conta_joao.sacar(200.00)
        print(f"   Saque de R$ 200,00 → Saldo: R$ {conta_joao.saldo:.2f}")
        
        # Tentativa de saque acima do limite
        resultado = conta_joao.sacar(1500.00)
        print(f"   Tentativa de saque de R$ 1.500,00 → {'✅ Sucesso' if resultado else '❌ Falhou'}")
        print(f"   Saldo atual: R$ {conta_joao.saldo:.2f}")
        
        # Operações na conta da Maria
        print(f"\n📊 Conta da Maria ({conta_maria.numero}) - Saldo inicial: R$ {conta_maria.saldo:.2f}")
        conta_maria.depositar(1000.00)
        print(f"   Depósito de R$ 1.000,00 → Saldo: R$ {conta_maria.saldo:.2f}")
        
        conta_maria.sacar(300.00)
        print(f"   Saque de R$ 300,00 → Saldo: R$ {conta_maria.saldo:.2f}")
        
        # Aplicar rendimento na poupança
        if hasattr(conta_maria, 'aplicar_rendimento'):
            saldo_antes = conta_maria.saldo
            conta_maria.aplicar_rendimento()
            rendimento = conta_maria.saldo - saldo_antes
            print(f"   📈 Rendimento de R$ {rendimento:.2f} → Saldo: R$ {conta_maria.saldo:.2f}")
        
        # Operações na conta da empresa
        print(f"\n📊 Conta da Empresa ({conta_empresa.numero}) - Saldo inicial: R$ {conta_empresa.saldo:.2f}")
        conta_empresa.depositar(5000.00)
        print(f"   Depósito de R$ 5.000,00 → Saldo: R$ {conta_empresa.saldo:.2f}")
        
        resultado = conta_empresa.sacar(10000.00)
        print(f"   Saque de R$ 10.000,00 → {'✅ Sucesso' if resultado else '❌ Falhou'}")
        print(f"   Saldo atual: R$ {conta_empresa.saldo:.2f}")
        
        # Demonstrando polimorfismo
        print("\n👥 DEMONSTRAÇÃO DE POLIMORFISMO")
        print("-" * 40)
        
        contas = agencia.listar_contas()
        
        for conta in contas:
            tipo = "Corrente" if isinstance(conta, ContaCorrente) else "Poupança"
            print(f"   {tipo}: {conta} - Saldo: R$ {conta.saldo:.2f}")
        
        # Extratos
        print("\n📋 EXTRATOS BANCÁRIOS")
        print("=" * 60)
        
        for conta in contas:
            print(f"\n{conta}")
            print("-" * 40)
            print(conta.extrato())
        
        # Estatísticas finais
        print("\n📈 ESTATÍSTICAS DO SISTEMA")
        print("=" * 60)
        print(f"   Total de bancos: {Banco.get_total_bancos()}")
        print(f"   Total de contas na agência: {len(contas)}")
        
        saldo_total = sum(conta.saldo for conta in contas)
        print(f"   Saldo total na agência: R$ {saldo_total:.2f}")
        
        # Detalhamento por tipo de conta
        contas_corrente = [c for c in contas if isinstance(c, ContaCorrente)]
        contas_poupanca = [c for c in contas if isinstance(c, ContaPoupanca)]
        
        print(f"   Contas Corrente: {len(contas_corrente)}")
        print(f"   Contas Poupança: {len(contas_poupanca)}")
        
        print("\n🎉 Sistema executado com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro durante a execução: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()