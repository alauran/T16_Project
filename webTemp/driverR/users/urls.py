from django.conf.urls import url, include
from users.views import dashboard, register, profile,username_change



urlpatterns = [
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/", register, name="register"),
    url(r"^profile/", profile, name="profile"),
    url(r"^username_change_form/",username_change, name="username_change"),

]