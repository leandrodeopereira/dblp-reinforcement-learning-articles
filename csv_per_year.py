import numpy as np
import csv

# Initialize dictionary
read_dictionary = np.load('year_dict_with_graph_prop.npy',allow_pickle='TRUE').item()

data_list = [['Year', 'Vertices', 'Links', 'Clique_number', 'Diameter', 'Clustering Coefficient', 'Max Degree']]
line = 1
for year in read_dictionary.keys():
    read_dictionary[year]
    data_list.append([
        year, 
        read_dictionary[year]['vertices'], 
        read_dictionary[year]['links'],
        read_dictionary[year]['clique_number'], 
        read_dictionary[year]['diameter'],
        read_dictionary[year]['clustering_coefficient'],
        read_dictionary[year]['max_degree']
        ])



with open('table_years.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(data_list)