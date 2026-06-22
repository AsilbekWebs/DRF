from django.db import models

# Create your models here.

class Product(models.Model):
    CHOICES = (
        ('black', 'BLACK'),
        ('white', 'WHITE'),
        ('blue', 'BLUE'),
        ('green', 'GREEN'),
        ('red', 'RED'),
        ('purple', 'PURPLE'),
        ('orange', 'ORANGE'),
        ('yellow', 'YELLOW'),
        ('pink', 'PINK'),
        ('brown', 'BROWN'),
        ('gray', 'GRAY'),
        ('grey', 'GREY'),
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    color = models.CharField(max_length=100, choices=CHOICES)
    created_add = models.DateTimeField(auto_now_add=True)
    updated_add = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        ordering = ['-created_add']
        db_table = 'product'

