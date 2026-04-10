from django.db import models
from utils.models import CommonModel

class Wishlist(CommonModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="wishlist_items")
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="wishlisted_by")

    class Meta:
        unique_together = ("user", "product")
        db_table = "wishlist"


class CartItem(CommonModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="in_carts")
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("user", "product")
        db_table = "cart_item"


    # @property
    # def subtotal(self):
    #     return self.quantity * self.product.price