from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Subscriber(models.Model):
    first_name = models.CharField(default="", blank="True", null="True", max_length=32)
    last_name = models.CharField(default="", blank="True", null="True", max_length=32)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add="True")

    def __unicode__(self):  # Python3 __str__
        return self.email
