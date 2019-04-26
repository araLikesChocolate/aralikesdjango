from django.db import models
from django import forms
from django.utils import timezone
import os
from uuid import uuid4 # universally unique identifiers : 타임스템프를 기준으로 고유한 번호 지정
import jsonfield
from login.models import Member

#파라미터 instance는 Data 모델을 의미 filename은 업로드 된 파일의 파일 이름
def user_path(instance, filename): 
    extension = filename.split('.')[-1]
    aa = str(timezone.now())
    bb = aa.split('.')[0]
    print(type(bb))
    return '%s/%s.%s' % (instance.member_idx.id, bb, extension) # 예 : wayhome/abcdefgs.png

class Data(models.Model):
    idx = models.AutoField(primary_key=True, null=False)
    url = models.ImageField(blank=True, upload_to=user_path)
    # url = models.ImageField(upload_to=user_path,
    #                         null=False,
    #                         verbose_name=('imgs'),
    #                         blank=False,)
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
        # fields = '__all__'
        fields = ['url','publish']
        labels = {  'url':'이미지',
                    'publish':'공유여부',
                }