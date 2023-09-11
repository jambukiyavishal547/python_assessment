from django.db import models

# Create your models here.
class Comment(models.Model):
	postId=models.PositiveIntegerField()
	name=models.CharField(max_length=30,blank=True)
	email=models.EmailField()
	body=models.TextField()

	def __str__(self):
		return self.name