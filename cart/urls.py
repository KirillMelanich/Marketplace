from django.urls import path, include
from .views import cart_view, cart_add, cart_delete, cart_update

app_name = "cart"

urlpatterns = [
    path("", cart_view, name="cart-view"),
    path("add/", cart_add, name="add-to-cart"),
    # path("search/<slug:slug>/", category_list, name="category-list"),
]
