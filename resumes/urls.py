from django.urls import path
from . import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('experience/', views.experience, name='experience'),
    path('educational_history/', views.educational_history, name='educational_history'),
    path('skills/', views.skills, name='skills'),
    path('hobbies/', views.hobbies, name='hobbies'),
    path('contact/', views.contact, name='contact'),  
]

urlpatterns += staticfiles_urlpatterns()