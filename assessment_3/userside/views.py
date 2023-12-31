from django.shortcuts import render,redirect
from .models import *
# Create your views here.

#===============================================================================================
#===============================================================================================

#user side

def index(request):
	return render(request,'index.html')

def doctor(request):
	return render(request,'doctor.html')

def about(request):
	return render(request,'about.html')

def treatment(request):
	return render(request,'treatment.html')


def contact(request):
    if request.method=='POST':
        Contect.objects.create(
	        name = request.POST['name'],
	        email = request.POST['email'],
	        mobile = request.POST['mobile'],
	        message = request.POST['message'],
        )
        msg = 'Message send Successfully'
        return render(request,'contact.html',{'msg':msg})
    else:
        return render(request,'contact.html')


def appointment(request):
	try:
		if request.session['email']:
			if request.method=="POST":
				try:
					Appointment.objects.get(pname=request.POST['pname'])
					msg="Appointment Alredy Exist"
					return render(request,'appointment.html',{'msg':msg})
				except:
					Appointment.objects.create(
								pname=request.POST['pname'],
								dname=request.POST['dname'],
								mobile=request.POST['mobile'],
								date=request.POST['date']
						)
					msg="Appointment Posted"
					return render(request,'index.html',{'msg':msg})
			else:
				return render(request,'appointment.html')
		else:
			return render(request,'login.html')
	except:
		pass
		msg="please Login First"
		return render(request,'login.html')


def logout(request):
	try:
		try:
			del request.session['email']
			del request.session['fname']
			del request.session['profile_pic']
			return redirect('index')
		except:
			del request.session['name']
			del request.session['doc_email']
			return redirect('index')
	except Exception as e :
		print(e)
		return redirect('index')

def login(request):
	if request.method=="POST":
		try:
			try:
				user=User.objects.get(email=request.POST['email'])
				if user.password==request.POST['password']:
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['profile_pic']=user.profile_pic.url
					return render(request,'index.html')
				else:
					msg="Incorrect Password"
					return render(request,'login.html',{'msg':msg})
			except Exception as e:
				print(e)
				doctors = Doctor.objects.get(email = request.POST['email'])
				if doctors.password == request.POST['password']:
					request.session['doc_email']=doctors.email
					request.session['name']=doctors.name
					return render(request,'doctor-index.html')
				else:
					msg = 'Password & Confirm Password Does Not Match'
					return render(request,'login.html',{'msg':msg})
		except Exception as e:
			print(e)
			msg="Email Not Registered"
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'login.html')

def singup(request):
	if request.method=="POST":
		try:
			User.objects.get(email=request.POST['email'])
			msg="Email Alredy Exist"
			return render(request,'singup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					mobile=request.POST['mobile'],
					gender=request.POST['gender'],
					address=request.POST['address'],
					email=request.POST['email'],
					password=request.POST['password'],
					profile_pic=request.FILES['profile_pic']
					)
				msg="Sing Up Successfully"
				return render(request,'login.html',{'msg':msg})
			else:
				msg="Password Not Match"
				return render(request,'singup.html',{'msg':msg})
	else:
		return render(request,'singup.html')

def change_password(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])
		if user.password==request.POST['old-password']:
			if request.POST['new-password']==request.POST['c-password']:
				user.password=request.POST['new-password']
				user.save()
				return redirect('logout')
			else:
				msg="New Password Not Match"
				return render(request,'change-password.html',{'msg':msg})
		else:
			msg="Old Password Not Match"
			return render(request,'change-password.html',{'msg':msg})
	else:
		return render(request,'change-password.html')

def profile(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.email=request.POST['email']
		user.mobile=request.POST['mobile']
		user.address=request.POST['address']
		try:
			user.profile_pic=request.FILES['profile_pic']
		except:
			pass
		user.save()
		request.session['profile_pic']=user.profile_pic.url
		msg="profile Updated successfully"
		return render(request,'profile.html',{'user':user,'msg':msg})
	else:
		return render(request,'profile.html',{'user':user})



#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

# Docture Side

def doctor_index(request):
	return render(request,'doctor-index.html')

def remove_from_appointment(request):
	return redirect('my-appointment')

def my_appointment(request):
	try:
		doctors=Doctor.objects.get(email=request.session['doc_email'])
		appointments=Appointment.objects.all()
		return render(request,'my-appointment.html',{'appointments':appointments})
	except Exception as e:
		print(e)
		pass
		return render(request,'login.html')

def doctore_singup(request):
	if request.method=="POST":
		try:
			Doctor.objects.get(email=request.POST['email'])
			msg="Email Alredy Exist"
			return render(request,'doctore-singup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				Doctor.objects.create(
					name=request.POST['name'],
					degree=request.POST['degree'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					gender=request.POST['gender'],
					password=request.POST['password']
					)
				msg="Sing Up Successfully"
				return render(request,'login.html',{'msg':msg})
			else:
				msg="Password Not Match"
				return render(request,'doctore-singup.html',{'msg':msg})
	else:
		return render(request,'doctore-singup.html')