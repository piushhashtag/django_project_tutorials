from django import forms
from django.contrib.auth import get_user_model,authenticate

user=get_user_model()
class Login_form(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput)

	def clean(self,*args,**kwargs):
		username=self.cleaned_data.get("username")
		password=self.cleaned_data.get("password")
		user=authenticate(username=username,password=password)
		if not user:
			raise forms.ValidationError("This User Not Exist")
		return super(Login_form,self).clean(*args,**kwargs)



class Register_view(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	email=forms.EmailField(label="Email address")
	email2=forms.EmailField(label="Confirm Email")
	class Meta:
		model=user
		fields=['username','email','email2','password']
	def clean_email2(self):
		email=self.cleaned_data.get("email")
		email2=self.cleaned_data.get("email2")
		if email != email2:
			raise forms.ValidationError("Email Must Match")
		email_qs=user.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("Email With This Name Is Already Exists")
		return super(Register_view,self)




