from django.db import models
from profiles.models import user
from books.models import book

# Create your models here.
class comment(models.Model):
    book = models.OneToOneField(book, on_delete=models.CASCADE)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comments'
        unique_together = (('book', 'user'),)