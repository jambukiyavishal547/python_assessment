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

	def __str__(self) -> str:
		return self.fname+ "  "+self.lname

class Doctor(models.Model):
	name=models.CharField(max_length=100)
	degree=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	gender=models.CharField(max_length=10)
	password=models.CharField(max_length=15)
	

	def __str__(self) -> str:
		return self.name +" "+self.degree


class Appointment(models.Model):
	pname=models.CharField(max_length=40)
	dname=models.CharField(max_length=50,default="")
	mobile=models.PositiveIntegerField()
	date=models.CharField(max_length=100)

	def __str__(self) -> str:
		return self.pname +" "+self.dname


class Contect(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	message=models.TextField()

	def __str__(self) -> str:
		return self.name