from django.db import models


class GearType(models.Model):
    """
    Model that allows dynamic creation of
    """

    name = models.CharField(max_length=50)

    additional_requirements = models.JsonField

    def __str__(self):
        return self.name

