from django.urls import path, include
from .views import products_view, product_detail_view, category_list

app_name = "shop"

urlpatterns = [
    path("", products_view, name="products"),
    path("<slug:slug>/", product_detail_view, name="product_detail"),
    path("search/<slug:slug>/", category_list, name="category_list"),
]