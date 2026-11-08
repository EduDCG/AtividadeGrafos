def criar_grafo():

    Matriz = []
    vertices = []
    return Matriz, vertices


def inserir_vertice(matriz, vertices, vertice):

    for V in vertices:
      if V == vertice:
        print(f"Vértice {vertice} já existe!")
        return

    vertices.append(vertice)

    qtd_linhas = len(vertices)

    if qtd_linhas == 0:
      matriz.append([0])

    else:

      for linha in matriz:
        linha.append(0)
      novalinha = []

      i = 0
      while i < qtd_linhas:
        i += 1
        novalinha.append(0)

      matriz.append(novalinha)



def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):

    # PASSO 1
    origem_existe = False
    destino_existe = False
    for v in vertices:
      if v == origem:
        origem_existe = True
      if v == destino:
        destino_existe = True

    if not origem_existe:
      print(f"{origem} não existe, criando origem...")
      inserir_vertice(matriz, vertices, origem)

    if not destino_existe:
      print(f"{destino} não existe, criando destino...")
      inserir_vertice(matriz, vertices, destino)

    # PASSO 2
    i_origem = vertices.index(origem)
    i_destino = vertices.index(destino)

    # PASSO 3
    matriz[i_origem][i_destino] = 1
    print(f"Aresta ({origem}, {destino}) inserida.")

    if nao_direcionado == True: # se for não-direcionado
      matriz[i_destino][i_origem] = 1
      print(f"Aresta ({destino}, {origem}) inserida.")



def remover_vertice(matriz, vertices, vertice):

    # PASSO 1
    vertice_existe = False
    for v in vertices:
      if v == vertice:
        vertice_existe = True
        break

    if (not vertice_existe):
        print(f"Vértice {vertice} não existe!")
        return

    # PASSO 2.1
    indice = vertices.index(vertice)

    # PASSO 2.2
    matriz.pop(indice)

    # PASSO 2.3
    for coluna in matriz:
      coluna.pop(indice)

    # PASSO 2.4
    v = vertices.pop(indice)
    print(f"Vértice {v} removido.")



def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):

    # PASSO 1
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
      print(f"{origem} não existe!")
      return
    if not destino_existe:
      print(f"{destino} não existe!")
      return

    # PASSO 2
    i_origem = vertices.index(origem)
    i_destino = vertices.index(destino)

    # PASSO 3
    matriz[i_origem][i_destino] = 0
    print(f"Aresta ({origem}, {destino}) removida.")

    # PASSO 4
    if nao_direcionado == True:
      matriz[i_destino][i_origem] = 0
      print(f"Aresta ({destino}, {origem}) removida.")


def existe_aresta(matriz, vertices, origem, destino):

    # PASSO 1
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
      print(f"{origem} não existe!")
      return False
    if not destino_existe:
      print(f"{destino} não existe!")
      return False

    # PASSO 2
    i_origem = vertices.index(origem)
    i_destino = vertices.index(destino)

    # PASSO 3
    return matriz[i_origem][i_destino] == 1


def vizinhos(matriz, vertices, vertice):

    # PASSO 1
    vertice_existe = False
    for v in vertices:
      if v == vertice:
        vertice_existe = True
        break

    if (vertice_existe == False):
        print(f"Vértice {vertice} não existe!")
        return

    # PASSO 2
    indice = vertices.index(vertice)

    # PASSO 3
    lista_vizinhos = []

    # PASSO 4
    for i, item in enumerate(matriz[indice]):
      if item == 1:
        lista_vizinhos.append(vertices[i])

    # PASSO 5
    return lista_vizinhos


def grau_vertices(matriz, vertices, nao_direcionado=False):

    graus = {}
    qtd_vertices = len(vertices)

    # para cada vértice
    for i in range(qtd_vertices):
        vertice = vertices[i]

        if nao_direcionado:
            grau = sum(matriz[i])

            if matriz[i][i] > 0:
                grau += matriz[i][i]
                
            graus[vertice] = grau

        else:
            # Grau de saída
            grau_saida = sum(matriz[i])

            # Grau de entrada
            # o j é o índice da linha, mudando em cada loop enquanto o i continua no mesmo lugar (replicando uma coluna da matriz)
            grau_entrada = sum(matriz[j][i] for j in range(qtd_vertices))

            grau_total = grau_saida + grau_entrada
            
            graus[vertice] = {
                "saida": grau_saida,
                "entrada": grau_entrada,
                "total": grau_total
            }

    return graus


