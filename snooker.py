from def_agents import Agent, RandomAgentProgram
from def_agents import Environment
from def_agents import Thing


# Ball Classes
class Ball(Thing):
    def __eq__(self, other):
        return self.value == other.value

    pass


class Red(Ball):
    def __init__(self):
        self.value = 1

    def __repr__(self):
        return "Red"

    def __str__(self):
        return "Red"


class Colour(Ball):
    pass


class Yellow(Colour):
    def __init__(self):
        self.value = 2

    def __repr__(self):
        return "Yellow"


class Green(Colour):
    def __init__(self):
        self.value = 3

    def __repr__(self):
        return "Green"


class Brown(Colour):
    def __init__(self):
        self.value = 4

    def __repr__(self):
        return "Brown"


class Blue(Colour):
    def __init__(self):
        self.value = 5

    def __repr__(self):
        return "Blue"


class Pink(Colour):
    def __init__(self):
        self.value = 6

    def __repr__(self):
        return "Pink"


class Black(Colour):
    def __init__(self):
        self.value = 7

    def __repr__(self):
        return "Black"


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

        for i in range(1):
            self.status['balls remaining'].append(Red())
        for ball in [Yellow(), Green(), Brown(), Blue(), Pink(), Black()]:
            self.status['balls remaining'].append(ball)

    def run(self):
        super().run(1000)

    def thing_classes(self):
        return [Ball]

    def percept(self, agent):
        """Returns the status of balls remaining and potted """
        return self.status

    def ballsPotted(self):
        return self.status['balls potted']

    def ballsRemaining(self):
        return self.status['balls remaining']

    def execute_action(self, agent, action):
        """Change balls potted and remaining status; track performance.
        Score ball value for each correct ball potted; -4 for each invalid one."""
        if action is not "NoOp":
            matchingBalls = [b for b in self.ballsRemaining() if b == action]
            ballOn = self.ballOn()
            if ballOn is None:
                agent.performance -= 4
            elif isinstance(action, ballOn):
                agent.performance += action.value
                self.pot(action)
            else:
                agent.performance -= 4

    def pot(self, ball):

        if isinstance(ball, Red):
            self.ballsRemaining().remove(ball)

        if issubclass(type(ball), Colour) and not isinstance(self.lowestValueBallRemaining(), Red):
            self.ballsRemaining().remove(ball)

        self.ballsPotted().append(ball)

    def ballOn(self):
        if len(self.ballsRemaining()) == 0:
            return None
        elif len(self.ballsPotted()) == 0:
            return Red
        else:
            lastBallPotted = self.ballsPotted()[-1]

        if isinstance(lastBallPotted, Red) and isinstance(self.lowestValueBallRemaining(), Red):
            return Colour
        elif isinstance(lastBallPotted, Colour):
            return Red
        else:
            return self.lowestValueBallRemaining()

    def lowestValueBallRemaining(self):
        sortedBallsRemaining = sorted(self.ballsRemaining(), key=lambda x: x.value)
        lowestValueBallRemaining = sortedBallsRemaining[0]
        return lowestValueBallRemaining


def RandomSnookerAgent():
    """Randomly choose a ball colour to pot."""
    return Agent(RandomAgentProgram([Red(), Yellow(), Green(), Brown(), Blue(), Pink(), Black(), "NoOp"]))


def run_RandomSnookerAgent():
    # create an object of the RandomVacuumAgent
    agent = RandomSnookerAgent()
    # create an object of TrivialVacuumEnvironment
    environment = TrivialSnookerEnvironment()
    # add agent to the environment
    environment.add_thing(agent)
    # run the environment
    environment.run()
    # check final status of the environment
    print(f'Performance: {agent.performance}')


if __name__ == '__main__':
    run_RandomSnookerAgent()
