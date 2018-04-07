from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DealSerializer
from .models import Deal
from django.contrib.auth.decorators import login_required


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


def detail(request, deal_id):
    deal = get_object_or_404(Deal, pk=deal_id)
    return render(request, 'deal/detail.html', {'deal': deal})
