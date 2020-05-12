
from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    text = models.CharField(max_length=200)
    #auto_now_add=True - set this attribute to the current date and time
    date_added = models.DateTimeField(auto_now_add=True)
    #Sets a user as owner for each topic for authentification
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text
    

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        #it allows us to set a special attribute telling Django to use 'Entries'
        # when it needs  to refer to more than one entry. Without this, Django
        # would refer to multiple entries as 'Entrys'.
        verbose_name_plural = 'entries'
        
    def __str__(self):
        return f"{self.text[:50]}..."
