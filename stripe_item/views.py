from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import stripe
from django.conf import settings
from .models import Item


# Create your views here.

def item(request, item_id):
    item = get_object_or_404(Item,
                             id=item_id)
    return render(request,
                  'stripe_item/item.html',
                  {'item': item})


def buy(request, item_id):
    if request.method == 'GET':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        item = get_object_or_404(Item,
                                 id=item_id)
        domain = "http://127.0.0.1:8000"
        try:
            stripe_session = stripe.checkout.Session.create(
                success_url=f'{domain}/success/',
                cancel_url=f'{domain}/cancelled/',
                line_items=[
                    {
                        'price_data': {
                            'currency': item.currency,
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
            session_id = stripe_session['id']
            return JsonResponse({'session_id': session_id})
        except Exception as err:
            print(err)
            return JsonResponse({'error': str(err)})
