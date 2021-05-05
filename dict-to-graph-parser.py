import numpy as np
from helpers import string_to_range, ask_for_years_range, normalize
from igraph import *

# Layouts and plotting

color_dict = {0: 'gray', 1: 'red'}
visual_style = {}
#visual_style["vertex_size"] = 15

visual_style["vertex_label_dist"] = 1
visual_style["edge_width"] = 0.5 #[1 + 2 * int(is_formal) for is_formal in g.es["is_formal"]]
visual_style["edge_color"] = 'red'
#visual_style["bbox"] = (600, 600)
visual_style["margin"] = 65

# Initialize dictionary
read_dictionary = np.load('result-final.npy',allow_pickle='TRUE').item()

years = ask_for_years_range(read_dictionary.keys())
year_dict_with_graph_prop = dict()

for year in years:
    g = Graph()
    articles = read_dictionary[year]

    for article in articles:
        index_array = []
        for author in article["authors"]:
            g_index = -1
            try:
                # Try to find vertex.
                g_index = g.vs.find(author).index
            except ValueError:
                # Add if it doesn't exist.
                g_index = g.add_vertex(author).index
            
            index_array.append(g_index)
        
        for i in range(len(index_array)):
            for j in range(i+1, len(index_array)):
                try: 
                    # Try to find edge.
                    g.get_eid(index_array[i],index_array[j])
                except InternalError: 
                    # Add if it doesn't exist.
                    g.add_edge(index_array[i],index_array[j])

    
#     year_dict_with_graph_prop[year] = { 
#         'vertices': len(g.vs['name']),
#         'links': len(g.get_edgelist()),
#         'clique_number': g.clique_number(),
#         'diameter': g.diameter(),
#         'clustering_coefficient': g.transitivity_undirected(),
#         'max_degree': max(g.degree()),
#         'vertices-without-links': len(g.vs.select(lambda vertex: vertex.degree() == 0))
#     }

# np.save('year_dict_with_graph_prop.npy', year_dict_with_graph_prop)
    g.vs['degree'] = g.degree()
    
    # g.write_pickle(f'graph/graph_{year}')
    visual_style["layout"] = g.layout_kamada_kawai()
    visual_style["vertex_label"] = g.vs["name"]
    visual_style["vertex_color"] = ['red' if degree != 0 else 'gray' for degree in g.vs["degree"]]
    visual_style["vertex_label_size"] = normalize(g.vs['degree'], 2, 20) if len(g.vs['name']) > 75 else normalize(g.vs['degree'], 10, 15)
    visual_style["vertex_size"] = normalize(g.vs['degree'], 5, 15) if len(g.vs['name']) > 75 else normalize(g.vs['degree'], 10, 15)
    visual_style["vertex_frame_width"] = 0.5
    visual_style["margin"] = 90 if len(g.vs) <= 2 else 65
    visual_style["bbox"] = (700, 700)

    plot(g, f'plots/{year}.png', **visual_style)
