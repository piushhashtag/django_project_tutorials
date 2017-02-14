from django import forms
from .models import File,Contact


class Form(forms.ModelForm):
	class Meta:
		model = File
		fields = ['file']


class CommentForm(forms.Form):
	# content_type=forms.CharField(widget=forms.HiddenInput)
	# object_id = forms.CharField(widget=forms.HiddenInput)
	# parent_id = forms.IntegerField(widget=forms.HiddenInput)
	content = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
	class Meta:
		model=Contact
		fields=['name','email','Subject','message']