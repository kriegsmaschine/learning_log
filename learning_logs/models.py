from django.db import models

class Topic(models.Model):
	#a topic the user is learning about
	text 	   = models.CharField(max_length = 200)
	date_added = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		#return a string representation of the model
		return self.text



class Entry(models.Model):
	#This will store the specifics of something new learned
	topic 	   = models.ForeignKey(Topic)
	text 	   = models.TextField()
	date_added = models.DateTimeField(auto_now_add = True)

	#embed class Meta in Entry to handle django
	# calling "entries" vs "entrys"
	class Meta:
		verbose_name_plural = "entries"

	def __str__(self):
		#return a short string of the entry
		if(len(self.text) < 51):
			return self.text
		else:
			return self.text[:50] + "..."