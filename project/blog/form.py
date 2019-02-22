from django import forms
from . models import Blog 

class BlogPost(forms.ModelForm):
    class Meta: 
        model = Blog # Blog 모델을 기반으로 
        fields = ['title', 'body'] # title body 를 입력받겠다 입력 폼을 자동 생성 여기서 값을 입력 후 views.py로 전달