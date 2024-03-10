from django.urls import path
from . import views

app_name = 'weekdays'
urlpatterns = [
    path('', views.weekdays, name='weekdays'),
    path('uz/', views.uz, name='uz'),
    path('en/', views.en, name='en'),
    path('ru/', views.ru, name='ru'),
]
