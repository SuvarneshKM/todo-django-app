from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^$', views.home, name='home'),
  		path('add_todo/', views.add_todo),
  		path('delete_todo/<int:todo_id>/', views.delete_todo),
				]           
