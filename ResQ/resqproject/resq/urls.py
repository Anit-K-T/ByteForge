from django.urls import path 
  
# importing views from views..py 
from .views import resq
from . import views
  
urlpatterns = [ 
    path('', resq), 
    path('', views.index, name='index'),

]