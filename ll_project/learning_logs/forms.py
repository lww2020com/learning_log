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
        # exclude={'topic'}
        # 修改渲染表单的属性
        widgets={'text':forms.Textarea(attrs={'cols':80}),
                 'topic':forms.Select(attrs={'disabled':True})}
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     var = self.fields['topic']
    #     var.disabled = True
    # def __init__(self, *args, **kwargs):
    #     super(EntryForm, self).__init__(*args, **kwargs)
    #     self.fields['topic'].disabled = True

    def clean(self):
        
        # 在模板中有表单元素用到disable属性时,post时会被django忽略该元素,在views中执行form_isvild()
        # 时会返回False数据验证失败，并会把错误写到继承的form类的errors字典属性中,表单页面会提示【这个字段为必填字段】
        # 重写clean()方法把该字段的错误从errors字典中删除
        cleaned_data = super().clean()
        # 移除my_field字段的验证错误信息
        if 'topic' in self._errors:
            del self._errors['topic']
        return cleaned_data
