# from django.db.models.fields import TextField
# from django.forms import ModelForm, TextInput, NumberInput, Select, forms
# from django.forms.widgets import Textarea
# from .models import Item

# class ItemForm(ModelForm):
#     class Meta:
#         model=Item
#         fields='__all__'
#         widgets = {
#             'alphaval': TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'alpha value'
#                 }),

#                 'integerval': NumberInput(
#                 attrs={
#                     'class': 'form-control'
#                 }),

#                 'alphanumval': TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'alphanum value'
#                 }),
#         }