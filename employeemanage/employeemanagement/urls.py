from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name="employeemanagement"
urlpatterns = [
    path("",views.signupview,name="signupview"),
    path("login",views.loginview,name="login"),
    path("home",views.homeview,name="home"),
    path("trainingrecords",views.trainingrecords,name="trainingrecords"),
    path("profile",views.profile,name="profile"),  
    path("search",views.search,name="search"),
    path("perfomance",views.perfomance,name="perfomance"),
    path("manageemployees",views.manageemployees.as_view(),name="manageemployees"),
    path("manageperfomance",views.manageperfomance.as_view(),name="manageperfomance"),
    path("managetraining",views.managetraining.as_view(),name="managetraining")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
