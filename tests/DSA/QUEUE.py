def criar_no(valor, proximo=None):
    return {'valor': valor, 'proximo': proximo}

def criar_fila():
    return {'inicio': None, 'fim': None, 'tamanho': 0}

def enqueue(fila, valor):
    novo_no = criar_no(valor)
    
    if fila['fim'] is None:  # Fila vazia
        fila['inicio'] = novo_no
        fila['fim'] = novo_no
    else:
        fila['fim']['proximo'] = novo_no
        fila['fim'] = novo_no
    
    fila['tamanho'] += 1
    print(f"Valor {valor} adicionado à fila.")

def dequeue(fila):
    if fila['inicio'] is None:
        print("Erro: Fila vazia!")
        return None
    
    no_removido = fila['inicio']
    valor = no_removido['valor']
    fila['inicio'] = no_removido['proximo']
    
    if fila['inicio'] is None:
        fila['fim'] = None
    
    fila['tamanho'] -= 1
    print(f"Valor {valor} removido da fila.")
    return valor

def listar(fila):
    if fila['inicio'] is None:
        print("Fila vazia.")
        return
    
    print("Fila (início → fim):")
    atual = fila['inicio']
    elementos = []
    
    while atual is not None:
        elementos.append(str(atual['valor']))
        atual = atual['proximo']
    
    print(" → ".join(elementos))
    print(f"Tamanho: {fila['tamanho']}")

def inicio(fila):
    if fila['inicio'] is None:
        print("Fila vazia.")
        return None
    return fila['inicio']['valor']

def fim(fila):
    if fila['fim'] is None:
        print("Fila vazia.")
        return None
    return fila['fim']['valor']

def esta_vazia(fila):
    return fila['inicio'] is None

def main():
    fila = criar_fila()
    
    while True:
        print("\n" + "="*40)
        print("MENU DA FILA")
        print("="*40)
        print("1. Enqueue (Adicionar elemento)")
        print("2. Dequeue (Remover elemento)")
        print("3. Listar elementos")
        print("4. Ver início")
        print("5. Ver fim")
        print("6. Verificar se está vazia")
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
                enqueue(fila, valor)
            except Exception as e:
                print(f"Erro ao adicionar elemento: {e}")
                
        elif opcao == "2":
            dequeue(fila)
            
        elif opcao == "3":
            listar(fila)
            
        elif opcao == "4":
            inicio_valor = inicio(fila)
            if inicio_valor is not None:
                print(f"Início da fila: {inicio_valor}")
                
        elif opcao == "5":
            fim_valor = fim(fila)
            if fim_valor is not None:
                print(f"Fim da fila: {fim_valor}")
                
        elif opcao == "6":
            if esta_vazia(fila):
                print("A fila está vazia.")
            else:
                print("A fila não está vazia.")
                
        elif opcao == "0":
            print("Saindo do programa...")
            break
            
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()