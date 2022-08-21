import numpy as np

while True:
    print('-----------------------------------  DESCRIÇÃO  ------------------------------------')
    print('Programa que calcula o número de caminhos de comprimento n de existente entre dois\n'
          'vértices de um grafo.')
    print('-----------------------------------  INSTRUÇÕES  -----------------------------------')
    print('O Exemplo a seguir o ajudará na inserção da matriz de adjacência:\n')
    print('''
            1-------2                                      EXEMPLO
             \     /                           Matriz de adjacência (inserção)
              \   /                         linha 1   linha 2   linha 3   linha 4  
               \ /      ----------------> [[0,1,1,0],[1,0,0,1],[1,0,0,1],[0,1,1,0]]            
                \                                             =
               / \                                  [[0 1 1 0]   linha 1
              /   \                                  [1 0 0 1]   linha 2
             /     \                                 [1 0 0 1]   linha 3
            4-------3                                [0 1 1 0]]  linha 4
                                                                                             ''')
    print('-----------------------------  ENTRE COM OS DADOS  ---------------------------------')

    A = input('Digite a matriz de adjacência do grafo: ')
    C = 1
    comprimento = int(input('Digite o comprimento dos caminhos: '))
    inicial = int(input('Digite o vértice inicial: '))
    final = int(input('Digite o vértice final: '))

    k = 1
    while k <= comprimento:
        C = np.dot(C, eval(A))
        k = k + 1
    print('\n ***********************************  RESPOSTA  ***********************************\n')
    if C[inicial -1,final-1] == 0:
        print(f' Não existe nenhum caminho de comprimento {comprimento} do vértice {inicial} para '
              f'o vértice {final}.                                                                ')
    if C[inicial -1,final-1] == 1:
        print(f' Existe 1 caminho de comprimento {comprimento} do vértice {inicial} para o vértice'
              f' {final}.                                                                         ')
    if C[inicial -1,final-1] > 1:
        print(f' Existem {C[inicial -1,final-1]} caminhos de comprimento {comprimento} do vértice '
              f'{inicial} para o vértice {final}.                                                 ')
    print('\n **********************************************************************************\n')
    print('                       Autoria: Allan de Sousa Soares - IFBA VDC                       ')
    print('              Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')
    esc = input('Digite enter para continuar: ')
