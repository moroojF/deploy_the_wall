from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.wall),
    path('/createMsg', views.createMsg),
    path('/createComment', views.createComment),
    path('/delete/message/<int:msgID>', views.delete_msg),
    path('/delete/comment/<int:commentID>', views.delete_comment),
    
]
