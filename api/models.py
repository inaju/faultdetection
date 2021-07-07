from django.db import models
# Create your models here.


class ErrorCodeModel(models.Model):
    uid = models.IntegerField(null=True)
    error_code = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.error_code
