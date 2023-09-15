from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'

class Book(models.Model):
    title = models.CharField(max_length=80)
    rating = models.IntegerField(validators=[MinValueValidator(0),
                                             MaxValueValidator(5)])
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'