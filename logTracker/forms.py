from django.forms import ModelForm
from django import forms
from .models import Member, CheckInMembers


class CreateUserForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'


class LogInForm(ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'serial_number']


class EditMemberForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'


class CheckInForm(forms.Form):
    serial_number = forms.CharField(max_length=6)
