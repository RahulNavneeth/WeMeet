from django.contrib import admin
from django.urls import path
from WeMeet import views
from django.conf import settings
from django.conf.urls.static import static
from WeMeet.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage),
    path('register/school', views.register_school_page,name='registerSchool'),
    path('register/student', views.register_student_page,name='registerStudent'),
    path('login',views.loginPage,name='login'),
    path('404',views.NotFoundPage404),
    path('logout',views.logoutUser,name='logout'),
    path('school/<str:schoolname>',views.schoolUser),
    path('school/<str:schoolname>/batch/<str:batchurl>',views.batchView),
    path('admin/data/school/<int:schoolId>/batch/<int:batchId>',views.adminDataBatch),
    path('admin/data/school/<int:schoolId>',views.adminDataSchool),
    path('admin/data/school',views.adminDataAllSchool),
    path('student/<str:studentname>',views.studentUser),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
