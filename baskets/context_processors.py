from baskets.models import Basket


def baskets(request):
    print(f'context processor baskets works')
    baskets = []

    if request.user.is_authenticated:
        baskets = Basket.objects.filter(user=request.user)

    return {
        'baskets': baskets,
    }