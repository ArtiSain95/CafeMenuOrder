from django.urls import path
from . import views

urlpatterns = [
    path('s', views.SignUp.as_view()),
    path('', views.Login.as_view()),
    path('menu', views.CafeMenu.as_view()),
    # path('order', views.OrderListCreate.as_view()),

]
