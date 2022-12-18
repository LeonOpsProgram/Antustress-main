from .models import Test
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Select, CharField, ModelChoiceField, \
    MultipleChoiceField, CheckboxSelectMultiple, Form


class TestForm(ModelForm):
    class Meta:
        model = Test

        fields = ['title', 'anons', 'ans1', 'pr1', 'ans2', 'pr2', 'ans3', 'pr3']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название вопроса'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вопрос'
            }),
            'ans1': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вариант ответа 1'
            }),
            'pr1': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена ответа в баллах'
            }),
            'ans2': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вариант ответа 2'
            }),
            'pr2': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена ответа в баллах'
            }),
            'ans3': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вариант ответа 3'
            }),
            'pr3': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена ответа в баллах'
            })
        }


class Testans(Form):
    model = Test
    fields = ['ans1', 'ans2']
    test = Test.objects.order_by('id')
    widgets = {
        'ans1': Select(choices=((test[0].ans1, test[0].ans1), (test[0].ans2, test[0].ans2), (test[0].ans3, test[0].ans3)),
                       attrs={
                           'class': 'form-control',
                       }),
        'ans2': Select(choices=((test[1].ans1, test[1].ans1), (test[1].ans2, test[1].ans2), (test[1].ans3, test[1].ans3)),
                       attrs={
                           'class': 'form-control',
                       }),
        # 'ans3': Select(choices=((test.ans1, test.ans1), (test.ans2, test.ans2), (test.ans3, test.ans3)),
        #                attrs={
        #                    'class': 'form-control',
        #                }),
        # 'ans4': Select(choices=((test.ans1, test.ans1), (test.ans2, test.ans2), (test.ans3, test.ans3)),
        #                attrs={
        #                    'class': 'form-control',
        #                }),
        # 'ans5': Select(choices=((test.ans1, test.ans1), (test.ans2, test.ans2), (test.ans3, test.ans3)),
        #                attrs={
        #                    'class': 'form-control',
        #                }),
        # 'ans6': Select(choices=((test.ans1, test.ans1), (test.ans2, test.ans2), (test.ans3, test.ans3)),
        #                attrs={
        #                    'class': 'form-control',
        #                }),
        # 'ans7': Select(choices=((test.ans1, test.ans1), (test.ans2, test.ans2), (test.ans3, test.ans3)),
        #                attrs={
        #                    'class': 'form-control',
        #                }),
        # 'ans8': Select(choices=((test.ans1, test.ans1), (test.ans2, test.ans2), (test.ans3, test.ans3)),
        #                attrs={
        #                    'class': 'form-control',
        #                }),
        # 'ans9': Select(
        #     choices=((test[9].ans1, test[9].ans1), (test[9].ans2, test[9].ans2), (test[9].ans3, test[9].ans3)),
        #     attrs={
        #         'class': 'form-control',
        #     }),
        # 'ans10': Select(
        #     choices=((test[10].ans1, test[10].ans1), (test[10].ans2, test[10].ans2), (test[10].ans3, test[10].ans3)),
        #     attrs={
        #         'class': 'form-control',
        #     }),
    }

# from django import forms
#
#
#
# class GeeksForm(forms.Form):
#     def __init__(self):
#         model
#         geeks_field = forms.MultipleChoiceField(choices=DEMO_CHOICES)
