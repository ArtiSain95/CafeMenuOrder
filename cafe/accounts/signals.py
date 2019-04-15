from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import MealItem

# @receiver(post_save, sender=MealItem)
# def create_order(sender, instance, created, **kwargs):
#     import ipdb; ipdb.set_trace()
#     if created:
#         # import ipdb; ipdb.set_trace()
#         add = float(int(instance.menu.Price) * instance.quantity)
#         instance.total_item_price = add
#         instance.total_item_price.save()
#         print(instance.total_item_price)
#     else:
#         pass