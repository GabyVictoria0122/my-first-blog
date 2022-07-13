from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        # qual modelo deverá ser usado para criar este formulário
        model = Post
        # quais campos devem entrar no nosso formulário
        fields = ('title', 'text',)