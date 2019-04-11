from django.db import models
from django import forms

class Data(models.Model):
    username_date = models.CharField(max_length=255)
    data = models.ImageField(upload_to="files/usr/data",blank=True,)

class DataModelForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['data'] # 'username_date', 
        labels = { # 'username_date': '유저이름과 업로드 날짜',
                    'data':'이미지'
        }
