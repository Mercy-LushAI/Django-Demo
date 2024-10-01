from django.db import models

# Create your models here.
class Room(models.Models):
    # host = 
    # topic = 
    name = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    # participants = 
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def _str__(self):
        return self.name
