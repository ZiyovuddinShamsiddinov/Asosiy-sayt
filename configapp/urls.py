from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name="home"),
    path('categories/<int:category_id>', categories,name='categories' ),
    # path('new_about/<int:category_id>', new_about, name='new_about'),
    path('new_about/<int:new_id>/', new_about, name='new_about'),
    path('update_new/<int:new_id>', update_news, name='update_news'),
    path('add_news',add_news,name='add_news'),
    path('delete/<int:category_id>/', delete_new, name='delete_new'),

]