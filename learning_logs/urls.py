"""Define URL patterns in learning_logs"""

from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'learning_logs'
urlpatterns = [
	#Home page
	url(r"^$", views.index, name = "index"),

	#display topic and topic entries
	url(r"^topics/$", views.topics, name = "topics"),
	url(r"^topics/(?P<topic_id>\d+)/$", views.topic, name = "topic"),

	#forms
	url(r'^new_topic/$', views.new_topic, name = 'new_topic'),
	url(r'^new_entry/(?P<topic_id>\d+)$', views.new_entry, name = 'new_entry'),
	url(r'^edit_entry/(?P<entry_id>\d+)$', views.edit_entry, name = 'edit_entry'),
]