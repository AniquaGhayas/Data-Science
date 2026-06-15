import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import girvan_newman

G = nx.Graph([
    ("A","B"),("B","C"),("C","D"),("D","E"),
    ("E","F"),("F","G"),("G","H"),("H","A"),
    ("B","H"),("C","G"),("D","F")
])

comm1, comm2 = next(girvan_newman(G))

print("Community 1:", list(comm1))
print("Community 2:", list(comm2))

colors = ["lightgreen" if n in comm1 else "orange"
          for n in G.nodes()]

nx.draw(G, with_labels=True, node_color=colors)
plt.title("Community Detection")
plt.show()