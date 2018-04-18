from django import forms
from livestream.models import chat
from django.utils import timezone

class chat(forms.ModelForm):
    username = forms.CharField(widget=forms.HiddenInput(),initial="user")
    content = forms.CharField(max_length=128,required=True)
    # time = forms.DateTimeField()
    time = forms.DateTimeField(widget=forms.HiddenInput(),required=False)
    class Meta:
        model = chat
        fields = ('username','content','time')


