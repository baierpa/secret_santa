from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Members

class MembersCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Members
        fields = ('username',)

class MembersChangeForm(UserChangeForm):

    class Meta:
        model = Members
        fields = ('username',)