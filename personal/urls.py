from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post
from . import views 
from personal.views import index

urlpatterns = [
    
	#url(r'^webapp/', include('webapp.urls')),
	url(r'^$', views.index, name='index'),
    url(r'^$', ListView.as_view(queryset=Post.objects.order_by("-date","visitor")[:],
											template_name="blog/blog2.html")),
											
	#url(r'^contact/$', views.contact, name='contact'),
]