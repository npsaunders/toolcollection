from django.urls import path

from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('tools/', views.tools_index, name='index'),
  path('tools/<int:tool_id>/', views.tools_detail, name='detail'),
  path('tools/create/',views.ToolCreate.as_view(),name = 'tools_create'),
  path('tools/<int:pk>/update/', views.ToolUpdate.as_view(), name='tools_update'),
  path('tools/<int:pk>/delete/', views.ToolDelete.as_view(), name='tools_delete'),
]

