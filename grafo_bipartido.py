# Programa que classifica um grafo em bipartido ou não

while True:
    class Graph():

        def __init__(self, V):
            self.V = V
            self.graph = [[0 for column in range(V)] \
                          for row in range(V)]

        # Esta função retorna true se o grafo G[V][V] é bipartido e false caso não seja
        def isBipartite(self, src):

            # Cria uma matriz para armazenar as cores
            # atribuídas a cada vértice. O número de
            # de vértices é usado como índice neste array.
            # O valor '-1' de colorArr[i] é usado para
            # indicar que nenhuma cor atribuída ao vértice
            # vértice 'i'. O valor 1 é usado para indicar
            # que a primeira cor foi atribuída e o valor 0
            # indica que a segunda cor foi atribuída.
            colorArr = [-1] * self.V

            # Atribui-se a primeira cor ao vértice inicial
            colorArr[src] = 1

            # Cria uma fila (FIFO) de número de vértices e
            # enfileira e os enfileira para uma pesquisa
            # em BFS.
            # FIFO = First In First Out
            # BFS = Breadth First Search

            queue = []
            queue.append(src)

            # Executa enquanto houver vértices na fila.
            # (Similar a BFS)
            while queue:

                u = queue.pop()

                # Retorna false se houver um auto-loop
                if self.graph[u][u] == 1:
                    return False;

                for v in range(self.V):

                    # Existe uma aresta de u a v e o destino
                    # v não é colorido.

                    if self.graph[u][v] == 1 and colorArr[v] == -1:

                        # Atribui-se uma cor alternativa a este v
                        # adjacente de u
                        colorArr[v] = 1 - colorArr[u]
                        queue.append(v)

                    # Existe uma aresta de u para v e o destino
                    # v é colorido com a mesma cor que u
                    elif self.graph[u][v] == 1 and colorArr[v] == colorArr[u]:
                        return False

            # Se chegarmos aqui, todos os vértices
            # adjacentes podem ser coloridos com
            # cores alternadas
            return True


    # Entrada de Dados para a Execução acima e Descrição:
    print('\n-----------------------------------  DESCRIÇÃO  ------------------------------------')
    print('Programa que classifica um grafo em bipartido ou não.')
    print('-----------------------------------  INSTRUÇÕES  -----------------------------------')
    print('[1] Por exemplo, o ciclo C4 dado a seguir\n'
          '                                       A-------B                                     \n'
          '                                       |       |                                     \n'
          '                                       |       |                                     \n'
          '                                       D-------C                                     \n'
          'terá uma matriz de adjacência dada por: [[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]]     ')
    print('-----------------------------  ENTRE COM OS DADOS  ---------------------------------')
    g = Graph(int(input('Digite o número de vértices do grafo: ')))
    A = input('Digite a matriz de adjacência associada ao grafo em questão: ')

    g.graph = eval(f'{A}')
    print('\n ***********************************  RESPOSTA  ***********************************')
    if g.isBipartite(0):
        print(' O grafo dado é bipartido.\n')
    else:
        print(' O grafo dado não é bipartido.\n')

    print('Modificado por Allan de Sousa Soares - IFBA VDC')
    print('Versão original por Divyanshu Mehta disponível em: '
          'https://www.geeksforgeeks.org/bipartite-graph/')
    input('Digite Enter para continuar: ')

