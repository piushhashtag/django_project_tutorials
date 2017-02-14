from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .forms import Form, CommentForm, ContactForm
from .models import File, Comment
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required


def homepage(request):
	return render(request, 'home.html', {})


def formfile(request):
	form = Form(request.POST or None, request.FILES or None)
	if form.is_valid():
		forms = form.save(commit=False)
		forms.save()
	return render(request, 'file.html', {'form': form})


def show(request):
	data = get_object_or_404(File, id=1)
	content = ContentType.objects.get_for_model(File)
	obj = data.id
	form = CommentForm(request.POST or None)
	if form.is_valid():
		content_data = form.cleaned_data.get("content")
		new_comment, created = Comment.objects.get_or_create(
			content_type=content,
			object_id=obj,
			content=content_data,
		)
		return redirect('/home/show/')
	comments = Comment.objects.filter(content_type=content, object_id=obj)

	return render(request, 'download.html', {'all': data, 'comment': comments, 'form': form})


def show_second(request):
	data = get_object_or_404(File, id=2)
	content = ContentType.objects.get_for_model(File)
	obj = data.id
	form = CommentForm(request.POST or None)
	if form.is_valid():
		content_data = form.cleaned_data.get("content")
		new_comment, created = Comment.objects.get_or_create(
			content_type=content,
			object_id=obj,
			content=content_data,
		)
		return HttpResponseRedirect("/home/show2/")
	comments = Comment.objects.filter(content_type=content, object_id=obj)
	return render(request, 'download1.html', {'all': data, 'comment': comments})


def show_third(request):
	data = get_object_or_404(File, id=3)
	content = ContentType.objects.get_for_model(File)
	obj = data.id
	form = CommentForm(request.POST or None)
	if form.is_valid():
		content_data = form.cleaned_data.get("content")
		new_comment, created = Comment.objects.get_or_create(
			content_type=content,
			object_id=obj,
			content=content_data,
		)
		return HttpResponseRedirect("/home/show3/")
	comments = Comment.objects.filter(content_type=content, object_id=obj)

	return render(request, 'download2.html', {'all': data, 'comment': comments})


def show_four(request):
	data = get_object_or_404(File, id=4)
	content = ContentType.objects.get_for_model(File)
	obj = data.id
	form = CommentForm(request.POST or None)
	if form.is_valid():
		content_data = form.cleaned_data.get("content")
		new_comment, created = Comment.objects.get_or_create(
			content_type=content,
			object_id=obj,
			content=content_data,
		)
		return redirect('/home/show4/')
	comments = Comment.objects.filter(content_type=content, object_id=obj)

	return render(request, 'download3.html', {'all': data, 'comment': comments, 'form': form})


def show_five(request):
	data = get_object_or_404(File, id=5)
	content = ContentType.objects.get_for_model(File)
	obj = data.id
	form = CommentForm(request.POST or None)
	if form.is_valid():
		content_data = form.cleaned_data.get("content")
		new_comment, created = Comment.objects.get_or_create(
			content_type=content,
			object_id=obj,
			content=content_data,
		)
		return redirect('/home/show5/')
	comments = Comment.objects.filter(content_type=content, object_id=obj)

	return render(request, 'download4.html', {'all': data, 'comment': comments, 'form': form})


def show_six(request):
	data = get_object_or_404(File, id=6)
	content = ContentType.objects.get_for_model(File)
	obj = data.id
	form = CommentForm(request.POST or None)
	if form.is_valid():
		content_data = form.cleaned_data.get("content")
		new_comment, created = Comment.objects.get_or_create(
			content_type=content,
			object_id=obj,
			content=content_data,
		)
		return redirect('/home/show6/')
	comments = Comment.objects.filter(content_type=content, object_id=obj)

	return render(request, 'download5.html', {'all': data, 'comment': comments, 'form': form})


def show_seven(request):
	data = get_object_or_404(File, id=7)
	content = ContentType.objects.get_for_model(File)
	obj = data.id
	form = CommentForm(request.POST or None)
	if form.is_valid():
		content_data = form.cleaned_data.get("content")
		new_comment, created = Comment.objects.get_or_create(
			content_type=content,
			object_id=obj,
			content=content_data,
		)
		return redirect('/home/show7/')
	comments = Comment.objects.filter(content_type=content, object_id=obj)

	return render(request, 'download6.html', {'all': data, 'comment': comments, 'form': form})


def show_eight(request):
	data = get_object_or_404(File, id=8)
	content = ContentType.objects.get_for_model(File)
	obj = data.id
	form = CommentForm(request.POST or None)
	if form.is_valid():
		content_data = form.cleaned_data.get("content")
		new_comment, created = Comment.objects.get_or_create(
			content_type=content,
			object_id=obj,
			content=content_data,
		)
		return redirect('/home/show8/')
	comments = Comment.objects.filter(content_type=content, object_id=obj)

	return render(request, 'download7.html', {'all': data, 'comment': comments, 'form': form})


