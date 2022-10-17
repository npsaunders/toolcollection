from django.urls import path

from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('tools/', views.tools_index, name='index'),
  path('tools/<int:tool_id>/', views.tools_detail, name='detail'),
]

