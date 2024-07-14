



from django.urls import path 
from ytdownload_app import views 
  
urlpatterns = [ 
    path("", views.ytube,name="ytube"), 
] 