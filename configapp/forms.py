import re
from django import forms
from django.core.exceptions import ValidationError
from django.template.defaultfilters import title
from .models import Categories,News

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
        #fields='__all__'
        fields=['title','context','is_bool','category']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'context':forms.Textarea(attrs={'class':'form-control','rows':5}),
            'category':forms.Select(attrs={'class':'form-control'}),
        }

    # def clean_title(self):
    #     title=self.cleaned_data['title']
    #     if re.match(r'\d' , title):
    #         raise ValidationError('Title raqam bulmasin')
    #     return title