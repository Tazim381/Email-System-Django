from django.urls import path
from . import views
urlpatterns =[
    path('',views.send_mail_page, name = "home")
]