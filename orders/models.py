from django.db import models
from profiles.models import user
from books.models import book

status_choices = (
    ("placed", "Placed"),
    ("using", "Using"),
    ("returned", "Returned"),
)

# Create your models here.
class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(book, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(user, on_delete=models.SET_NULL, blank=True, null=True)
    taken = models.DateTimeField(blank=True, null=True)
    exp_return = models.DateTimeField(blank=True, null=True)
    r_status = models.CharField(choices=status_choices, default="placed", max_length=20)

    # placed
    # using
    # returned

    class Meta:
        managed = False
        db_table = 'orders'