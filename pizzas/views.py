from django.shortcuts import render
from .models import Pizza
# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    '''显示所有主题'''
    pizzas = Pizza.objects.all()
    context = {'pizzas':pizzas}
    return render(request,  'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    '''显示单个主题及其所有条目'''
    pizza = Pizza.objects.get(id=pizza_id)
    entries = pizza.topping_set.all()
    context = {'pizza': pizza, 'topping': entries}
    return render(request, 'pizzas/pizza.html', context)
