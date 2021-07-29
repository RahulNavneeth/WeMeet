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
    path('update/<int:userid>/<str:userurl>',views.updatepage),
    path('ajax/msg/<str:schoolname>/<str:batchurl>',views.batchMsg),
    path('ajax/showmsg/<str:schoolname>/<str:batchurl>',views.msgView),

    path('passwordreset/<str:code>/<int:user>',views.passreset),
    # path('mailTest',views.mailTest),
    path('mailTest/acc',views.mailacc,name='mailacc'),
    path('mailTest/code',views.submitCode,name='submitCode'),
    path('mailTemplate',views.mailTest),
    path('u/school/<str:schoolname>',views.schoolUser),
    path('school/<str:schoolname>/batch/<str:batchurl>',views.batchView),
    path('student/<str:studenturl>',views.studentView),
    path('admin/data/school/<int:schoolId>/batch/<int:batchId>',views.adminDataBatch),
    path('admin/data/school/<int:schoolId>',views.adminDataSchool),
    path('admin/data/school',views.adminDataAllSchool),
    path('u/student/<str:studentname>',views.studentUser),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
