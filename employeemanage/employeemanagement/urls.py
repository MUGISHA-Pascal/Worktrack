from django.urls import path
from . import views
app_name="employeemanagement"
urlpatterns = [
    path("",views.signupview,name="signupview"),
    path("login",views.loginview,name="login"),
    path("home",views.homeview,name="home"),
    path("trainingrecords",views.trainingrecords,name="trainingrecords"),
    path("profile",views.profile,name="profile"),
    path("search",views.search,name="search"),
    path("perfomance",views.perfomance,name="perfomance"),
]
