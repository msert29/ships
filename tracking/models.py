from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_imo_number(value):
    if len(value) != 7:
        raise ValidationError(_("IMO number format is incorrect!"))
    
class Ship(models.Model):
    imo_number = models.PositiveIntegerField(primary_key=True, validators=[validate_imo_number])
    name = models.CharField(max_length=50)

class Position(models.Model):
    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-timestamp"]