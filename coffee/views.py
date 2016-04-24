from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from coffee.forms import OrderForm, DrinkFormSet
from .models import Order
import datetime


def index(request):
    return render(request, 'coffee/index.html')


@login_required(login_url='/coffee/login')
def dashboard(request):
    current_order_list = Order.objects.filter(drink__placed=False)\
        .filter(user=request.user)\
        .order_by('date')\
        .distinct()
    previous_order_list = Order.objects.filter(drink__placed=True)\
        .exclude(drink__placed=False)\
        .filter(user=request.user)\
        .order_by('date').distinct()[:5]

    context = {
        'current_order_list': current_order_list,
        'previous_order_list': previous_order_list
    }
    return render(request, 'coffee/dashboard.html', context)


def detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'coffee/detail.html', {'order': order})


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
            'order': o,
            'error_message': "You didn't select any drinks.",
        })
    else:
        for placed_drink in placed_drinks:
            placed_drink.placed = True
            placed_drink.save()

    return HttpResponseRedirect(reverse('coffee:status', args=(o.id,)))


def status(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'coffee/status.html', {'order': order})


def order_new(request):
    if not request.user.is_authenticated():
        redirect('/login/?next=%s' % request.path)
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.date = datetime.datetime.now()
            if request.user:
                order.user = request.user
            drink_formset = DrinkFormSet(request.POST, instance=order)
            if drink_formset.is_valid():
                order.save()
                drink_formset.save()
                return HttpResponseRedirect(reverse('coffee:dashboard'))
    else:
        form = OrderForm()
        drink_formset = DrinkFormSet(instance=Order())
    return render(request, 'coffee/order_edit.html', {
        'form': form,
        'drink_formset': drink_formset,
        })


def order_edit(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if order.user is not None:
        if not order.user == request.user:
            return redirect('/coffee/login')
    return render(request, 'coffee/order_edit.html')


