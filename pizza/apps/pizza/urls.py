from django.urls import path
from pizza.apps.pizza.views import MainPage, CreateOrder

app_name = 'pizza'

urlpatterns = [
    path('', MainPage.as_view(), name='pizza'),
    path('create_order/', CreateOrder.as_view(), name='create_order')

]
