# Reasoning agents project - 2019/2020 
# Francesco Caputo, Riccardo Gozzovelli, Mario Vetrini

**Learning Reward Machines for Partially Observable Reinforcement Learning**

Reward Machines (RMs) provide a structured, automata-based representation of a
reward function that enables a Reinforcement Learning (RL) agent to decompose
an RL problem into structured subproblems that can be efficiently learned via
off-policy learning. Here we show that RMs can be learned from experience,
instead of being specified by the user, and that the resulting problem decomposition
can be used to effectively solve partially observable RL problems. We pose the
task of learning RMs as a discrete optimization problem where the objective is
to find an RM that decomposes the problem into a set of subproblems such that
the combination of their optimal memoryless policies is an optimal policy for the
original problem. We show the effectiveness of this approach on three partially
observable domains, where it significantly outperforms A3C, PPO, and ACER, and
discuss its advantages, limitations, and broader potential.

**Content**
This repository is used as a container for sharing the presentation (.pptx and .pdf) of the scientific paper previously listed, together with the original code that was used for it (link to the Bitbucket repository is contained in the paper itself). 
We provided for the code above a new possible use case, more realistic than the toy problem used by the original authors, to check whether RMs  can also be applied for more complex problems.


