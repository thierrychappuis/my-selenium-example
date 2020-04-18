from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path("", views.result_search, name="result_search"),
    path("", views.product_sheet, name="product_sheet"),
]
