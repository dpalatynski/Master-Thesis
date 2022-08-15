import networkx as nx
import math
import random


# Coordinates of boundaries of area of Lower Silesian Voivodeship
NORTH = 51.8047222
EAST = 14.8172222
SOUTH = 50.0961111
WEST = 17.795

# Population
POPULATION = 2901200
DEGREE_URBANIZATION = 0.606
RATIO_WITH_SALARY_MORE_10K = 0.062
NUMBER_OF_HOUSEHOLDS = int(RATIO_WITH_SALARY_MORE_10K * DEGREE_URBANIZATION * POPULATION)

# Due to restricted computational power one agent describes 10 people
NUMBER_OF_HOUSEHOLDS = int(NUMBER_OF_HOUSEHOLDS/10)

# Rectangular network:
HEIGHT = NORTH - SOUTH
WIDTH = WEST - EAST
NUMBER_OF_POINTS = NUMBER_OF_HOUSEHOLDS

NUMBER_OF_NODES_HEIGHT = int(math.sqrt(HEIGHT/WIDTH * NUMBER_OF_POINTS))
NUMBER_OF_NODES_WIDTH = int(NUMBER_OF_POINTS/NUMBER_OF_NODES_HEIGHT)

LENGTH_HEIGHT = HEIGHT/NUMBER_OF_NODES_HEIGHT
LENGTH_WIDTH = WIDTH/NUMBER_OF_NODES_WIDTH

G = nx.grid_2d_graph(NUMBER_OF_NODES_HEIGHT, NUMBER_OF_NODES_WIDTH)
G = nx.convert_node_labels_to_integers(G)

NUMBER_OF_NODES = NUMBER_OF_NODES_HEIGHT*NUMBER_OF_NODES_WIDTH

K = nx.barabasi_albert_graph(NUMBER_OF_NODES, 1)
node_mapping = dict(zip(K.nodes(), sorted(K.nodes(), key=lambda k: random.random())))
K = nx.relabel_nodes(K, node_mapping)

L = nx.star_graph(len(G))
mapping = {0:len(G), len(G):0}
L = nx.relabel_nodes(L, mapping)

nx.write_gpickle(G, 'network_neighbourhood.pickle')
nx.write_gpickle(K, 'social_neighbourhood.pickle')
nx.write_gpickle(L, 'social_media.pickle')
