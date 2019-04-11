from django import forms
from .models import Data

#book 입력, 수정, html에서 사용하기 위해

def min_length3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError("3글자 이상입니다.")

# 일반 FORM
class DataForm(forms.Form):
    username_date = forms.CharField(label="forms 제목")
    # data = models.ImageField(upload_to="files/usr/data",blank=True,)

    def save2(self, commit=True):
        data = Data(**self.cleaned_data) #{'title':'', 'author':'',....}
        if commit:
            data.save()
        return data