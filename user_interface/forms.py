from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import (User,user1,usereg,meeting,admin1,org)

class user1_form(ModelForm):
    class Meta:
        model = user1
        fields= "__all__"

class usereg_form(ModelForm):
    class Meta:
        model = usereg
        fields= "__all__"

class meeting_form(ModelForm):
    class Meta:
        model = meeting
        fields= "__all__"

class admin1_form(ModelForm):
    class Meta:
        model = admin1
        fields= "__all__"

class org_form(ModelForm):
    class Meta:
        model = org
        fields= "__all__"

    
