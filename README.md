# Adoption of electric vehicles - an agent based model approach

For my master thesis, I decided to use agent-based modeling to determine the adoption possibilities of electric vehicles in Poland. Agents are considered as nodes in networks. They have only two states: $1$ states for beings against electric vehicles and $-1$ means a person is for this innovation. They're set in the created environment, which consists of four networks. It reflects the behavior of people in real life. All relationships between people have different properties. For this model, I analyzed the following networks: neighborhood network, social interaction network, temporary social interaction network, and social media network.

Using high-performance computing hardware cluster BEM, I was able to conduct more than $1000$ simulations for different sets of parameters. Parameters, which were investigated:
* $p$ - the probability of being a conformist by an agent,
* $a$ - the weight of neighbourhood network,
* $b$ - the weight of social interaction network,
* $c$ - the weight of temporary social interaction network,
* $d$ - the weight of social media network,
* $h$ - the probability of positive influence by social media.

Based on the high amount of simulation, I decided to group all results into four classes of similarities and, for every one of them present an exemplary graph with trajectories of magnetization.

<h3> Slow convergence of some trajectories </h3>
In the first group, the parameters cause the behavior of magnetization as presented in the figure below. We can see that for lower values of probabilities $p$, the system stabilizes almost immediately at a given level, and it is difficult for the society to make at least little changes in the opinion about EVs. On the other hand, if values of probability of independence are big enough $(p > 0.25)$, we can see that the system becomes disordered and for all parameters, final magnetization fluctuates around $0$. <br> <br>

<img src="https://github.com/dpalatynski/Master-Thesis/blob/main/results/plots/figure4_3.jpg">

<h3> Quick convergence to steady states </h3>
This group is characterized by magnetization being almost constant - except a short initial phase. Trajectories from this group approach the steady state almost immediately. An example of this similarity class is presented in the figure below. From this plot, we can observe that all trajectories are set in order from the low probabilities $p$ to the higher values. Hence, it is the most influential parameter for this type of graph. <br> <br>

<img src="https://github.com/dpalatynski/Master-Thesis/blob/main/results/plots/figure4_5.jpg">

<h3> Irregular fluctuations </h3>
The next class of similarity is characterized by quick drops of magnetization to a given value and its large irregular fluctuations around this value. This group is highly dependent on social media influence because the corresponding parameter $d$ is high. Exemplary trajectories of this similarity class are presented in the figure below. <br> <br>

<img src="https://github.com/dpalatynski/Master-Thesis/blob/main/results/plots/figure4_8.jpg">

<h3> Intersections of some trajectories </h3>
Among all sets of parameters, there are some values for which we can observe behavior not covered by the previous classes. These trajectories are shown in the figure below. Firstly, considering probabilities $p$ we can see that for lower values of this parameter $p ∈ (0.1, 0.25)$ the magnetization behaves like in the quick convergence group. It immediately drops to a value around $1 − p$ with an additional influence of other parameters, which raise or lower a trajectory by a small amount. Then, as for the slow converging, there are some values of $p$ for which we can see a smooth decrease in time to a specific level based on other parameters in the considered set. What is more, for $p > 0.35$ we can see some unexpected behavior in this model. The trajectory for $p = 0.35$ crosses other higher values of probability of independence. Finally, all trajectories stabilize at some point, however their order is not anticipated here.  <br> <br>

<img src="https://github.com/dpalatynski/Master-Thesis/blob/main/results/plots/figure4_11.jpg">

To better understand what has been done in these simulations, let us consider a graph below, in which we can see the same simulations but for a higher value of $p$. For lower probability $p < 0.29$, magnetization stabilizes at a high level, which reflects the situation when the final number of electric vehicles has been reached in the society and then it is impossible to enlarge a number of them. This situation blocks the diffusion of innovation on a specific level. However, increasing the value of $p$ such that p ∈ (0.29, 0.35) makes few trajectories crawl to their stable point. For all these values of the probability $p$ there are intersections with trajectories in which the probability of independence is higher. <br> <br>

<img src="https://github.com/dpalatynski/Master-Thesis/blob/main/results/plots/figure4_12.jpg">

A more detailed analysis of results is performed in a master thesis. Here you could find only a few of the most important issues from this thesis.
