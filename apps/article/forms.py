#_*_ encoding: utf-8 _*_
__author__ = "Administrator"
__date__ = "2018/2/5 , 20:32"
from django.contrib.auth.forms import forms
class CommentForm(forms.Form):
    nickname = forms.CharField(required=True,max_length=10,min_length=2)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True,max_length=500)

class SearchForm(forms.Form):
    keyword = forms.CharField(required=True,max_length=30)

class StudySearchForm(forms.Form):
    keyword = forms.CharField(required=True,max_length=30)

class RssSearchForm(forms.Form):
    keyword = forms.CharField(required=True, max_length=30)