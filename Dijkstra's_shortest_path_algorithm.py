# use Dijkstra's algorithm to calculate the shortest path from the source point
# to every other point in the graph

import numpy as np

# initialize corrected data

processed_data = []

with open(r"C:\Users\ASUS\Desktop\dijkstraData.txt", 'r') as file:
    for str_line in file:
        str_line = str_line.replace(',', ' ')
        str_line = str_line.split()
        # now str_line is a list of chars
        str_line.pop(0)
        # poped out the first element
        # now split the lists at a range of 2
        cor_split = np.array_split(str_line, len(str_line) / 2)
        processed_data.append(cor_split)
# what is above is for preprocessing the data

# the below is for figuring out the Dijkstra'a algorithm

# step1: initialize processed vertices and shortest-path distance, shortest paths
num_of_vertices = 200
vertices_processed = [1]
dist = [0]
min_value = 1e5
best_ending_point = None
best_staring_point = None

while len(vertices_processed) != num_of_vertices:
    for i in vertices_processed:
        for point in processed_data[i - 1]:
            # this is to make sure the end vertex is not in the processed vertexes
            if point[0] not in processed_data:
                if point[1] < min_value:
                    min_value = point[1]
                    best_starting_point = i
                    best_ending_point = point[0]

    # include the processed point in X
    vertices_processed.append(best_ending_point)
    dist.append(min_value + dist[-1])
