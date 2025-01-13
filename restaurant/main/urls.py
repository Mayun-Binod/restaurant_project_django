from django.urls import path
from .views import *
urlpatterns = [
    path("",index,name="index"),
    path("about/",about,name="about"),
    path("contact/",contact,name="contact"),
    path("menu/",menu,name="menu"),
    path("service/",service,name="service"),
    path('terms/', terms, name='terms'),
    path('privacy/', privacy, name='privacy'),
    path('support/', support, name='support'),
    path('policy/',policy, name='policy'),
    # ------------------------------auth part-----------------------------
    path("register/",register,name="register"),
]
