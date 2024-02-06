from .forms import ShippingAddressForm

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from cart.cart import Cart

from .models import Order, OrderItem, ShippingAddress


@login_required(login_url="account:login")
def shipping(request):
    try:
        shipping_address = ShippingAddress.objects.get(user=request.user)
    except ShippingAddress.DoesNotExist:
        shipping_address = None

    form = ShippingAddressForm(instance=shipping_address)

    if request.method == "POST":
        form = ShippingAddressForm(request.POST, instance=shipping_address)
        if form.is_valid():
            shipping_address = form.save(commit=False)
            shipping_address.user = request.user
            form.save()
            return redirect("account:dashboard")

    return render(request, "payment/shipping.html", {"form": form})


def checkout(request):
    if request.user.is_authenticated:
        shipping_address = get_object_or_404(ShippingAddress, user=request.user)
        if shipping_address:
            return render(request, "payment/checkout.html", {"shipping_address": shipping_address})
    return render(request, "payment/checkout.html")


def complete_order(request):
    if request.POST.get("action") == "payment":
        name = request.POST.get("name")
        email = request.POST.get("email")
        street_address = request.POST.get("address1")
        apartment_address = request.POST.get("address2")
        city = request.POST.get("city")
        country = request.POST.get("state")
        zip_code = request.POST.get("zip_code")

        cart = Cart(request)
        total_price = cart.get_total_price()

        shipping_address, _ = ShippingAddress.objects.get_or_create(
            user=request.user,
            defaults= {
                "full_name": name,
                "email": email,
                "street_address": street_address,
                "apartment_address": apartment_address,
                "city": city,
                "country": country,
                "zip_code": zip_code
            }
        )

        if request.user.is_authenticated:
            order = Order.objects.create(user=request.user, shipping_address=shipping_address, amount=total_price)

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["qty"],
                    user=request.user,
                )
        else:
            order = Order.objects.create(shipping_address=shipping_address, amount=total_price)

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["qty"],
                )

        return JsonResponse({"success": True})


def payment_success(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return render(request, "payment/payment-success.html")


def payment_fail(request):
    return render(request, "payment/payment-failed.html")
