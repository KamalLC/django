from django import forms
from .models import Blog
#using 1st method forms.Form (Normal form like contact form)
class BlogForm(forms.Form):
    title = forms.CharField(max_length=100)
    subtitle = forms.CharField(max_length=100)
    image = forms.ImageField()
    #btntext = forms.CharField(max_length=100)
    paragraph = forms.CharField(widget=forms.Textarea)



#using 2nd method forms.ModelForm (Database related operations)
class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'subtitle', 'paragraph','image']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'subtitle': forms.TextInput(attrs={'class':'form-control'}),
            'paragraph': forms.Textarea(attrs={'class': 'form-control','id':'paragraph'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
        }
        # labels = {
        #     'title': 'Blog Title',
        #     'subtitle': 'Blog Subtitle',
        #     'paragraph': 'Blog Paragraph',
        #     'image': 'Blog Image',
        # }