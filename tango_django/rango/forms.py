from django import forms
from rango.models import page,Category

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=128, label="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        model = Category
        fields = ('name','views','likes')

class PageForm(forms.Form):
    title = forms.CharField(max_length=128, label="Please enter the title of the page.")
    url = forms.URLField(max_length=200, label="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        model = page
        fields = ('title', 'url', 'views')
    

