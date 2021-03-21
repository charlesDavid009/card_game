from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import Iterationsforms
from .randoms import seedLCG, lcg
from .xorshift import XORShift

xor  = XORShift(1)
js = seedLCG(1)
lists = []

class RandomView(FormView):
    template_name = 'index.html'
    form_class = Iterationsforms

    