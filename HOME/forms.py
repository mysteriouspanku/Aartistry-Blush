
# from django import forms
# from .models import Posts

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Posts
#         fields = ['title', 'post_type', 'image']

from django import forms
from .models import Posts

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'post_type', 'platform', 'link', 'image', 'caption']
