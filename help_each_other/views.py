from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from . import forms
from django.urls import reverse
from . import models
from .models import Charity
from datetime import datetime, timedelta
from django.core import serializers
from django.utils import timezone
import pytz




def home(request):

    lists = Charity.objects.all()

    #expired time
    expired_time = timezone.now() - timedelta(hours=26)

    #query where exipired time is > time created of the post
    time_created = Charity.objects.filter(created_at__lt=expired_time)

    if time_created:
        time_created.delete()

    return render(request, 'help_each_other/home.html', {
        'lists': lists
    })

def show_current_item(request, id):
    item = Charity.objects.filter(id=id)

    return render(request, 'help_each_other/show_current_item.html', {
        'item': item,
        'id': id
    })

def show_item(request, id):
    item = Charity.objects.filter(id=id)
    item_s = serializers.serialize('json', item)


    return JsonResponse(item_s, safe=False)

def address_list(request):
    addresses = models.Charity.objects.order_by().values_list("address", flat=True).distinct()
    return JsonResponse(list(addresses), safe=False)


def leave_charity(request):
    if request.method == 'POST':
        form = forms.CreateCharity(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.gooddoer = request.user
            instance.save()
            return HttpResponseRedirect(reverse("home"))
    else:
        form = forms.CreateCharity()
    return render(request, 'help_each_other/leave_charity.html', {
        'title': 'Leave Charity',
        'form': form
    })



def about(request):
    return render(request, 'help_each_other/about.html', {
        'title': 'About',
    })