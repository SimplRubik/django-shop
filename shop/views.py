from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.db.models import Q

from .forms import ReviewForm
from .models import Product, CartItem, Category, Order, OrderItem


def product_list(request):
    products = Product.objects.all()
    
    query = request.GET.get('q', '')

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )


    category_id =request.GET.get('category')

    if category_id:
        products = products.filter(category__id=category_id)
    
    categories = Category.objects.all()
        
    return render(request, 'shop/product_list.html', {
        'products': products,
        'categories': categories,
        'query': query,
        })


def product_detail(request, pk):
    print("METHOD =", request.method)
    print("POST DATA =", request.POST)


    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect('product_detail', pk=pk)
    else:
        form = ReviewForm()
    return render(request, 'shop/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'form': form,
        })


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    messages.success(request, f"Товар <<{product.name}>> добавлен в корзину")
    return redirect('cart_detail')


@login_required
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'shop/cart_detail.html', {
        'cart_items': cart_items,
        'total': total,
    })


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    messages.success(request, f"Товар <<{item.product.name}>> удален из корзины.")
    return redirect('cart_detail')


@login_required
@require_POST
def update_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    if quantity > 0:
        item.quantity = quantity
        item.save()
        messages.success(request, f"Колличество для <<{item.product.name}>> обновлено!")
    else:
        item.delete()
        messages.info(request, f"Товар <<{item.product.name}>> удален из корзины")
    return redirect('cart_detail')


@login_required
def checkout(request):
    #Забрать все товары пользователя из корзины
    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items.exists():
        return redirect('cart_detail')
    
    total_sum = sum(item.product.price * item.quantity for item in cart_items)
    #СОздать новый заказ
    order = Order.objects.create(user=request.user,
                                 total_sum=total_sum,
                                 )

    #Переносим товары из корзины в заказ
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price_at_purchase=item.product.price
        )
    
    #очищаем корзину
    cart_items.delete()

    return render(request,"shop/checkout_success.html", {'order': order})


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'shop/order_history.html', {'orders': orders})