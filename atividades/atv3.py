def criar_grafo():
    vertices = []
    arestas = []

    return vertices, arestas



def inserir_vertice(vertices, vertice):

    for v in vertices:
        if v == vertice:
            print(f"{vertice} já existe!")
            return

    vertices.append(vertice)



def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    origem_existe = False
    destino_existe = False

    for v in vertices:
        if v == origem:
            origem_existe = True
        elif v == destino:
            destino_existe = True
        if origem_existe and destino_existe:
            break

    if not origem_existe:
        print(f"{origem} não existe, criando origem...")
        inserir_vertice(vertices, origem)

    if not destino_existe:
        print(f"{destino} não existe, criando destino...")
        inserir_vertice(vertices, destino)

    # PASSO 2
    arestas.append([origem, destino])

    # PASSO 3
    if nao_direcionado:
        arestas.append([destino, origem])



def remover_aresta(arestas, origem, destino, nao_direcionado=False):

    encontrou_algo = False
    for i, aresta in enumerate(arestas):
        if [origem, destino] == aresta:
            arestas.pop(i)
            encontrou_algo = True

        if nao_direcionado and [destino, origem] == aresta:
            arestas.pop(1)

    if not encontrou_algo:
        print("Aresta não encontrada.")

def remover_vertice(vertices, arestas, vertice):

    # PASSO 1
    existe_vertice = False
    for i, v in enumerate(vertices):
        # PASSO 2
        if v == vertice:
            vertices.pop(i)
            existe_vertice = True
            break

    if not existe_vertice:
        print("Vértice não encontrado.")

    # PASSO 3
    for i, aresta in enumerate(arestas):
        if aresta[0] == vertice or aresta[1] == vertice:
            aresta.remove(aresta)

def existe_aresta(arestas, origem, destino):

    for aresta in arestas:
      if aresta[0] == origem and aresta[1] == destino:
        return True
    return False

def vizinhos(vertices, arestas, vertice):

    lista_vizinhos = []
    if vertice in vertices:
        for aresta in arestas:
            if aresta[0] == vertice:
                lista_vizinhos.append(aresta[1])
    return lista_vizinhos

def grau_vertices(vertices, arestas, nao_direcionado=False):

    graus = {}

    for vertice in vertices:
        entrada = 0
        saida = 0

        for aresta in arestas:
            if aresta[0] == vertice:
                saida += 1
            if aresta[1] == vertice:
                entrada += 1

        if (nao_direcionado) == False:
            # Arestas não direcionadas são armazenadas em ambos
            # Cada laço (A -> A) é armazenado uma vez mas conta grau 2
            grau = saida
            if [vertice, vertice] in arestas:
                grau += 1
            graus[vertice] = grau
        else:
            graus[vertice] = { "entrada": entrada, "saida": saida, "total": entrada + saida}

    return graus

def percurso_valido(arestas, caminho):

    if len(caminho) < 2:
        return True

    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]
        if existe_aresta(arestas, origem, destino) == False:
            return False

    return True

def listar_vizinhos(vertices, arestas, vertice):

    if vertice in vertices:
        lista = vizinhos(vertices, arestas, vertice)
        if len(lista) == 0:
            print("Vértice não possui os vizinhos")
        else:
            print(f"Vizinhos do {vertice}:")
            for v in lista:
                print(f"- {v}")
    else:
        print("Vértice nem existe")

def exibir_grafo(vertices, arestas):
    print("Vértices: ")
    for v in vertices:
        print(f"- {v}")

    print("Arestas: ")
    for a in arestas:
        print(f"{a[0]} -> {a[1]}")


def arestas():
    vertices, arestas = criar_grafo()

    tipo = input("Grafo é não direcionado? (s/n): ").lower()

    nao_direcionado = True
    if tipo == "s":
        nao_direcionado = True
    elif tipo == "n":
        nao_direcionado = False
    else:
        print("Vai ser não-direcionado por padrão")

    while True:
        print("\n========== MENU ==========")
        print("1 - Mostrar grafo")
        print("2 - Inserir vértice")
        print("3 - Inserir aresta")
        print("4 - Remover vértice")
        print("5 - Remover aresta")
        print("6 - Verificar arestas")
        print("7 - Grau dos vértices")
        print("8 - Listar vizinhos")
        print("9 - Verificar percurso")
        print("0 - Adeus")
        print("==========================")

        op = input("Escolha uma opção: ")

        match op:
            case "1":
                exibir_grafo(vertices, arestas)

            case "2":
                vertice = input("Digite o nome do vértice: ")
                inserir_vertice(vertices, vertice)

            case "3":
                origem = input("Insira o nome da origem: ")
                destino = input("Insira o nome do destino: ")
                inserir_aresta(vertices, arestas, origem, destino, nao_direcionado)

            case "4":
                vertice = input("Vértice para remover: ")
                remover_vertice(vertices, arestas, vertice)

            case "5":
                origem = input("Origem: ")
                destino = input("Destino: ")
                remover_aresta(arestas, origem, destino, nao_direcionado)

            case "6":
                origem = input("Origem: ")
                destino = input("Destino: ")
                if existe_aresta(arestas, origem, destino):
                    print("Já tem essa aresta")
                else:
                    print("Não tem essa aresta")

            case "7":
                graus = grau_vertices(vertices, arestas, nao_direcionado)
                for vertice in graus:
                    print(f"{vertice} - {graus[vertice]}")

            case "8":
                vertice = input("Vértice: ")
                listar_vizinhos(vertices, arestas, vertice)

            case "9":
                caminho = input("Digite o caminho (A B C): ").split()
                if percurso_valido(arestas, caminho):
                    print("Percurso possivel")
                else:
                    print("Percurso impossível")

            case "0":
                print("Adios.")
                break

            case _:
                print("Chapou")