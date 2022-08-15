import networkx as nx
import random
import pickle
import numpy as np
import sys


def spinson_independent_flip(opinions, spinson):
    opinions[spinson] = -1 if opinions[spinson] == 1 else 1

    return opinions


def spinson_conformity_flip(graphs, opinions, spinson, q, coefficients):
    neighbours_opinion = 0
    for i in range(len(graphs)):
        if len(list(graphs[i].neighbors(spinson))) < q:
            neighbours = list(graphs[i].neighbors(spinson))
        else:
            neighbours = random.sample(list(graphs[i].neighbors(spinson)), q)
        if len(neighbours) != 0:
            neighbours_opinions = [opinions[neighbour] for neighbour in neighbours]
            neighbours_opinion += coefficients[i]*sum(neighbours_opinions)/len(neighbours)
    if neighbours_opinion > 0:
        opinions[spinson] = 1
    elif neighbours_opinion < 0:
        opinions[spinson] = -1

    return opinions


def q_voter_simulation(graphs, p, q, iterations, coefficients, h):
    magnetization = []

    opinions = [1] * len(graphs[0])
    while opinions.count(-1) < 15:  # agents have different opinions at the beginning of simulation
        opinions[random.randint(0, len(graphs[0]) - 1)] = -1

    social_media_opinion = [1]
    opinions = opinions + social_media_opinion

    magnetization.append(sum(opinions[:-1]) / len(graphs[0]))
    for i in range(iterations):
        # in every iteration graph of temporary interactions and opinion of social media is changing
        graphs[-2] = nx.fast_gnp_random_graph(len(graphs[0].nodes()), random.uniform(0.0001, 0.001))
        if random.random() < h:  # social media influence change opinion
            opinions[-1] = -1
        else:
            opinions[-1] = 1
        # choosing neighbours
        for i in range(len(graphs[0])):
            spinson = random.choice(list(graphs[0].nodes()))  # chooses one random node
            if random.random() < p:  # does it act independently?
                if random.random() < 0.5:  # the same probability to change opinion
                    opinions = spinson_independent_flip(opinions, spinson)
            else:
                opinions = spinson_conformity_flip(graphs, opinions, spinson, q, coefficients)

        magnetization.append(sum(opinions[:-1]) / len(graphs[0]))

    return magnetization


def calculate_magnetization(graphs, p, q, mc, iterations, coefficients, h):
    magnetization = np.zeros(iterations + 1)
    for i in range(mc):
        magnetization = magnetization + q_voter_simulation(graphs, p, q, iterations, coefficients, h)
    magnetization = magnetization / mc

    return magnetization


G = nx.read_gpickle('network_neighbourhood.pickle')
K = nx.read_gpickle('social_neighbourhood.pickle')
L = nx.read_gpickle('social_media.pickle')

graphs = [G, K, None, L]
h = float(sys.argv[7])
p = float(sys.argv[1])
q = int(sys.argv[2])
a, b, c, d = float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6])
mc = 50
iterations = 120
coefficients = [a, b, c, d]

magnetizations = calculate_magnetization(graphs, p, q, mc, iterations, coefficients, h)
with open(f'magnetization_p={p}_q={q}_a={a}_b={b}_c={c}_d={d}_h={h}.pkl', 'wb') as file:
    pickle.dump(magnetizations, file)
