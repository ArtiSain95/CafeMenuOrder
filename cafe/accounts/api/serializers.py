from django.db.migrations import serializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import EmailField
from django.contrib.auth.models import User

from accounts import models
from accounts.models import UserSignUp, Menu,  MealItem


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'id',
            'email',
            'username',
            'mobile',
            'password',
        ]
        extra_kwargs = {"password":
                            {"write_only":True}
                        }
        model = UserSignUp
    def create(self, validated_data):
            email = validated_data['email']
            username = validated_data['username']
            mobile = validated_data['mobile']
            password = validated_data['password']
            user_obj = UserSignUp(
                    username = username,
                     email = email,
                    mobile = mobile,
                     password = password
            )
            user_obj.save()
            return validated_data

class LoginSerializer(serializers.ModelSerializer):
    email = EmailField(label='Email Address', required=True, allow_blank=True)
    class Meta:
        model = UserSignUp
        fields = (
            'email',
            'password',
        )
        extra_kwargs = {"password":
                            {"write_only": True}
                        }
    def validate(self, data):
            user_obj = None
            email = data.get("email", None)
            password = data.get("password", None)
            if not email:
                raise ValidationError("email is required to login")

            user = UserSignUp.objects.filter(email = email, password = password)

            if user.exists() and user.count() == 1:
                user_obj = user.first()
            else:
                raise ValidationError("Incorrect credientials, please try again")
            return  data




#
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = (

            'Category',
            'Id',
            'Item',
            'Price',
        )



class OrderedItemCreateSerializer(serializers.ModelSerializer):
    # menu = MenuSerializer(many=True)
    class Meta:
        model = MealItem
        fields = '__all__'

#
# class OrderedMealCreateSerializer(serializers.ModelSerializer):
#     # menu = MenuSerializer(many=True)
#     class Meta:
#         model = OrderedMeal
#         fields = '__all__'