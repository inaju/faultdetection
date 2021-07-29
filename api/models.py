from django.db import models
# Create your models here.


class ErrorCodeModel(models.Model):
    uid = models.IntegerField(null=True)
    error_code = models.CharField(max_length=100)
    engine_load = models.DecimalField(
        null=True, decimal_places=4, max_digits=1000)
    coolant_temp = models.DecimalField(
        null=True, decimal_places=4, max_digits=1000)
    rpm = models.DecimalField(null=True, decimal_places=4, max_digits=1000)
    intake_pump = models.DecimalField(
        null=True, decimal_places=4, max_digits=1000)
    throttle_pos = models.DecimalField(
        null=True, decimal_places=4, max_digits=1000)
    fuel_pressure = models.DecimalField(
        null=True, decimal_places=4, max_digits=1000)
    speed = models.DecimalField(null=True, decimal_places=4, max_digits=1000)
    intake_pressure = models.DecimalField(
        null=True, decimal_places=4, max_digits=1000)
    date = models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)

    def __str__(self):
        return self.error_code
