from atividades import atv1, atv2, atv3

def main():
    op = ""
    
    while op != "0":
        print("1- Lista de adjacência\n2- Matriz\n3- Lista de arestas\n0- Fechar")
        print("Selecione a atividade:")
        op = input()
        
        if op == "1":
            atv1.adjacencia()
        
        elif op == "2":
            atv2.matriz()
            
        elif op == "3":
            atv3.arestas()
            
        elif op == "0":
            print("Fechando...")

        else:
            print("Atividade não encontrada.")
    
    
main()