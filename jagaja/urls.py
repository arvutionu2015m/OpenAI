from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ai-soovitused/', views.ai_soovitused, name='ai_soovitused'),
    path('muuda-alamülesanne/', views.muuda_alamülesanne, name='muuda_alamülesanne'),
    path('signup/', views.signup, name='signup'),
    path('lisa/', views.lisa_ülesanne, name='lisa_ülesanne'),
]