import random

from def_agents import Agent
from def_agents import (ReflexVacuumAgent, ModelBasedVacuumAgent, TrivialVacuumEnvironment, compare_agents,
                        RandomVacuumAgent)

random.seed("aima-python")


def run_RandomVacuumAgent():
    # create an object of the RandomVacuumAgent
    agent = RandomVacuumAgent()
    # create an object of TrivialVacuumEnvironment
    environment = TrivialVacuumEnvironment()
    # add agent to the environment
    environment.add_thing(agent)
    # run the environment
    environment.run()
    # check final status of the environment
    assert (environment.status == {(1, 0): 'Clean', (0, 0): 'Clean'})
    print(f'Performance: {agent.performance}')


def run_ReflexVacuumAgent():
    # create an object of the ReflexVacuumAgent
    agent = ReflexVacuumAgent()
    # create an object of TrivialVacuumEnvironment
    environment = TrivialVacuumEnvironment()
    # add agent to the environment
    environment.add_thing(agent)
    # run the environment
    environment.run()
    # check final status of the environment
    assert (environment.status == {(1, 0): 'Clean', (0, 0): 'Clean'})
    print(f'Performance: {agent.performance}')


def run_ModelBasedVacuumAgent():
    # create an object of the ModelBasedVacuumAgent
    agent = ModelBasedVacuumAgent()
    # create an object of TrivialVacuumEnvironment
    environment = TrivialVacuumEnvironment()
    # add agent to the environment
    environment.add_thing(agent)
    # run the environment
    environment.run()
    # check final status of the environment
    assert (environment.status == {(1, 0): 'Clean', (0, 0): 'Clean'})
    print(f'Performance: {agent.performance}')


def run_compare_agents():
    environment = TrivialVacuumEnvironment
    agents = [ModelBasedVacuumAgent, ReflexVacuumAgent]

    result = compare_agents(environment, agents)
    performanceOfModelBasedVacuumAgent = result[0][1]
    performance_ReflexVacuumAgent = result[1][1]

    # The performance of ModelBasedVacuumAgent will be at least as good as that of
    # ReflexVacuumAgent, since ModelBasedVacuumAgent can identify when it has
    # reached the terminal state (both locations being clean) and will perform
    # NoOp leading to 0 performance change, whereas ReflexVacuumAgent cannot
    # identify the terminal state and thus will keep moving, leading to worse
    # performance compared to ModelBasedVacuumAgent.
    assert (performance_ReflexVacuumAgent <= performanceOfModelBasedVacuumAgent)
    for r in result:
        print(f'Agent:  {r[0].__qualname__} had performance: {r[1]}')


def run_Agent():
    def constant_program(percept):
        return percept

    agent = Agent(constant_program)
    result = agent.program(5)
    assert (result == 5)
