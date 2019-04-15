from accounts.models import  MealItem
from .serializers import  OrderedItemCreateSerializer
from rest_framework import  viewsets


# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = OrderedMeal.objects.all()
#     serializer_class = OrderedMealCreateSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = MealItem.objects.all()
    serializer_class = OrderedItemCreateSerializer
