from django.db import models
from rest_framework import status
from rest_framework.response import Response

from accounts.validators import validate_author_email

class UserSignUp(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(max_length=240,validators=[validate_author_email],null=False,blank=False)
    username = models.CharField(max_length=200,unique=True,
                             error_messages={
                                 "unique": "This Username is not unique, please try again",
                                 "blank" : "this can't be null"

                             })
    mobile = models.IntegerField(unique=True,error_messages={
                                 "unique": "This Number is not unique, please try again",
                                 "blank" : "this can't be null"

                             })
    password = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
           super(UserSignUp, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

class UserLogin(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=200)
    extra_kwargs = {'password':

                        {'write_only': True}
                    }

#Model for Menu-json file
OPTIONS = [
    ('drinks', 'Drinks'),
    ('fastfood', 'Fastfood'),
    ('deserts','Deserts'),
]
class Menu(models.Model):
    Category = models.CharField(max_length=100, choices=OPTIONS, default='drinks')
    Id = models.BigAutoField(primary_key=True)
    Item = models.CharField(max_length=200)
    Price = models.DecimalField(decimal_places=2, max_digits=10)

    def save(self, *args, **kwargs):
        super(Menu, self).save(*args, **kwargs)


class MealItem(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_item_price = models.DecimalField(decimal_places=3,max_digits=8,null=True, blank=True)

    def save(self, *args, **kwargs):
        self.total_item_price = self.quantity * self.menu.Price
        super(MealItem, self).save(*args, **kwargs)


# class OrderedMeal(models.Model):
#     meal_items = models.ManyToManyField(MealItem, related_name="ordered_item")
#     total_price = models.DecimalField(decimal_places=3,max_digits=8,null=True, blank=True)
#
#     def save(self, *args, **kwargs):
#         self.total_price = self.total_price + self.meal_items.total_item_price
#         super(OrderedMeal, self).save(*args, **kwargs)





