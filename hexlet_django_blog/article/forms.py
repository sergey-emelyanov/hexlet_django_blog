from django import forms


class CommentArticleForm(forms.Form):
    content = forms.CharField(label='Комментарий')
