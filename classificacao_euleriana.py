import numpy as np

while True:
    print('\n-----------------------------------  DESCRIÇÃO  ------------------------------------')
    print('Programa que informa se existe ou não um caminho entre dois vértices diferentes de um \n'
          'grafo orientado ou não orientado.')
    print('-----------------------------------  INSTRUÇÕES  -----------------------------------')
    print('[1] Os vértices são designados por 0, 1, 2,...                                   \n'
          '[2] Por exemplo, o grafo dado a seguir                                           \n'
          '                                       0-----1                                   \n'
          '                                       | \   |                                   \n'
          '                                       |  \  |                                   \n'
          '                                       |   \ |                                   \n'
          '                                       |    \|                                   \n'
          '                                       3-----2                                   \n'
          'terá a seguinte matriz de adjacência: [[0,1,1,1],[1,0,1,0],[1,1,0,1],[1,0,1,0]]')
    print('-----------------------------  ENTRE COM OS DADOS  ---------------------------------')
    A = input('Digite a matriz de adjacência: ')

    # Matriz de adjacência interna gerada
    arr = np.array(eval(A))
    listv=list()
    listg=list()
    k=0
    for i in range(0, len(arr)):
        grau =0
        for j in range(0, len(arr)):
            if arr[i, j] == 1:
                grau = grau+1

        if grau % 2 == 1:
            k = k + 1
            listv.append(i)
            listg.append(grau)
    print('\n ***********************************  RESPOSTA  ***********************************')
    if k==0:
        print(' O grafo em questão tem um circuito de Euler, pois todos os vértices têm grau par.')
    elif k==2:
        print(f' O grafo em questão tem um caminho de Euler, pois possui dois vértices {listv[0]} e {listv[1]} com\n'
              f' graus ímpares {listg[0]} e {listg[1]}, respectivamente, e os demais com grau par.')
    else:
        print(f' O grafo em questão não é Euleriano, pois possui mais de dois vértices com grau \n'
              f' ímpar. Por exemplo: o vértice {listv[0]} com grau {listg[0]}, o vértice {listv[1]} com grau {listg[1]}, o vértice \n'
              f' {listv[2]} com grau {listg[2]} etc.')
    print(' **********************************************************************************')
    input('Digite Enter para continuar: ')
