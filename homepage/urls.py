from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.homepage, name='homepage'),
	url(r'^files/$', views.formfile, name='files'),
	url(r'^show/$', views.show, name='home1'),
	url(r'^show2/$', views.show_second, name='home2'),
	url(r'^show3/$', views.show_third, name='home3'),
	url(r'^show4/$', views.show_four, name='home4'),
	url(r'^show5/$', views.show_five, name='home5'),
	url(r'^show6/$', views.show_six, name='home6'),
	url(r'^show7/$', views.show_seven, name='home7'),
	url(r'^show8/$', views.show_eight, name='home8'),
	url(r'^show9/$', views.show_nine, name='home9'),
	url(r'^show10/$', views.show_ten, name='home10'),
	url(r'^show11/$', views.show_eleven, name='home11'),
	url(r'^show12/$', views.show_twelve, name='home12'),
	url(r'^show13/$', views.show_thirteen, name='home13'),
	url(r'^show14/$', views.show_fourteen, name='home14'),
	url(r'^show15/$', views.show_fifteen, name='home15'),
	url(r'^show16/$', views.show_sixteen, name='home16'),
	url(r'^project/$', views.project, name='project'),
	url(r'^contact/$', views.contactform, name='contact'),
	url(r'^profile/$', views.profile, name='profile'),
	# url(r'^comment_form/$', views.formss, name='commentform'),

]
