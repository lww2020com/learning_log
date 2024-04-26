from typing import Any
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
        exclude={'topic'}
        # 修改渲染表单的属性
        widgets={'text':forms.Textarea(attrs={'cols':80}),
                 'topic':forms.Select(attrs={'readonly':True})}
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     var = self.fields['topic']
    #     var.disabled = True
