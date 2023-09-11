from django.urls import path
from .import views
urlpatterns = [


    path('',views.index,name='index'),
    path('doctor/',views.doctor,name='doctor'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('appointment/',views.appointment,name='appointment'),
    path('treatment/',views.treatment,name='treatment'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('singup/',views.singup,name='singup'),
    path('change-password/',views.change_password,name='change-password'),
    path('profile/',views.profile,name='profile'),



    path('my-appointment/',views.my_appointment,name='my-appointment'),
    path('remove-from-appointment/',views.remove_from_appointment,name='remove-from-appointment'),
    path('doctore-singup/',views.doctore_singup,name='doctore-singup'),
    path('doctor-index/',views.doctor_index,name='doctor-index'),
]