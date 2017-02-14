from django.shortcuts import render,redirect
from django.contrib.auth import (login,logout,get_user_model,authenticate)
from .forms import Login_form,Register_view


def login_view(request):
	print(request.user.is_authenticated())
	forms=Login_form(request.POST or None)
	if forms.is_valid():
		username=forms.cleaned_data.get('username')
		password=forms.cleaned_data.get('password')
		user=authenticate(username=username,password=password)
		login(request,user)
		print(request.user.is_authenticated())
		return redirect('/home/')
	return render(request,'login_view.html',{"forms":forms})


def register_view(request):
	formss=Register_view(request.POST or None)
	if formss.is_valid():
		forms=formss.save(commit=False)
		username=formss.cleaned_data.get("username")
		password=formss.cleaned_data.get("password")
		forms.set_password(password)
		forms.save()
		new_user=authenticate(username=username,password=password)
		login(request,new_user)
		return redirect('/login/')
	return render(request, "register.html", {"formss": formss})


def logout_view(request):
	logout(request)
	return redirect('/home/')


#
# def logout_view(request):
# 	logout(request)
# 	return render(request,'regster.html',{})





