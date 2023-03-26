from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('login/',views.login,name='login'),
    # path('admin/', admin.site.urls),
    # path('result/', views.result, name='result')
]
