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
    path('DnD',views.DragNDrop),
    path('addBatch/<str:schoolname>',views.addBatch),
    path('add/post/<str:user>',views.addPost),
    path('logout',views.logoutUser,name='logout'),
    path('update/<int:userid>/<str:userurl>',views.updatepage),
    path('ajax/msg/<str:schoolname>/<str:batchurl>',views.batchMsg),
    path('ajax/displaypostStd',views.displayPostStd),
    path('ajax/showmsg/<str:schoolname>/<str:batchurl>',views.msgView),
    path('ajax/updatemsg/<str:schoolName>/<str:batchurl>/<str:user>/<int:msgid>',views.updatchat),
    path('ajax/deletemsg/<str:schoolName>/<str:batchurl>/<str:user>/<int:msgid>',views.deletechat),
    # path('ajax/taguserchat',views.tagUserChat),
    path('batchupdate/<str:schoolname>/<str:batchurl>',views.batchUpdate),
    path('passwordreset/<str:code>/<int:user>',views.passreset),
    # path('mailTest',views.mailTest),
    path('mailTest/acc',views.mailacc,name='mailacc'),
    path('mailTest/code',views.submitCode,name='submitCode'),
    path('mailTemplate',views.mailTest),
    path('u/school/<str:schoolname>',views.schoolUser),
    path('school/<str:schoolname>/batch/<str:batchurl>',views.batchView),
    path('student/<str:studenturl>',views.studentView),
    path('admin/data/school/<int:schoolId>/batch/<int:batchId>',views.adminDataBatch),
    path('admin/data',views.jsonAdmin),
    path('admin/data/school/<int:schoolId>',views.adminDataSchool),
    path('admin/data/school',views.adminDataAllSchool),
    path('data/school/<int:schoolId>',views.reactDataSchool),
    path('u/student/<str:studentname>',views.studentUser),
    path('post/<int:postid>',views.postView),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
