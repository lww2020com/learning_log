from django import forms
from .models import Entry, Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['text']
        labels={'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields='__all__'
        labels={'text':''}
        # 修改渲染表单的属性
        widgets={'text':forms.Textarea(attrs={'cols':80}),'topic':forms.Select(attrs={'disabled':True})}