from django.db import models
from django import forms
from django.utils import timezone
import os
from uuid import uuid4 # universally unique identifiers : 타임스템프를 기준으로 고유한 번호 지정
import jsonfield
from login.models import Member

def get_file_path(instance, filename):
    upload_to = 'img'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.member_idx, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        pass

    # return the whole path to the file
    return os.path.join(upload_to, filename)

class Data(models.Model):
    idx = models.AutoField(primary_key=True, null=False)
    url = models.ImageField(upload_to=get_file_path,
                            null=False,
                            verbose_name=('imgs'),
                            blank=False,)
    texts = jsonfield.JSONField()
    date = models.DateTimeField(auto_now_add = True)
    publish = models.BooleanField(default=False)
    member_idx = models.ForeignKey(Member, db_column='member_idx', on_delete=models.CASCADE)

    class Meta:
        db_table = u'data'

# django.utils.timezone
class DataModelForm(forms.ModelForm):
    class Meta: 
        model = Data
        fields = ['url', ] # 'username_date', 
        labels = { # 'username_date': '유저이름과 업로드 날짜',
                    'url':'이미지'
        }