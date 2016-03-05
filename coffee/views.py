from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader

from .models import Order
import pdb


def index(request):
    latest_order_list = Order.objects.order_by('date')[:5]
    context = {'latest_order_list': latest_order_list}
    return render(request, 'coffee/index.html', context)

def detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'coffee/detail.html', {'order' : order}) 

def drinks(request, order_id):
    response = "You're looking at drinks for order %s"
    return HttpResponse(response % order_id)

def place_order(request, order_id):
    o = get_object_or_404(Order, pk=order_id)
    try:
        placed_drinks = []
        placed_drinks_ids = request.POST.getlist('placed')
        for drink_id in placed_drinks_ids:
            placed_drinks.append(o.drink_set.get(pk=drink_id))
    except (KeyError, Order.DoesNotExist):
        return render(request, 'coffee/detail.html', {
            'order' : o,
            'error_message' : "You didn't select any drinks.",
        })
    else:
        pdb.set_trace()
        for placed_drink in placed_drinks:
            placed_drink.placed = True
            placed_drink.save()

    return HttpResponseRedirect(reverse('coffee:status', args=(o.id,)))

def status(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'coffee/status.html', {'order' : order})

