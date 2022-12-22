import networkx as nx
import matplotlib.pyplot as plt

# Cria o grafo
G = nx.Graph()

# Adiciona vértices ao grafo
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)


# Adiciona arestas ao grafo
G.add_edge(1, 2)
G.add_edge(2, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 1)

# Calcula as posições dos nós com o layout de mola
pos = nx.spring_layout(G)

# Desenha o grafo
nx.draw(G, pos=pos, with_labels=True)

# Ajusta a posição dos rótulos

# Desenha os rótulos nos nós
nx.draw_networkx_labels(G, pos=pos)

# Exibe o gráfico
plt.show()