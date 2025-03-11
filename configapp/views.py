from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect,get_object_or_404
from django.middleware.csrf import get_token
from configapp.forms import NewsForm, Categories, UserLoginForm
from configapp.models import *

def news_search(request):
    query = request.GET.get('q', '').strip()  # Bo‘sh joylarni
    news_item = News.objects.filter(title__iexact=query).first()  # Katta-kichik harf ajratmasdan qidirish

    if query:
        try:
            news_item = News.objects.filter(title__iexact=query).first()        # Aniq sarlavha bo‘yicha qidirish
        except News.DoesNotExist:
            news_item = None

    return render(request, 'index.html', {'news_item': news_item, 'query': query})

def loginPage(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')

    else:
        form=UserLoginForm()
    return render(request,'login.html',{'form':form})

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



                #28.02.25

def add_news(request):
    # print("token = = ",get_token(request)) token tutib olish
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect('home')
    else:
        form = NewsForm()
    return render(request,'add_news.html',{'form':form})

def new_about(request,new_id):
    new=get_object_or_404(News,pk=new_id)
    context={
        'new':new,
    }
    return render(request,'new_about.html',context=context)


def update_news(request,new_id):
    new=get_object_or_404(News, id=new_id)
    if request.method == "POST":
        form = NewsForm(request.POST,instance=new)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm(instance=new)

    return render(request,'update_new.html',{'form':form,"new":new})

def delete_new(request,new_id):
    new=get_object_or_404(News, id=new_id)
    if request.method == "POST":
        new.delete()
        return redirect('home')
    return redirect('home')


    # def new_about(request,category_id):
#     new=News.objects.get(pk=category_id)
#     context={
#         'news':new,
#     }
#     return render(request,'new_about.html',context=context)

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



