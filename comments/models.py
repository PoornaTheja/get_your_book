from django.db import models
from profiles.models import user
from books.models import book

# Create your models here.
class comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(book, on_delete=models.CASCADE)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comments'
        # unique_together = (('book', 'user'),) 