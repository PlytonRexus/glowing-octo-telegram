from django.db import models

class PowerPlant(models.Model):
    SEQGEN = models.IntegerField()
    YEAR = models.IntegerField()
    PSTATABB = models.CharField(max_length=2)
    PNAME = models.CharField(max_length=100)
    GENNTAN = models.FloatField()
    PERCENTAGE = models.FloatField()

    def __str__(self):
        return self.PNAME
