from django.db import models

# Create your models here.
class book(models.Model):
    book_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)    
    authors = models.CharField(max_length=100)
    publi_date = models.DateField(blank=True, null=True)
    n_copies = models.IntegerField(blank=True, null=True)
    available = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    n_read = models.IntegerField(blank=True, null=True, default=0)  
    cover = models.ImageField(upload_to ='books/', default = "books/noImg.jpg")

    class Meta:
        managed = False 
        db_table = 'books' 