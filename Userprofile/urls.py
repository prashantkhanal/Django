from django.urls import path
from Userprofile.views import loginView, UserReg
app_name = "user"
urlpatterns = [
    path('login/', loginView.as_view(),name="login"),
    path("register/", UserReg.as_view(), name="register"),

    
]


