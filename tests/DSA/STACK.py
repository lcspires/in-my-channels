def criar_no(valor, proximo=None):
    return {'valor': valor, 'proximo': proximo}

def criar_pilha():
    return {'topo': None, 'tamanho': 0}

def push(pilha, valor):
    novo_no = criar_no(valor, pilha['topo'])
    pilha['topo'] = novo_no
    pilha['tamanho'] += 1
    print(f"Valor {valor} adicionado à pilha.")

def pop(pilha):
    if pilha['topo'] is None:
        print("Erro: Pilha vazia!")
        return None
    
    no_removido = pilha['topo']
    valor = no_removido['valor']
    pilha['topo'] = no_removido['proximo']
    pilha['tamanho'] -= 1
    print(f"Valor {valor} removido da pilha.")
    return valor

def listar(pilha):
    if pilha['topo'] is None:
        print("Pilha vazia.")
        return
    
    print("Pilha (topo → base):")
    atual = pilha['topo']
    elementos = []
    
    while atual is not None:
        elementos.append(str(atual['valor']))
        atual = atual['proximo']
    
    print(" → ".join(elementos))
    print(f"Tamanho: {pilha['tamanho']}")

def topo(pilha):
    if pilha['topo'] is None:
        print("Pilha vazia.")
        return None
    return pilha['topo']['valor']

def esta_vazia(pilha):
    return pilha['topo'] is None

def main():
    pilha = criar_pilha()
    
    while True:
        print("\n" + "="*40)
        print("MENU DA PILHA")
        print("="*40)
        print("1. Push (Adicionar elemento)")
        print("2. Pop (Remover elemento)")
        print("3. Listar elementos")
        print("4. Ver topo")
        print("5. Verificar se está vazia")
        print("0. Sair")
        print("="*40)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            try:
                valor = input("Digite o valor a ser adicionado: ")
                try:
                    valor = int(valor)
                except ValueError:
                    try:
                        valor = float(valor)
                    except ValueError:
                        pass
                push(pilha, valor)
            except Exception as e:
                print(f"Erro ao adicionar elemento: {e}")
                
        elif opcao == "2":
            pop(pilha)
            
        elif opcao == "3":
            listar(pilha)
            
        elif opcao == "4":
            topo_valor = topo(pilha)
            if topo_valor is not None:
                print(f"Topo da pilha: {topo_valor}")
                
        elif opcao == "5":
            if esta_vazia(pilha):
                print("A pilha está vazia.")
            else:
                print("A pilha não está vazia.")
                
        elif opcao == "6":
            print(pilha)
                
        elif opcao == "0":
            print("Saindo do programa...")
            break
            
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()