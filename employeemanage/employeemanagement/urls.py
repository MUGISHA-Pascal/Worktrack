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
    path("changeprofile",views.changeprofile,name="changeprofile"),    
    path("search",views.search,name="search"),
    path("perfomance",views.perfomance,name="perfomance"),
    path("manageemployees",views.manageemployees.as_view(),name="manageemployees")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
