# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 23:09:26
# @Author  : handong
# @FileName: forms.py
# @Software: PyCharm

from django import forms
from.models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}