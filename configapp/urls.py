from tkinter.font import names

from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name="home"),
    path('categories/<int:category_id>', categories,name='categories' ),
    # path('new_about/<int:category_id>', new_about, name='new_about'),
    path('new_about/<int:new_id>/', new_about, name='new_about'),
    path('update_new/<int:new_id>', update_news, name='update_new'),
    path('add_news',add_news,name='add_news'),
    path('delete/<int:category_id>/', delete_new, name='delete_new'),
    path('',loginPage,name='login'),#
    path('', news_search, name='news_search'),#index.html ga borgani uchun "name/" yo'q

]