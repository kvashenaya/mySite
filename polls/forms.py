from django import forms
class UserForm(forms.Form):
    Назва_категорії = forms.CharField(max_length=100)
    Новий_кандидат_1= forms.CharField(max_length=100)
    Новий_кандидат_2= forms.CharField(max_length=100)
    Новий_кандидат_3= forms.CharField(max_length=100)
    Новий_кандидат_4= forms.CharField(max_length=100)
    Новий_кандидат_5= forms.CharField(max_length=100)
    
