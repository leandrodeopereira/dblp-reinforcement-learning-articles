import numpy as np
from helpers import string_to_range, ask_for_years_range
from igraph import *

# Layouts and plotting

color_dict = {0: 'gray', 1: 'red'}
visual_style = {}
visual_style["vertex_size"] = 15

visual_style["vertex_label_dist"] = 2
#visual_style["edge_width"] = [1 + 2 * int(is_formal) for is_formal in g.es["is_formal"]]
#visual_style["edge_curved"] = False
#visual_style["bbox"] = (600, 600)
visual_style["margin"] = 60

# Initialize dictionary
read_dictionary = np.load('result-correct-title.npy',allow_pickle='TRUE').item()

years = ask_for_years_range(read_dictionary.keys())

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
                    
    g.vs['degree'] = g.degree()
    
    visual_style["layout"] = g.layout_kamada_kawai()
    visual_style["vertex_label"] = g.vs["name"]
    visual_style["vertex_color"] = ['red' if degree != 0 else 'gray' for degree in g.vs["degree"]]

    plot(g, f'plots/{year}.png', **visual_style)
