from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('doctor/',views.doctor,name='doctor'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('treatment/',views.treatment,name='treatment'),
    path('login/',views.login,name='login'),
    path('singup/',views.singup,name='singup'),
]