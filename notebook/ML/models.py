from django.db import models
from django import forms
import os
from uuid import uuid4 # universally unique identifiers : 타임스템프를 기준으로 고유한 번호 지정
import jsonfield
from login.models import Member

class Data(models.Model):
    idx = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255, null=False, blank=False)
    texts = jsonfield.JSONField()
    date = models.DateTimeField(auto_now_add = True)
    publish = models.BooleanField(default=False)
    member_idx = models.ForeignKey(Member, db_column='member_idx', on_delete=models.CASCADE)
    model = models.CharField(max_length=255, null=False, blank=False)
    
    class Meta:
        db_table = u'data'
        # fields = ['idx', 'image_path', 'texts', 'date', 'publish']

    def __str__(self) :
        return 'idx: {}, url: {}, texts: {}, date: {}, publish: {}, member_idx: {}'.format(type(self.idx), type(self.url), type(self.texts), type(self.date), type(self.publish), type(self.member_idx))

# django.utils.timezone
class DataModelForm(forms.ModelForm):
    class Meta: 
        model = Data
        fields = ['url', ] # 'username_date', 
        labels = { # 'username_date': '유저이름과 업로드 날짜',
                    'url':'이미지'
        }