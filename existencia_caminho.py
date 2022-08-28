# programa que verifica se existe um caminho simples entre dois vértices distintos de um grafo G

from collections import defaultdict
import numpy as np

while True:
    # Esta classe representa um gráfico direcionado usando a representação por meio de uma lista de adjacências
    class Graph:

        def __init__(self, vertices):
            self.V = vertices  # Número de vértices
            self.graph = defaultdict(list)  # Dicionário padrão para armazenar o grafo

        # Função para adicionar um vértice ao grafo.
        def addEdge(self, u, v):
            self.graph[u].append(v)

        # Usando a busca em largura (BFS) para checar a existência de uma caminho entre s e d
        def isReachable(self, s, d):
            # Marca todos os vértices como não visitados
            visited = [False] * (self.V)

            # Criar uma fila para a busca em largura
            queue = []

            # Marcar o nó de origem como visitado e o enfileira

            queue.append(s)
            visited[s] = True

            while queue:

                # Desenfileira um vértice da fila
                n = queue.pop(0)

                # Se este nó adjacente for o nó de destino, então retorne true
                if n == d:
                    return True

                # Caso contrário, continue a fazer busca em largura
                for i in self.graph[n]:
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True
            # Se a busca em largura estiver completo sem visitar d
            return False


    # Instruções ao usuário e contribuições pessoais

    print('\n-----------------------------------  DESCRIÇÃO  ------------------------------------')
    print('Programa que informa se existe ou não um caminho entre dois vértices diferentes de um \n'
          'grafo orientado ou não orientado.')
    print('-----------------------------------  INSTRUÇÕES  -----------------------------------')
    print('[1] Os vértices são designados por 0, 1, 2,...                                        \n'
          '[2] Por exemplo, o grafo dado a seguir\n'
          '                                       0------->1                                 \n'
          '                                       |                                          \n'
          '                                       |                                          \n'
          '                                       v                                          \n'
          '                                       2------->3                                 \n'
          'terá a seguinte matriz de adjacência: [[0,1,1,0],[0,0,0,0],[0,1,0,1],[0,0,0,0]]')
    print('-----------------------------  ENTRE COM OS DADOS  ---------------------------------')

    # Dados a serem inseridos pelo usuário
    A = input('Digite a matriz de adjacência: ')
    u = int(input('Digite o vértice inicial: '))
    v = int(input('Digite o vértice final: '))

    # Matriz de adjacência interna gerada
    arr = np.array(eval(A))
    g = Graph(len(arr))

    if u == v:
        print('Os vértices devem ser distintos.')

    # Criação da lista de adjacência a partir da matriz de adjacência dada pelo usuário
    if u != v:
        print('\n ***********************************  RESPOSTA  ***********************************')
        for i in range(0, len(arr)):
            for j in range(0, len(arr)):
                if arr[i, j] != 0:
                    g.addEdge(i, j)

        # Saídas para o usuário
        if g.isReachable(u, v):
            print(" Existe um caminho do vértice %d para o vértice %d" % (u, v))
        else:
            print(" Não existe um caminho do vértice %d para o vértice %d" % (u, v))
    print(' **********************************************************************************')
    print('\nModificado por Allan de Sousa Soares - IFBA VDC')
    print('             Canal: https://www.youtube.com/c/MatematicaParaGenteGrande')
    print('Versão original por Neelam Yadav disponível em: \n'
          'https://www.geeksforgeeks.org/find-if-there-is-a-path-between-two-vertices-in-a-given-graph/')
    input('Digite Enter para continuar: ')

