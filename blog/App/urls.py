from . import views
from django.urls import path

urlpatterns = [
    path('', views.Postlist.as_view(), name="home"),
    path('<slug:slug>/', views.DetailedView.as_view(), name="post_detail"),
]