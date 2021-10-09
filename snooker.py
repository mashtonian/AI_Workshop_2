from def_agents import Agent, RandomAgentProgram
from def_agents import Environment
from def_agents import Thing

red, yellow, green, brown, blue, pink, black = "Red", "Yellow", "Green", "Brown", "Blue", "Pink", "Black"

colours = [yellow, green, brown, blue, pink, black]

values = {red: 1,
          yellow: 2,
          green: 3,
          brown: 4,
          blue: 5,
          pink: 6,
          black: 7
          }


class TrivialSnookerEnvironment(Environment):
    """This environment begins with all fifteen balls. Each can be potted.
    The agent perceives the balls potted and remaining.
    This serves as an example of how to implement a simple
    Environment.
    performance is allocated according to standard snooker scoring,
    ball value and four point penalties for fouls"""

    def __init__(self):
        super().__init__()
        self.status = {'balls remaining': [],
                       'balls potted': []}

        for i in range(15):
            self.ballsRemaining().append(red)
        for c in colours:
            self.ballsRemaining().append(c)

    def percept(self, agent):
        """Returns the status of balls remaining and potted """
        return self.status

    def ballsPotted(self):
        return self.status['balls potted']

    def ballsRemaining(self):
        return self.status['balls remaining']

    def execute_action(self, agent, action):
        """Change balls potted and remaining status; track performance.
        Score ball value for each correct ball potted; -4, -5, -6 or -7
        depending on ball value for each invalid one."""
        if action != "NoOp":
            ballsOn = self.ballsOn()
            if ballsOn is None:
                agent.performance -= max(4, values[action])
            elif action in ballsOn:
                agent.performance += values[action]
                self.pot(action)
            else:
                agent.performance -= max(4, values[action])

    def pot(self, ball):
        if ball == red:
            self.ballsRemaining().remove(ball)
        if ball in colours and self.ballsPotted()[-1] != red:
            self.ballsRemaining().remove(ball)
        self.ballsPotted().append(ball)

    def ballsOn(self):
        if len(self.ballsRemaining()) == 0:
            return None
        elif len(self.ballsPotted()) == 0:
            return [red]

        lastBallPotted = self.ballsPotted()[-1]

        if lastBallPotted == red:
            return colours
        elif lastBallPotted in colours and self.lowestValueBallRemaining() == red:
            return [red]
        else:
            return [self.lowestValueBallRemaining()]

    def lowestValueBallRemaining(self):
        sortedBallsRemaining = sorted(self.ballsRemaining(), key=lambda x: values[x])
        lowestValueBallRemaining = sortedBallsRemaining[0]
        return lowestValueBallRemaining


def RandomSnookerAgent():
    """Randomly choose a ball colour to pot."""
    return Agent(RandomAgentProgram([red, yellow, green, brown, blue, pink, black, "NoOp"]))


def run_SnookerAgent(agent):
    # create an object of TrivialVacuumEnvironment
    environment = TrivialSnookerEnvironment()
    # add agent to the environment
    environment.add_thing(agent)
    # run the environment
    environment.run()
    # check final status of the environment
    print(f'Performance: {agent.performance}')


def MaximumSnookerAgent():
    """A simple maximum scoring agent for the trivial snooker environment. [Figure 2.8]"""
    shotsList = []
    for r in range(15):
        shotsList.append(red)
        shotsList.append(black)

    for s in [yellow, green, brown, blue, pink, black]:
        shotsList.append(s)

    def program(percept):

        if shotsList:
            action = shotsList.pop(0)
        else:
            action = 'NoOp'

        return action

    return Agent(program)


if __name__ == '__main__':
    run_SnookerAgent(RandomSnookerAgent())
    run_SnookerAgent(MaximumSnookerAgent())
