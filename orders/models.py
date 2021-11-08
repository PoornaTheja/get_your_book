from django.db import models
from profiles.models import user
from books.models import book

# Create your models here.
class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(book, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(user, on_delete=models.SET_NULL, blank=True, null=True)
    taken = models.DateTimeField(blank=True, null=True)
    exp_return = models.DateTimeField(blank=True, null=True)
    r_status = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'