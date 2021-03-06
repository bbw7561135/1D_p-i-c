from parameters import *
import numpy as np

class Particle:
    def __init__(self, pos, vel, omegaP, QoverM, move, num):
        self.x = pos
        self.v = vel
        self.q = omegaP**2 * (1 / QoverM) * eps0 * (SIZE / num)
        self.qm = QoverM
        self.mv = move

def twoStream1 ():
    PARTS = []
    sep = 1.0 * SIZE / (NP / 2)
    for i in range(NP / 2):
        # unperturbed position
        x0 = (i + 0.5) * sep

        # perturbation
        theta = 2 * np.pi * MODE * x0 / SIZE
        dx = AMPL * np.cos(theta)
        x1 = x0 + dx
        x2 = x0 - dx

        # periodic boundaries
        if x1 < 0:
            x1 += SIZE
        if x2 < 0:
            x2 += SIZE
        if x1 >= SIZE:
            x1 -= SIZE
        if x2 >= SIZE:
            x2 -= SIZE

        # add to PARTS
        PARTS.append(Particle (x1, -1.0, 1.0, -1.0, True, NP))
        PARTS.append(Particle (x2, 1.0, 1.0, -1.0, True, NP))

    sep = SIZE / NP
    for i in range (NP):
        x0 = (i + 0.5) * sep
        PARTS.append(Particle (x0, 0.0, 1.0, 1.0, False, NP))

    return PARTS

def twoStream2 ():
    PARTS = []
    for i in range(NP / 2):
        x = np.random.uniform(0, SIZE)
        PARTS.append(Particle (x, 1.0, 1.0, -1.0, True, NP))
        x = np.random.uniform(0, SIZE)
        PARTS.append(Particle (x, -1.0, 1.0, -1.0, True, NP))
    for i in range(NP):
        x = np.random.uniform(0, SIZE)
        PARTS.append(Particle (x, 0.0, 1.0, -1.0, False, NP))
    return PARTS

def fourStream ():
    PARTS = []
    for i in range(NP / 4):
        x = np.random.uniform(0, SIZE)
        PARTS.append(Particle (x, 0.5, 1.0, -1.0, True, NP))
        x = np.random.uniform(0, SIZE)
        PARTS.append(Particle (x, -0.5, 1.0, -1.0, True, NP))
        x = np.random.uniform(0, SIZE)
        PARTS.append(Particle (x, -1.5, 1.0, -1.0, True, NP))
        x = np.random.uniform(0, SIZE)
        PARTS.append(Particle (x, 1.5, 1.0, -1.0, True, NP))
    for i in range(NP):
        x = np.random.uniform(0, SIZE)
        PARTS.append(Particle (x, 0.0, 1.0, 1.0, False, NP))
    return PARTS

def plasmaFluc ():
    sep = 1.0 * SIZE / NP
    PARTS = []
    for i in range(NP):
        # unperturbed position
        x0 = (i + 0.5) * sep
        x0 += np.random.uniform(-dX, dX)
        # perturbation
        if (x0 < SIZE / 2 + 5 * dX) and (x0 >= SIZE / 2):
            x0 -= np.abs(x0 - SIZE / 2) * np.sqrt(2.0)

        if x0 < 0:
            x0 += SIZE
        if x0 >= SIZE:
            x0 -= SIZE
        PARTS.append(Particle (x0, 0.0, 1.0, -1.0, True, NP))

    for i in range(NP):
        x0 = (i + 0.5) * sep
        PARTS.append(Particle (x0, 0.0, 1.0, 1.0, False, NP))
    return PARTS

def beamInstability ():
    PARTS = []
    sep = 1.0 * SIZE / NP
    for i in range(NP):
        # unperturbed position
        x0 = (i + 0.5) * sep
        x0 += np.cos(2 * np.pi * x0 / SIZE)

        if x0 < 0:
            x0 += SIZE
        if x0 >= SIZE:
            x0 -= SIZE

        PARTS.append(Particle (x0, -1.0, 1 / np.sqrt(1000.0), -0.001, True, NP))

    n1n2 = 5
    sep = SIZE / (NP / n1n2)
    for i in range (NP / n1n2):
        x0 = (i + 0.5) * sep
        PARTS.append(Particle (x0, 0.0, 1.0, -0.001, True, NP / n1n2))

    ovCharge = 0.0
    for i in range(len(PARTS)):
        ovCharge += PARTS[i].q
    QMi = -SIZE / ovCharge
    sep = 1.0 * SIZE / NP
    for i in range(NP):
        x0 = (i + 0.5) * sep
        PARTS.append(Particle (x0, 0.0, 1.0, QMi, False, NP))
    return PARTS
