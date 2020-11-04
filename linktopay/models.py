from django.db import models

# Create your models here.

class LinkToPayRequest(models.Model):
    id = models.CharField(max_length=80, blank=True, primary_key=True)
    dev_reference = models.CharField(max_length=100, blank=False, null=False)
    amount = models.FloatField()

    def __str__(self):
        return self.name + ' ' + self.last_name

    @property
    def playlist_id(self):
        return self.id
