"""views.py in learning_logs app"""
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
	#the home page for the learning_logs app
	return render(request, "learning_logs\\index.html")

#page to display available topics in the database
def topics(request):
	"""Show all topics"""
	topics  = Topic.objects.order_by("date_added")
	context = {"topics_out":topics}
	return render(request, "learning_logs\\topics.html", context)

#page to display the detailed entries of a specific topic
def topic(request, topic_id):
	"""show all entries for a given topic"""
	topic   = Topic.objects.get(id = topic_id)
	entries = topic.entry_set.order_by("-date_added")
	context = {"topic" : topic, "entries" : entries}
	return render(request, "learning_logs\\topic.html", context)


""" forms """


def new_topic(request):
	#add new topic
	if request.method != 'POST':
		#No data submitted; creat a blank form
		form = TopicForm()
	else:
		#POST data submitted; process data in form
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))

	context = {'form':form}
	return render(request, 'learning_logs\\new_topic.html', context)

def new_entry(request, topic_id):
	#Add a new entry for a particular topic.
	topic = Topic.objects.get(id = topic_id)

	if request.method != 'POST':
		#No data submitted; create a blank form
		form = EntryForm()
	else:
		#POST data submitted; process data
		form = EntryForm(request.POST)
		if form.is_valid():
			new_entry 		= form.save(commit = False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args = [topic_id]))

	context = {'topic':topic, 'form':form}
	return render(request, 'learning_logs\\new_entry.html', context)

def edit_entry(request, entry_id):
	entry = Entry.objects.get(id = entry_id)
	topic = entry.topic

	if request.method != 'POST':
		#Initial request; pre-fill form with the current entry
		form = EntryForm(instance = entry)
	else:
		#POST data submitted; process data
		form = EntryForm(instance = entry, data = request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args = [topic.id]))
	
	context = {'entry':entry, 'topic':topic, 'form':form}
	return render(request, "learning_logs\\edit_entry.html", context)
