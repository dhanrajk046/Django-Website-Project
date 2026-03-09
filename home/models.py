from time import timezone
from django.utils import timezone

from django.db import models

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField()
    phone = models.CharField(max_length=15, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    # date = models.DateField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name