from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class Furniture(models.Model):
    # Had to implement id because Document Class didn't recognize it's existence
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True, null=False, default='Furniture')
    item_stock = models.IntegerField(null=True)

    def __str__(self):
        return '%s' % (self.name)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)