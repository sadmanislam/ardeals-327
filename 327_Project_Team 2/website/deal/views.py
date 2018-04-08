from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DealSerializer
from .models import Deal, Category
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Lists all deals or create a new one
class DealList(APIView):

    def get(self, request):
        deals = Deal.objects.all()
        serializer = DealSerializer(deals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DealDetail(APIView):
    def get_object(self, pk):
        try:
            return Deal.objects.get(pk=pk)
        except Deal.objects.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = DealSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = DealSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@login_required
def index(request):
    all_deals = Deal.objects.all()
    context = {'all_deals': all_deals}
    return render(request, 'deal/index.html', context)


def alldeals(request):
    all_deals = Deal.objects.all()
    context = {'all_deals': all_deals}
    return render(request, 'deal/deals.html', context)


def apparels(request):
    category = Category.objects.filter(name="Apparels")
    all_deals = Deal.objects.all()
    context = {'category': category,
               'all_deals': all_deals}
    return render(request, 'deal/category.html', context)


def food(request):
    category = Category.objects.filter(name="Food")
    all_deals = Deal.objects.all()
    context = {'category': category,
               'all_deals': all_deals}
    return render(request, 'deal/category.html', context)


def accessories(request):
    category = Category.objects.filter(name="Accessories")
    all_deals = Deal.objects.all()
    context = {'category': category,
               'all_deals': all_deals}
    return render(request, 'deal/category.html', context)


def services(request):
    category = Category.objects.filter(name="Services")
    all_deals = Deal.objects.all()
    context = {'category': category,
               'all_deals': all_deals}
    return render(request, 'deal/category.html', context)


def electronics(request):
    category = Category.objects.filter(name="Electronics")
    all_deals = Deal.objects.all()
    context = {'category': category,
               'all_deals': all_deals}
    return render(request, 'deal/category.html', context)


def dailyessentials(request):
    category = Category.objects.filter(name="Daily Essentials")
    all_deals = Deal.objects.all()
    context = {'category': category,
               'all_deals': all_deals}
    return render(request, 'deal/category.html', context)


def detail(request, deal_id):
    deal = get_object_or_404(Deal, pk=deal_id)
    all_deals = Deal.objects.all()
    context = {'deal': deal,
               'all_deals': all_deals}
    return render(request, 'deal/detail.html', context)


class DealCreate(CreateView):
    model = Deal
    fields = ['publisher', 'user', 'description_small', 'description_long', 'main_attraction', 'type', 'genre',
              'contact', 'validity', 'category', 'address', 'area', 'longitude', 'latitude', 'thumbnail']
