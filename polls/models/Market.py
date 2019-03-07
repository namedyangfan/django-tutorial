from django.db import models


class Market(models.Model):
    internal_name = models.CharField(max_length=255, null=False)
    display_name  = models.CharField(max_length=255, null=False)
    slug          = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.display_name, self.slug)
