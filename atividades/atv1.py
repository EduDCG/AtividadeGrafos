# CRIAR GRAFO
def criar_grafo():
    return {}


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
        print("0 - Adeus")
        print("==========================")

        op = input("Escolha uma opção: ")

        if op == "1":
            exibir_grafo(grafo)

        elif op == "2":
            vertice = input("Digite o vértice: ")
            inserir_vertice(grafo, vertice)

        elif op == "3":
            origem = input("Origem: ")
            destino = input("Destino: ")
            inserir_aresta(grafo, origem, destino, nao_direcionado)

        elif op == "4":
            vertice = input("Vértice para remover: ")
            remover_vertice(grafo, vertice, nao_direcionado)

        elif op == "5":
            origem = input("Origem: ")
            destino = input("Destino: ")
            remover_aresta(grafo, origem, destino, nao_direcionado)

        elif op == "7":
            graus = grau_vertices(grafo)

            for vertice in graus:
                print(vertice, ":", graus[vertice])

        elif op == "6":
            origem = input("Origem: ")
            destino = input("Destino: ")

            if existe_aresta(grafo, origem, destino):
                print("Tem sim")
            else:
                print("Não tem viu")

        elif op == "8":
            vertice = input("Digite o vértice: ")
            listar_vizinhos(grafo, vertice)

        elif op == "9":
            caminho = input("Digite o caminho (A B C): ").split()

            if percurso_valido(grafo, caminho):
                print("Percurso válido.")
            else:
                print("Percurso impossível.")

        elif op == "0":
            print("Encerrando....")
            break

        else:
            print("Chapou")


