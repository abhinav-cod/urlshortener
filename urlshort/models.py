from django.db import models
from .utils import create_tiny_url

# Create your models here.
class tinyurls(models.Model):
    time_created=models.DateTimeField(auto_now_add=True)
    num_times_followed=models.PositiveIntegerField(default=0)
    original_url=models.URLField()
    tiny_url=models.CharField(max_length=15,unique=True,blank=True)

    class Meta:
        ordering=['-time_created']

    def __str__(self):
        return "{} to {}".format(self.original_url,self.tiny_url)

    def save(self, *args, **kwargs):
        if not self.tiny_url:
            self.tiny_url=create_tiny_url(self)
        super().save(self, *args, **kwargs)