def show_nine(request):
	data = get_object_or_404(File, id=9)
	content = ContentType.objects.get_for_model(File)
	obj = data.id
	form = CommentForm(request.POST or None)
	if form.is_valid():
		content_data = form.cleaned_data.get("content")
		new_comment, created = Comment.objects.get_or_create(
			content_type=content,
			object_id=obj,
			content=content_data,
		)
		return redirect('/home/show9/')
	comments = Comment.objects.filter(content_type=content, object_id=obj)

	return render(request, 'download8.html', {'all': data, 'comment': comments, 'form': form})


def show_ten(request):
	data = get_object_or_404(File, id=10)
	content = ContentType.objects.get_for_model(File)
	obj = data.id
	form = CommentForm(request.POST or None)
	if form.is_valid():
		content_data = form.cleaned_data.get("content")
		new_comment, created = Comment.objects.get_or_create(
			content_type=content,
			object_id=obj,
			content=content_data,
		)
		return redirect('/home/show10/')
	comments = Comment.objects.filter(content_type=content, object_id=obj)

	return render(request, 'download9.html', {'all': data, 'comment': comments, 'form': form})


def show_eleven(request):
	data = get_object_or_404(File, id=11)
	content = ContentType.objects.get_for_model(File)
	obj = data.id
	form = CommentForm(request.POST or None)
	if form.is_valid():
		content_data = form.cleaned_data.get("content")
		new_comment, created = Comment.objects.get_or_create(
			content_type=content,
			object_id=obj,
			content=content_data,
		)
		return redirect('/home/show11/')
	comments = Comment.objects.filter(content_type=content, object_id=obj)

	return render(request, 'download10.html', {'all': data, 'comment': comments, 'form': form})


def show_twelve(request):
	data = get_object_or_404(File, id=12)
	content = ContentType.objects.get_for_model(File)
	obj = data.id
	form = CommentForm(request.POST or None)
	if form.is_valid():
		content_data = form.cleaned_data.get("content")
		new_comment, created = Comment.objects.get_or_create(
			content_type=content,
			object_id=obj,
			content=content_data,
		)
		return redirect('/home/show12/')
	comments = Comment.objects.filter(content_type=content, object_id=obj)

	return render(request, 'download11.html', {'all': data, 'comment': comments, 'form': form})


def show_thirteen(request):
	data = get_object_or_404(File, id=13)
	content = ContentType.objects.get_for_model(File)
	obj = data.id
	form = CommentForm(request.POST or None)
	if form.is_valid():
		content_data = form.cleaned_data.get("content")
		new_comment, created = Comment.objects.get_or_create(
			content_type=content,
			object_id=obj,
			content=content_data,
		)
		return redirect('/home/show13/')
	comments = Comment.objects.filter(content_type=content, object_id=obj)

	return render(request, 'download12.html', {'all': data, 'comment': comments, 'form': form})


def show_fourteen(request):
	data = get_object_or_404(File, id=14)
	content = ContentType.objects.get_for_model(File)
	obj = data.id
	form = CommentForm(request.POST or None)
	if form.is_valid():
		content_data = form.cleaned_data.get("content")
		new_comment, created = Comment.objects.get_or_create(
			content_type=content,
			object_id=obj,
			content=content_data,
		)
		return redirect('/home/show14/')
	comments = Comment.objects.filter(content_type=content, object_id=obj)

	return render(request, 'download13.html', {'all': data, 'comment': comments, 'form': form})


def show_fifteen(request):
	data = get_object_or_404(File, id=15)
	content = ContentType.objects.get_for_model(File)
	obj = data.id
	form = CommentForm(request.POST or None)
	if form.is_valid():
		content_data = form.cleaned_data.get("content")
		new_comment, created = Comment.objects.get_or_create(
			content_type=content,
			object_id=obj,
			content=content_data,
		)
		return redirect('/home/show15/')
	comments = Comment.objects.filter(content_type=content, object_id=obj)

	return render(request, 'download14.html', {'all': data, 'comment': comments, 'form': form})


def show_sixteen(request):
	data = get_object_or_404(File, id=16)
	content = ContentType.objects.get_for_model(File)
	obj = data.id
	form = CommentForm(request.POST or None)
	if form.is_valid():
		content_data = form.cleaned_data.get("content")
		new_comment, created = Comment.objects.get_or_create(
			content_type=content,
			object_id=obj,
			content=content_data,
		)
		return redirect('/home/show16/')
	comments = Comment.objects.filter(content_type=content, object_id=obj)

	return render(request, 'download15.html', {'all': data, 'comment': comments, 'form': form})


@login_required(login_url='/login/')
def project(request):
	return render(request, 'project.html', )


def profile(request):
	return render(request, 'profile.html', )



def contactform(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		forms = form.save(commit=False)
		forms.save()
		return redirect("base:homepage")
	return render(request, 'contact.html', {'form': form})
