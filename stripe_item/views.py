from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import stripe
from django.conf import settings
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY
domain = "http://127.0.0.1:8000"
# Create your views here.

def item(request, item_id):
    item = get_object_or_404(Item,
                             id=item_id)
    return render(request,
                  'stripe_item/item.html',
                  {'item': item})


def buy(request, item_id):
    if request.method == 'GET':
        item = get_object_or_404(Item,
                                 id=item_id)
        try:
            stripe_session = stripe.checkout.Session.create(
                success_url=f'{domain}/success/',
                cancel_url=f'{domain}/cancelled/',
                line_items=[
                    {
                        'price_data': {
                            'currency': item.get_status_display,
                            'unit_amount': int(item.price * 100),
                            'product_data': {
                                'name': item.name
                            },
                        },
                        'quantity': 1,
                    },
                ],
                mode="payment",
            )
            return JsonResponse({'session_id': stripe_session['id']})
        except Exception as err:
            print(err)
            return JsonResponse({'error': str(err)})
