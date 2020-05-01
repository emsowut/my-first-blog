from django.conf import settings
from django.db import models
from django.utils import timezone
#lines that add some bits from other files


class Post(models.Model):
    # defines our model (an object) named Post
    # models.Model means that Post is a Django Model, 
    # so Django knows to save it in the database
    
    # properties:
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # ForeignKey is a link to another model
    title = models.CharField(max_length=200) 
    # CharField(max_length=XXX) = how to define text with a limited number of characters
    text = models.TextField()
    # TextField() = long text with no limit
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # methods:
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title