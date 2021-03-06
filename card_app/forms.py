from django import forms 
from .models import CardComment, CardReComment


class CardSearchForm(forms.Form):
    word = forms.CharField(label='ワード',required=False, widget=forms.TextInput(attrs={'placeholder':'キーワードを検索', 'class':'form-control'}))

    def clean_name(self):
        word = self.cleaned_data['word']
        return word

class CardCommentForm(forms.ModelForm):
    class Meta:
        model = CardComment
        fields = ('name', 'text', 'thumnail')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
            }),
            'text': forms.Textarea(attrs={
                'class': "form-control",
            }),
            'thumnail': forms.ClearableFileInput(attrs={
                'class': "form-control-file",
            }),
        }


class CardReCommentForm(forms.ModelForm):
    class Meta:
        model = CardReComment
        fields = ('name', 'text', 'thumnail')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
            }),
            'text': forms.Textarea(attrs={
                'class': "form-control",
            }),
            'thumnail': forms.ClearableFileInput(attrs={
                'class': "form-control-file",
            }),
        }