def percurso_valido(matriz, vertices, caminho):
    
    if len(caminho) < 2:
        return True
    
    # PASSO 1
    for i in range(len(caminho)-1):
        v1 = caminho[i]
        v2 = caminho[i+1]
        
        # PASSO 2
        if not existe_aresta(matriz, vertices, v1, v2):
            return False
    
    # PASSO 3
    return True



def listar_vizinhos(matriz, vertices, vertice):

    # PASSO 1
    vertice_existe = False
    for v in vertices:
      if v == vertice:
        vertice_existe = True
        break

    if (vertice_existe == False):
      print(f"Vértice {vertice} não existe!")
      return

    # PASSO 2
    lista_vizinhos = vizinhos(matriz, vertices, vertice)

    if len(lista_vizinhos) == 0:
      print(f"{vertice} não possui nenhum vizinho!")
      return

    # PASSO 3
    print(f"Vizinhos de {vertice}:")
    for v in lista_vizinhos:
      print(f"- {v}")


def exibir_grafo(matriz, vertices):
    # PASSO 1
    # junta todas as vértices
    cabecalho = "  " + " ".join(str(v) for v in vertices)
    print(cabecalho)

    # PASSO 2
    for i, linha in enumerate(matriz):
        # transforma os valores em string e junta em uma linha
        linha_formatada = " ".join(str(valor) for valor in linha)
        
        # Exibe o vértice atual seguido dos valores da linha
        print(f"{vertices[i]} {linha_formatada}")


def matriz():

    matriz, vertices = criar_grafo()

    tipo = input("Grafo é não direcionado? (s/n): ").lower()

    nao_direcionado = None
    if tipo == "s":
        nao_direcionado = True
    elif tipo == "n":
        nao_direcionado = False
    else:
      print("chapou, vai ser não-direcionado por padrão")
      nao_direcionado = True

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
          print("MOSTRAR GRAFO")
          exibir_grafo(matriz, vertices)


        elif op == "2":
          print("INSERIR VÉRTICE")
          print("Insira o nome do vértice:")
          vertice = input()
          inserir_vertice(matriz, vertices, vertice)


        elif op == "3":
          print("INSERIR ARESTA")
          print("Insira o nome da origem:")
          origem = input()

          print("Insira o nome do destino:")
          destino = input()

          inserir_aresta(matriz, vertices, origem, destino, nao_direcionado)


        elif op == "4":
          print("REMOVER VÉRTICE")
          print("Insira o nome do vértice a ser removido:")
          vertice = input()
          remover_vertice(matriz, vertices, vertice)


        elif op == "5":
          print("REMOVER ARESTA")
          print("Insira o nome da origem:")
          origem = input()

          print("Insira o nome do destino:")
          destino = input()

          remover_aresta(matriz, vertices, origem, destino, nao_direcionado)


        elif op == "6":
          print("VERIFICAR ARESTA")
          print("Insira o nome da origem:")
          origem = input()

          print("Insira o nome do destino:")
          destino = input()

          existe = existe_aresta(matriz, vertices, origem, destino)
          if existe:
            print(f"Aresta {origem}, {destino} existe.")
          else:
            print(f"Aresta {origem}, {destino} NÃO existe.")


        elif op == "7":
            print("GRAU DE VÉRTICES")
            graus = grau_vertices(matriz, vertices, nao_direcionado)
            for i, grau in enumerate(graus):
                print(f"{grau} - {graus[grau]}")


        elif op == "8":
          print("LISTAR VIZINHOS")
          print("Insira o nome do vértice que deseja listar os vizinhos:")
          vertice = input()
          listar_vizinhos(matriz, vertices, vertice)

        elif op == "9":
            print("VERIFICAR CAMINHO")
            caminho = input("Digite o caminho (A B C): ").split()
            
            if percurso_valido(matriz, vertices, caminho):
                print("Percurso válido.")
            else:
                print("Percurso impossível.")
            
            
        elif op == "0":
            print("Encerrando....")
            break

        else:
            print("Chapou")

