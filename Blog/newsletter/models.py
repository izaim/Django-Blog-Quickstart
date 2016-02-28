from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Subscribe(models.Model):
    first_name = models.CharField(default="", blank="True", null="True")
    last_name = models.CharField(default="", blank="True", null="True")
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add="True", auto_now="false")

    def __unicode__(self):  # Python3 __str__
        return self.email
