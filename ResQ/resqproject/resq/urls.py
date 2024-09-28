from django.urls import path 
from .views import hospital_dashboard
# importing views from views..py 
from .views import resq
from . import views
  
urlpatterns = [ 
    path('', views.resq, name='resq'), 
    path('index/', views.index, name='index'),
    path('dashboard/', hospital_dashboard, name='hospital_dashboard'),
    path('dashboard.html', views.dashboard, name='dashboard_html'),  # Added this line
]
