
# Breadth-First Search
def bfs(grafo, vertice):    
    visitados = []
    fila = []
    
    if len(grafo) == 0:
        return "Grafo vazio! Não foi possível realizar busca."

    # PASSO 1
    fila.append(vertice)

    # PASSO 3
    while len(fila) > 0:
        print(f"visitados: {visitados}\nfila: {fila}")

        # PASSO 3.B
        visitados.append(fila[0])

        # PASSO 3.C
        for vizinho in grafo[fila[0]]:
            # PASSO 3.D.II
            if vizinho not in visitados and vizinho not in fila:
                # PASSO 3.D.III
                fila.append(vizinho)

        removido = fila.pop(0)
        # print(f"removido: {removido}")

    # PASSO 4
    return visitados


# BFS Menor Caminho
def menor_caminho(grafo, origem, destino):    
    fila = []
    fila.append(
        {
            'vertice': origem,
            'caminho': [origem]
        }
    )

    visitados = []

    # PASSO 3
    while len(fila) > 0:
        removido = fila.pop(0)
        vertice_atual = removido['vertice']
        caminho_atual = removido['caminho']
        
        
        # PASSO 3.b
        if vertice_atual == destino:
            return caminho_atual

        # PASSO 3.c
        if vertice_atual not in visitados:
            visitados.append(vertice_atual)

        # PASSO 3.d
        vizinhos = grafo[vertice_atual]

        # PASSO 3.e
        na_fila = [item['vertice'] for item in fila] # pega todos os vértices que estão na fila
        for vizinho in vizinhos:

            if vizinho not in visitados and vizinho not in na_fila:
                fila.append(
                    {
                        'vertice': vizinho,
                        'caminho': caminho_atual + [vizinho] 
                    }
                )

    # PASSO 4
    return None


# CRIAR GRAFO
def criar_grafo():
    grafo = {}

    return grafo


# INSERIR VÉRTICE
def inserir_vertice(grafo, vertice):
    if vertice in grafo:
        return
    else:
        grafo[vertice] = []


# INSERIR ARESTA
def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    inserir_vertice(grafo, origem)
    inserir_vertice(grafo, destino)

    if destino in grafo[origem]:
        pass
    else:
        grafo[origem].append(destino)

    if nao_direcionado == True:
        if origem in grafo[destino]:
            pass
        else:
            grafo[destino].append(origem)


# OBTER VIZINHOS
def vizinhos(grafo, vertice):
    if vertice in grafo:
        return grafo[vertice]
    else:
        return []


# LISTAR ADACENCIA
def listar_vizinhos(grafo, vertice):
    if vertice in grafo:
        lista = vizinhos(grafo, vertice)
        print("Vizinhos:", lista)
    else:
        print("Vértice não existe")


# EXIBIR GRAFO
def exibir_grafo(grafo):
    for vertice in grafo:
        print(vertice, "->", grafo[vertice])


# REMOVER ARESTA
def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem in grafo:
        if destino in grafo[origem]:
            grafo[origem].remove(destino)

    if nao_direcionado == True:
        if destino in grafo:
            if origem in grafo[destino]:
                grafo[destino].remove(origem)


# REMOVER VÉRTICE
def remover_vertice(grafo, vertice):
    if vertice in grafo:

        for outro in grafo:
            if vertice in grafo[outro]:
                grafo[outro].remove(vertice)

        del grafo[vertice]


# VERIFICAR ARESTA
def existe_aresta(grafo, origem, destino):
    if origem in grafo:
        if destino in grafo[origem]:
            return True

    return False


# GRAU DOS VÉRTICES
def grau_vertices(grafo):
    graus = {}

    for vertice in grafo:
        entrada = 0
        saida = len(grafo[vertice])

        for outro in grafo:
            if vertice in grafo[outro]:
                entrada += 1

        total = entrada + saida

        graus[vertice] = (entrada, saida, total)

    return graus


# VERIFICAR PERCURSO
def percurso_valido(grafo, caminho):
    if len(caminho) < 2:
        return True

    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]

        if existe_aresta(grafo, origem, destino) == False:
            return False

    return True


def adjacencia():
    grafo = criar_grafo()

    tipo = input("Grafo é não direcionado? (s/n): ").lower()

    if tipo == "s":
        nao_direcionado = True
    else:
        nao_direcionado = False

    while True:
        print("\n========== MENU ==========")
        print("1 - Mostrar grafo")
        print("2 - Inserir vertice")
        print("3 - Inserir Aresta")
        print("4 - Remover vertice")
        print("5 - Remover aresta")
        print("6 - Verificar arestas")
        print("7 - Grau dos vertices")
        print("8 - Listar vizinhos")
        print("9 - Verificar percurso")
        print("10 - Breadth Search")
        print("11 - Menor caminho entre 2 vértices")
        print("0 - Adeus")
        print("==========================")

        op = input("Escolha uma opção: ")

        match op:
            
            case "1":
                exibir_grafo(grafo)

            case "2":
                vertice = input("Digite o vértice: ")
                inserir_vertice(grafo, vertice)

            case "3":
                origem = input("Origem: ")
                destino = input("Destino: ")
                inserir_aresta(grafo, origem, destino, nao_direcionado)

            case "4":
                vertice = input("Vértice para remover: ")
                remover_vertice(grafo, vertice, nao_direcionado)

            case "5":
                origem = input("Origem: ")
                destino = input("Destino: ")
                remover_aresta(grafo, origem, destino, nao_direcionado)

            case "7":
                graus = grau_vertices(grafo)

                for vertice in graus:
                    print(vertice, ":", graus[vertice])

            case "6":
                origem = input("Origem: ")
                destino = input("Destino: ")

                if existe_aresta(grafo, origem, destino):
                    print("Tem sim")
                else:
                    print("Não tem viu")

            case "8":
                vertice = input("Digite o vértice: ")
                listar_vizinhos(grafo, vertice)

            case "9":
                caminho = input("Digite o caminho (A B C): ").split()

                if percurso_valido(grafo, caminho):
                    print("Percurso válido.")
                else:
                    print("Percurso impossível.")

            case "10":
                vertice = input("Digite o vértice que deseja iniciar: ")
                print(bfs(grafo, vertice))
            
            case "11":
                origem = input("Origem: ")
                destino = input("Destino: ")

                caminho = menor_caminho(grafo, origem, destino)
                if caminho:
                    print(f"Menor caminho: {caminho}")
                else:
                    print(f"Não foi possível realizar a busca entre 2 caminhos.")

            case "0":
                print("Encerrando....")
                break
