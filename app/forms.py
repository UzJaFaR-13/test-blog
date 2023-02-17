from django import forms
from .models import Blog, Comment


class BlogAddForms(forms.ModelForm):
    tags = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'please enter Tags'}
    ))

    class Meta:
        model = Blog
        fields = [
            'title',
            'image',
            'text',
            'category'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Sarlavha"}),
            'image': forms.FileInput(attrs={'class': "form-control"}),
            'text': forms.Textarea(attrs={'class': "form-control", 'placeholder': "Izoh qildiring"}),
            # 'category': forms.CheckboxSelectMultiple(attrs={'class': "form-control"}),
        }


class BlogUpdateForms(forms.ModelForm):

    class Meta:
        model = Blog
        fields = [
            'title',
            'text',
            'category'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Sarlavha Yangilash"}),
            'text': forms.Textarea(attrs={'class': "form-control", 'placeholder': "Izoh qildiring Yangilash"}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
