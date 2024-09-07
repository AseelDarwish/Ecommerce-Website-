from django.conf import settings
from django.http import HttpRequest

class Cart:
    def __init__(self, request: HttpRequest):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart 

        def add(self,product):
            product_id = str(product.id) 
            if product_id in self.cart:
                pass
            else:
                self.cart[product_id] = {'price':str(product.price)}
                self.session.modified = True