from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='login',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=('username','password',)
#Add news.1
# class NewsForm(forms.Form):
#     title=forms.CharField(max_length=150,label='Название', ###
#                         widget=forms.TextInput(attrs={"class":"form-control"}))
#     context=forms.CharField(label='Текст',required=False,widget=forms.Textarea(attrs={
#         "class":"form-control",
#         "rows":5
#     }))
#     is_bool=forms.BooleanField(label="Opublikirovano?",initial=True)
#     category=forms.ModelChoiceField(empty_label='Viberite categoriyu', ###
#                                     label='Kategoriya',queryset=Categories.objects.all(),
#                                     widget=forms.Select(attrs={"class":"form-control"}))
#
# class CategoriesForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Category',widget=forms.TextInput(attrs={"class": "form-control"}))


    #28.02.25 pastda malumot qo'shish  Add news.2
class NewsForm(forms.ModelForm):

    class Meta:
        model=News
        fields=['title','context','is_bool','category','photos']
        #exclude =['created_ed']-shundan tashqari barchasi
        # fields='__all__'
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'context':forms.Textarea(attrs={'class':'form-control','rows':5}),
            'category':forms.Select(attrs={'class':'form-control'}),    

        }

    # def clean_title(self):
    #     title=self.cleaned_data['title']
    #     if re.sea rch(r'\d' , title):  # `re.match()` faqat string boshini tekshiradi
    #         raise ValidationError('Title raqam bulmasin')
    #     return title