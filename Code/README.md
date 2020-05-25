## Installation instructions
Clone the repository and be sure to use the following package versions:[Python3.5](https://www.python.org/) with [numpy](http://www.numpy.org/) and [tensorflow v1.2](https://www.tensorflow.org/). We **do not** recommend using Python3.6 since its *multiprocessing* module is unreliable (we learned this the hard way :grimacing:).


## Running examples

To run the code, move to the *src* folder and execute *run.py*. This code receives four parameters: The RL agent (which can be "lrm-dqn", "lrm-qrm", "dqn", or "human"), the environment (which can be "symbol", "cookie", or "keys"), the random seed, and the number of threads used when learning a Reward Machine. 

```
python3 run.py --agent=<agent> --world=<environment> --seed=<seed> --workers=<threads>
```

For instance, the following command runs LRM+DDQN on the Cookie domain using a random seed of 1 and 16 workers:

```
python3 run.py --agent="lrm-dqn" --world="cookie" --seed=1 --workers=16
```

The results are saved in the './results' folder. We also include four scripts that allow you to replicate the experiments from our paper. They are in the './scripts' folder. After running all of them, you can compute their average performance by executing *python3 export_results.py*. The overall results will be saved in './results/summary'.

The "lrm-dqn" agent uses LRM to learn an RM and DDQN to learn the policy. The "lrm-qrm" option also uses LRM to learn an RM but uses QRM to learn the policy. The other two agent options are baselines. The "dqn" baseline is a DDQN agent that uses a 10-order memory. Meanwhile, the "human" agent runs a hand-designed optimal policy---which gives a useful frame of reference.

The rest of the baselines from the paper (A3C, PPO, and ACER) were run directly using the [OpenAI Baselines](https://github.com/openai/baselines). To do so, we imported our three domains into the [OpenAI GYM](https://github.com/openai/gym). We will provide more details shortly.

Finally, note that we included code that allows you to manually play each environment. Go to *./src/worlds* and run any of the environments' code:

```
python3 cookie_world.py
python3 keys_world.py
python3 symbol_world.py
```

To control the agent, use the WASD keys. The environments are described in the paper.
