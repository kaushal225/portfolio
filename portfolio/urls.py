from django.urls import URLPattern, path
from . import views
urlpatterns=[
    path('',views.home,name="home"),
    path('skills/',views.skills,name="skills"),
    path('contact/',views.contact,name="contact")
]
