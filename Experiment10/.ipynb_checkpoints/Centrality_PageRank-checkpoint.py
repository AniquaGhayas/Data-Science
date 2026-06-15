import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

print("--- Graph Structural Analysis ---")

# A. Centrality & B. PageRank Analysis
G = nx.Graph([
    ("A","B"),("B","C"),("C","D"),("D","E"),
    ("E","F"),("F","G"),("G","H"),("H","A"),
    ("B","H"),("C","G"),("D","F")
])
degree_cent = nx.degree_centrality(G)
between_cent = nx.betweenness_centrality(G)
pagerank_val = nx.pagerank(G, alpha=0.85)

# Convert to DataFrame and Display Top Nodes
analysis_df = pd.DataFrame(
    {
        "Degree Centrality": degree_cent,
        "Betweenness Centrality": between_cent,
        "PageRank": pagerank_val,
    }
)
print(analysis_df.sort_values(by="PageRank", ascending=False).head(5))

# --- Short Visualization ---
plt.figure(figsize=(8, 5))

# Scale node sizes using a basic list comprehension based on PageRank
node_sizes = [pagerank_val[node] * 5000 for node in G.nodes()]

nx.draw(
    G,
    with_labels=True,
    node_size=node_sizes,
    node_color="skyblue",
    edge_color="lightgray",
)
plt.title("Nodes Scaled by PageRank")
plt.show()