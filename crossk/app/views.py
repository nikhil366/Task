from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from app.models import (Item, Category, ItemPrice)
from app.serializers import (
    ItemSerializer, CategorySerializer, ItemPriceSerializer)
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class CategoryView(APIView):

    def get(self, request):
        instance = Category.objects.all()
        serializer = CategorySerializer(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ItemViewSet(APIView):
    pagination_class = PageNumberPagination

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ItemPriceViewSet(APIView):

    def post(self, request):
        serializer = ItemPriceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        items_price = ItemPrice.objects.all()
        serializer = ItemPriceSerializer(items_price, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
