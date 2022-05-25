
from django.urls import path

from user_interface import views
from user_interface import summary
urlpatterns = [
    path('', views.index, name='index'),
    path("login",views.login_view,name='login'),
    path("logout",views.logout_view,name='logout'),
    path("register",views.register,name='register'),
    path("meeting",views.createmeeting,name='meeting'),
    path("sample",views.sample,name='sample'),
    path("create", views.form_createView, name='create'),

    path("adminLogin", views.adminLogin, name='adminLogin'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("useredit", views.useredit, name='useredit'),

    path("adminSignup", views.adminSignup, name='adminSignup'),
    path("adminSignupFun", views.adminSignupFun, name='adminSignupFun'),

    path("userLogin", views.userLogin, name='userLogin'),
    path("summeryadd", views.summeryadd, name='summeryadd'),
    path("login_user", views.login_user, name='login_user'),
    path("userSignupFun", views.userSignupFun, name='userSignupFun'),

    path("add_meeting_user", views.add_meeting_user, name='add_meeting_user'),

    path("adminDashboard", views.adminDashboard, name='adminDashboard'),
    path("speechgen", views.speechgen, name='speechgen'),
    path("speechgenFun", views.speechgenFun, name='speechgenFun'),

    path("users", views.users, name='users'),
    path("user_add", views.user_add, name='user_add'),
    path("login_admin", views.login_admin, name='login_admin'),
    path("userdashboard", views.userdashboard, name='userdashboard'),

    path("admin_logout", views.admin_logout, name='admin_logout'),
    path("attend", views.attend, name='attend'),
    path("attendfunc", views.attendfunc, name='attendfunc'),

    path('db_delete_user/<id>', views.db_delete_user, name='db_delete_user'),

    path('meeting_edit_admin/<id>', views.meeting_edit_admin, name='meeting_edit_admin'),
    path('meeting_view_admin/<id>', views.meeting_view_admin, name='meeting_view_admin'),
    path('meeting_delete/<id>', views.meeting_delete, name='meeting_delete'),

    path("meetings", views.meetings, name='meetings'),
    path("admin_meeting_add", views.admin_meeting_add, name='admin_meeting_add'),
    path("minutes", views.minutes, name='minutes'),

    path("adminedit", views.adminedit, name='adminedit'),
    path("update_meeting_admin", views.update_meeting_admin, name='update_meeting_admin'),

]