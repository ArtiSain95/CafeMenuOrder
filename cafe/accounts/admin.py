from django.contrib import admin

from .models import UserLogin, UserSignUp, Menu

admin.site.register(UserSignUp)
admin.site.register(UserLogin)
admin.site.register(Menu)
# admin.site.register(OrderedMeal)

