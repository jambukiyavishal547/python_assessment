from django.contrib import admin
from django.urls import path
from myapp.views import CommentList,CommentDetail

urlpatterns = [
    path('api/comments',CommentList.as_view()),
    path('api/comments/<int:pk>/',CommentDetail.as_view()),
    path('admin/', admin.site.urls),
]
