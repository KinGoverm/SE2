#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#encoding:UTF-8
from django import forms
from django.utils.translation import ugettext as _
from django.core.validators import validate_email
from django.contrib.auth.forms import AuthenticationForm

from django.forms.fields import MultipleChoiceField
from django.forms.widgets import CheckboxSelectMultiple
from django.forms import ModelForm


    


class LoginForm(forms.Form):
    #errors ="user with this password and username dosen't exist"
    errors =""
    username = forms.CharField(
        label = _('User Name'), 
        min_length = 2, 
        max_length = 30,
        widget = forms.TextInput(attrs={
            'placeholder':_('username'),
            'class': 'span6 required',
            'required': '',
        })
    )
    password = forms.CharField(
        label = _('Password'),
        min_length = 6,
        max_length = 30,
        widget = forms.PasswordInput(attrs={
            'placeholder':_('Password'),
            'class': 'span6 required',
            'required': '',
        })
    )

    set_username=''
    set_password=''





