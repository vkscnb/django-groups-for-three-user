from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'login/',views.user_login),
    url(r'create_and_list_of_teacher',views.create_and_list_of_teacher),
    url(r'details_of_teacher/(?P<teacher_id>[0-9]+)/$', views.details_of_teacher),
    url(r'create_and_list_of_student', views.create_and_list_of_student),
    url(r'details_of_student/(?P<student_id>[0-9]+)/$',views.details_of_student)
]