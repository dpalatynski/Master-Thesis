import networkx as nx
import random
import pickle
import numpy as np


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
    while opinions.count(-1) < 2:  # agents have different opinions at the beginning of simulation
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
    magnetizations = []
    if type(p) == list and type(q) != list:
        for j in range(len(p)):
            magnetization = np.zeros(iterations + 1)
            for i in range(mc):
                magnetization = magnetization + q_voter_simulation(graphs, p[j], q, iterations, coefficients, h)
            magnetizations.append(magnetization / mc)

    elif type(p) != list and type(q) == list:
        for j in range(len(q)):
            magnetization = np.zeros(iterations + 1)
            for i in range(mc):
                magnetization = magnetization + q_voter_simulation(graphs, p, q[j], iterations, coefficients, h)
            magnetizations.append(magnetization / mc)

    return magnetizations


G = nx.read_gpickle('small_network_neighbourhood.pickle')
K = nx.read_gpickle('small_social_neighbourhood.pickle')
L = nx.read_gpickle('small_social_media.pickle')

graphs = [G, K, None, L]
p = 0.01
qs = np.linspace(1, 10, 10)
h = 0.5
mc = 20
iterations = 1000
coefficients = [0.25, 0.25, 0.25, 0.25]

for q in range(len(qs)):
    x = calculate_magnetization(graphs, p, [int(qs[q])], mc, iterations, coefficients, h)
    with open(f'results/magnetization_p={p}_q={int(qs[q])}_a={coefficients[0]}_b={coefficients[1]}'
              f'_c={coefficients[2]}_d={coefficients[3]}_h={h}.pkl', 'wb') as file:
        pickle.dump(x, file)
