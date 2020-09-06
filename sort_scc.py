import numpy as np

# python is a language through pass by reference language

# open the data file in readable mode
file_txt = open(r"C:\Users\ASUS\Desktop\scc.txt", 'r')
source_data = []  # initialize list
t = 0

# for line in file_txt:
#     striped_line = line.strip()
#     line_list = striped_line.split(' ')
#     line_list = list(map(int, line_list))
#     source_data.append(line_list)

source_data = [[1, 7], [7, 4], [4, 1], [7, 9], [9, 6], [6, 3], [3, 9], [6, 8], [8, 2], [2, 5], [5, 8]]

num_edges = len(source_data)
num_vertices = np.max(source_data)  # number of vertices
finishing_time = np.zeros(num_vertices)

# finished data initialization step
explored = []
leader = np.zeros(num_vertices)

iterate = list(np.arange(num_vertices))
iterate.reverse()  # reverse the ordering


def DFS(G, i):  # G is the graph, i is the starting node
    explored.append(i)  # mark i as explored
    leader[int(i) - 1] = S
    for edge in find_edges(i,G):
        if edge[1] not in explored:
            DFS(G, edge[1])
    global t, finishing_time
    t = t + 1
    finishing_time[int(i) - 1] = t


def find_edges(starting_point, source):
    satisfied_edges = []
    for index in range(num_edges):
        if source[index][0] == starting_point:
            satisfied_edges.append(source[index])
    return satisfied_edges


# main function the first pass
for i in iterate:
    if (i + 1) not in explored:
        S = i + 1
        DFS(source_data, i + 1)


# end of the main function
# have already calculated the finishing times

def replacement_func(G, finishing_time):
    G_new = np.array(G)
    # exchange the directions of the matrix
    inter_result = np.copy(G_new[:, 0])

    G_new[:, 0] = np.copy(G_new[:, 1])
    G_new[:, 1] = np.copy(inter_result)
    # step2 : replace the values with the finishing times
    G_new = G_new.flatten()

    func = lambda x: finishing_time[x - 1]
    G_new = np.array(list(map(func, G_new)))

    G_new = G_new.reshape([-1, 2])
    return G_new


# the second pass of the algorithm
source_data_new = replacement_func(source_data, finishing_time)

explored = []
leader = np.zeros(num_vertices)
t=0
finishing_time = np.zeros(num_vertices)

for i in iterate:
    if (i + 1) not in explored:
        S = i + 1
        DFS(source_data_new, i + 1)
