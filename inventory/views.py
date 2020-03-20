from django.shortcuts import render, HttpResponse

# Create your views here.
from inventory.models import Inventory


def update_stock(request):
    Inventory.populate_stock()
    return HttpResponse('done!')