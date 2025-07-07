from .models import CartItem

def cart_summary(request):
    total_sum = 0
    total_count = 0

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_sum = sum(item.get_total_price() for item in cart_items)
        total_count = sum(item.quantity for item in cart_items)

    return {
        'cart_total_sum': total_sum,
        'cart_total_count': total_count,
    }