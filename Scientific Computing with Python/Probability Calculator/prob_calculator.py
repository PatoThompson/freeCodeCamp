import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        # First we save our keyword arguments as a dictionary
        self.balls = {}
        self.balls.update(kwargs)
        # Then we fill our contents list
        self.contents = []
        for (k,v) in self.balls.items():
            for i in range(v):
                self.contents.append(k)


    def draw(self, number):
        self.drawn = []
        # If the number of balls to draw exceeds the available qunatity, return all the balls
        if number > len(self.contents): number = len(self.contents)
        for i in range(number):
            x = random.randint(1,len(self.contents)) - 1
            self.drawn.append(self.contents[x])
            self.contents.remove(self.contents[x])
        return self.drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    match_count = 0
    # First we make a list out of expected_balls
    balls_to_match = []
    for (k,v) in expected_balls.items():
            for i in range(v):
                balls_to_match.append(k)
    # Then we run the experiment n-times through a copy of the original 'hat' object each time
    for i in range(num_experiments):
        copied_hat = copy.deepcopy(hat)
        # We draw n-balls
        balls_drawn = copied_hat.draw(num_balls_drawn)
        # And check for matches
        match = ''
        for ball in expected_balls:
            if balls_to_match.count(ball) <= balls_drawn.count(ball):
                match += '*'
        # If there is match between balls drawn and balls expected to be drawn, we increase our match counter
        if match == '*'*len(expected_balls):
            match_count += 1
    # Finally, we calculate the probability and return it's value
    probability = match_count / num_experiments
    return probability