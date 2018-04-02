from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Deal


def index(request):
    all_deals = Deal.objects.all()
    context = {'all_deals': all_deals}
    return render(request, 'deal/index.html', context)


def alldeals(request):
    all_deals = Deal.objects.all()
    context = {'all_deals': all_deals}
    return render(request, 'deal/deals.html', context)


def detail(request, deal_id):
    try:
        deal = Deal.objects.get(pk=deal_id)
    except Deal.DoesNotExist:
        raise Http404("Deal Does Not Exist. Sorry!")
    return render(request, 'deal/detail.html', {'deal': deal})




