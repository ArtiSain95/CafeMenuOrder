from rest_framework import generics, permissions
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.response import Response


from accounts.models import UserSignUp, Menu
from . import serializers

class SignUp(CreateAPIView):
        queryset = UserSignUp.objects.all()
        serializer_class = serializers.SignUpSerializer

#
class Login(APIView):
        permission_classes = [AllowAny]
        serializer_class = serializers.LoginSerializer

        def post(self, request, *args, **kwargs):
                data = request.data
                serializer = serializers.LoginSerializer(data=data)
                if serializer.is_valid(raise_exception=True):
                        new_data = serializer.data
                        return Response(new_data, status=HTTP_200_OK)
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)




class CafeMenu(generics.ListCreateAPIView):
         queryset =Menu.objects.all()
         serializer_class = serializers.MenuSerializer



# class OrderListCreate(generics.ListCreateAPIView):
#     queryset = OrderedMeal.objects.all()
#     serializer_class = serializers.OrderedMealCreateSerializer

