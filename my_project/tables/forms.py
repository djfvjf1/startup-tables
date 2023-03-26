from django import forms


class NameForm(forms.Form):
    author_name = forms.CharField(label='ФИО автора', max_length=100, )
    patent = forms.CharField(label='Номер патента', max_length=100)
    year = forms.CharField(label='Годы выдачи', max_length=100)
    name = forms.CharField(label='Название', max_length=100)

