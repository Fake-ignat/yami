from django.shortcuts import render
from .data import shindler

# Create your views here.
def index(request):
    id = request.GET.get("id", 1)
    return render(request, 'mos/base.html',
                  shindler[id])