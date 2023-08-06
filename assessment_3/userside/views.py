from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'index.html')

def doctor(request):
	return render(request,'doctor.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')

def testimonial(request):
	return render(request,'testimonial.html')

def treatment(request):
	return render(request,'treatment.html')

def login(request):
	return render(request,'login.html')

def singup(request):
	return render(request,'singup.html')