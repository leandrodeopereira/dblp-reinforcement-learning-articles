import numpy as np
import csv
import math

# Initialize dictionary
read_dictionary = np.load('year_dict_with_graph_prop.npy',allow_pickle='TRUE').item()

data_list = [['Year', 'Vertices', 'Links', 'Clique_number', 'Diameter', 'Clustering Coefficient', 'Average Degree' , 'Max Degree', 'Vertices without link']]
line = 1
for year in read_dictionary.keys():
    read_dictionary[year]
    data_list.append([
        year, 
        read_dictionary[year]['vertices'], 
        read_dictionary[year]['links'],
        read_dictionary[year]['clique_number'], 
        read_dictionary[year]['diameter'],
        '-' if math.isnan(read_dictionary[year]['clustering_coefficient']) else '%.2f' % read_dictionary[year]['clustering_coefficient'],
        '%.2f' % read_dictionary[year]['average_degree'],
        read_dictionary[year]['max_degree'],
        read_dictionary[year]['vertices-without-links']
        ])

with open('table_years.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_list)