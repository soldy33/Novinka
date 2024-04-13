from django.db import models
from datetime import timedelta
from django.utils import timezone



class Knihovna(models.Model):
    aboniment = models.IntegerField()
    nazev_knihy = models.CharField(max_length=150)
    datum_vypujceni = models.DateTimeField(auto_now_add=True)
    datum_vraceni = models.DateTimeField(blank=True, null=True)
    prodlouzit = models.BooleanField(default=False)
    novy_datum = models.DateTimeField(blank=True, null=True)

    @classmethod
    def vraceni_knihy(cls):
        knihy = cls.objects.filter(datum_vypujceni__lte= timezone.now() - timedelta(minutes=3))
        for kniha in knihy:
            kniha.datum_vraceni = timezone.now() + timedelta(weeks=4)
            kniha.save()

    def prodlouzit_vypujcku(self):
        if self.prodlouzit is not None:
            self.prodlouzit = True
            self.novy_datum = self.datum_vraceni + timezone.timedelta(weeks=2)
            self.save()

