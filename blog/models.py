from django.db import models

class Post(models.Model):

	DATE_CHOICES = (
    ('2013-01-06','2013-01-06'),
    ('blue', 'BLUE'),
    
   )

	website = models.TextField(max_length=100)
	visitor = models.TextField()
	date = models.TextField()
	

	
	def __str__(self):
		return self.website
		return self.visitor
		return self.date