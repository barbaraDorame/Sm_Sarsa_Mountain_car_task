import random
import math
from collections import defaultdict

class Montana:
    def __init__(self):
        self.x = random.uniform(-0.6, -0.4)
        self.vel = 0

    actions = [1, -1, 0]

    def terminal(self):
        if self.x >= 0.5:
            return True
        else
            return False

    def transition(self, action):
        self.x = self.x + self.vel
        self.vel = self.vel + 0.001 * action - 0.0025 * cos(3 * action)

        if self.x < -1.2:
            self.x = -1.2
            self.vel = 0
        if self.vel < - 0.07:
            self.vel = -0.07
        elif self.vel > 0.07:
            self.vel = 0.07


def Salsa_Episodic(episodes, alpha, gamma, Montana):
    q = defaultdict(float)
    w = defaultdict(lambda: [0 for i in xrange(montana.states)])
    for ep in range(episodes):
        mount = Mountain()
        s = mount.x, mount.y
        a = random.choice(mount.actions) if random.random() < 0.1 else max(
                mount.actions, key=lambda x: sum([y*x for x, y in zip(w[x], a)]))
        while not montana.terminal():
            w[s] = [w[s] + alpha]
            r = montana.transition(a)
            primas = montana.x, montana.y
            if montana.terminal():
                w[a] = [x + alpha * (r - sum([y*x for x, y in zip(w[a], s)])) *
                        y for y, x in zip(s, w[a])]
                break
            a_prima = random.choice(mount.actions) if random.random() < 0.1 else max(
                    mount.actions, key=lambda x: sum([y*x for x, y in zip(w[x], a)]))
            w[a] = [x + alpha * (r + gamma *
                                 sum([y*x for x, y in zip(w[a_prima], primas)])
                                 - sum([y*x for x, y in zip(w[x], a)])) *
                    y for y, x in zip(s, w[a])]
            s, a = primas, prima
    return [((x, y), max(montana.actions, key=lambda a:      q[((x, y), a)]))
            for x in range(10) for y in range(7)]
