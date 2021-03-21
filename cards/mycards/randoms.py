import random

def seedLCG(seed):
    global rand
    rand = seed


def lcg():
    a = 1140671485
    c = 128201163
    m = 2**24
    global rand
    rand = (a*rand + c) % m
    return rand

