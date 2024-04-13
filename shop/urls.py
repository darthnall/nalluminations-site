from django.urls import path

from . import views

app_name = "shop"
urlpatterns = [
    path("", views.home, name="home"),
    path("all/", views.all, name="all"),
    path("<int:product_id>/", views.detail, name="detail"),
]
