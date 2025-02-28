from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name="home"),
    path('categories/<int:category_id>', categories,name='categories' ),
    path('new_about/<int:category_id>', new_about, name='new_about'),
    path('add_news',add_news,name='add_news')

]