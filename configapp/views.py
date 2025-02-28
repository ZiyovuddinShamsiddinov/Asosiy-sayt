from django.shortcuts import render,redirect

from configapp.forms import NewsForm,Categories
from configapp.models import *



def index(request):
    news=News.objects.all()
    categories=Categories.objects.all()
    context={
        'news':news,
        'categories':categories,
    }
    return render(request,'index.html',context=context)

def categories(request,category_id):
    news=News.objects.filter(category_id=category_id)
    categories=Categories.objects.all()
    context={
        'news':news,
        'categories':categories,
    }
    return render(request,'categories.html',context=context)

def new_about(request,category_id):
    new=News.objects.get(pk=category_id)
    context={
        'news':new,
    }
    return render(request,'new_about.html',context=context)

# def add_news(request):
#     if request.method == "POST":
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             news = News.objects.create(**form.cleaned_data)
#             return redirect('home')
#
#     else:
#         form = NewsForm()
#     return render(request,'add_news.html',{'form':form})
#
#
# def add_category(request):
#     if request.method=="POST":
#         form=CategoriesForm(request.POST)
#         if form.is_valid():
#             categories=News.objects.create(**form.cleaned_data) #{'title': 'News0.1', 'context': 'Ziyo6kaZiyo6kaZiyo6kaZiyo6kaZiyo6kaZiyo6kaZiyo6kaZiyo6kaZiyo6kaZiyo6kaZiyo6kaZiyo6kaZiyo6kaZiyo6kaZiyo6kaZiyo6kaZiyo6ka', 'is_bool': True, 'category': <Categories: category4>}
#             return redirect('home')
#
#     else:
#         form = CategoriesForm()
#     return render(request,'add_news.html',{'form':form})


                #28.02.25

def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect('home')
    else:
        form = NewsForm()
    return render(request,'add_news.html',{'form':form})