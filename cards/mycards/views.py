from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import Iterationsforms
#from .randoms import seedLCG, lcg
from .xorshift import XORShift
import numpy as np

lists = []


class XORShift:
    def __init__(self, seed=1, word_length=64):
        self.sign_mask = (1 << (word_length-1))
        self.word_mask = self.sign_mask | (self.sign_mask -1)
        self.next = self._to2scomplement(seed)

    def _to2scomplement(self, number):
        return number & self.word_mask

    def _from2scomplement(self, number):
        return ~(number^self.word_mask) if (number & self.sign_mask) else number

    def seed(self, seed):
        self.next = self._to2scomplement(seed)

    def random(self):
        self.next ^= (self.next << 21) & self.word_mask
        self.next ^= (self.next >> 35) & self.word_mask
        self.next ^= (self.next <<  4) & self.word_mask
        return self._from2scomplement(self.next)



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


def button(request):
    return render(request, 'home.html')

def js_random(request):
    data = Iterationsforms(request.POST)
    if data.is_valid():
        rounds = data.cleaned_data['iteration']
        seedLCG(1)
        for i in range(rounds):
            print(lcg())
            lists.append(lcg())
            context = {"data": data, "lists": lists}
    return render(request, 'home.html', {'data': data, 'lists': lists})


def xorshift(request):
    data = Iterationsforms(request.POST)
    if data.is_valid():
        rounds = data.cleaned_data['iteration']
        xor = XORShift(1)
        for i in range(rounds):
            print(xor.random())
            lists.append(xor.random())
            context = {"data": data, "lists": lists}
    return render(request, 'xorshift.html', {'data': data, 'lists': lists})