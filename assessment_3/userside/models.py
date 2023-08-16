from django.db import models

# Create your models here.
class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	mobile=models.PositiveIntegerField()
	gender=models.CharField(max_length=10)
	address=models.TextField()
	email=models.EmailField()
	password=models.CharField(max_length=20)
	profile_pic=models.ImageField(upload_to="profile_pic/",default="")

	def __str__(self):
		return self.fname+ "  "+self.lname

class Appointment(models.Model):
	pname=models.CharField(max_length=40)
	dname=models.CharField(max_length=50,default="")
	mobile=models.PositiveIntegerField()
	date=models.CharField(max_length=100)

	def __str__(self):
		return self.pname +" "+self.dname