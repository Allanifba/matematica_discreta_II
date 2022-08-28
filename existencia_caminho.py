# programa que verifica se existe um caminho simples entre dois vértices distintos de um grafo G
# of a graph

from collections import defaultdict
import numpy as np
while True:
    # This class represents a directed graph using adjacency list representation
    class Graph:

        def __init__(self, vertices):
            self.V = vertices  # No. of vertices
            self.graph = defaultdict(list)  # default dictionary to store graph

        # function to add an edge to graph
        def addEdge(self, u, v):
            self.graph[u].append(v)

        # Use BFS to check path between s and d
        def isReachable(self, s, d):
            # Mark all the vertices as not visited
            visited = [False] * (self.V)

            # Create a queue for BFS
            queue = []

            # Mark the source node as visited and enqueue it
            queue.append(s)
            visited[s] = True

            while queue:

                # Dequeue a vertex from queue
                n = queue.pop(0)

                # If this adjacent node is the destination node,
                # then return true
                if n == d:
                    return True

                # Else, continue to do BFS
                for i in self.graph[n]:
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True
            # If BFS is complete without visited d
            return False


    # Create a graph given in the above diagram


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
    A = input('Digite a matriz de adjacência: ')
    u = int(input('Digite o vértice inicial: '))
    v = int(input('Digite o vértice final: '))
    if u==v:
        print('Os vértices devem ser distintos.')
        exit()

    print('\n ***********************************  RESPOSTA  ***********************************')
    arr = np.array(eval(A))
    g = Graph(len(arr))
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if arr[i,j]!=0:
                g.addEdge(i,j)

    if g.isReachable(u, v):
        print(" Existe um caminho do vértice %d para o vértice %d" % (u, v))
    else:
        print(" Não existe um caminho do vértice %d para o vértice %d" % (u, v))

    print('\nModificado por Allan de Sousa Soares - IFBA VDC')
    print('Versão original por Neelam Yadav disponível em: \n'
          'https://www.geeksforgeeks.org/find-if-there-is-a-path-between-two-vertices-in-a-given-graph/')
    input('Digite Enter para continuar: ')






    # This code is contributed by Neelam Yadav
