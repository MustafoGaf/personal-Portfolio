from django import forms
from .models import Comment, Blog


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
 
    to = forms.EmailField()
    comment = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields = ['name', 'email', 'body']
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'text' ,"date","author",  'tags']


