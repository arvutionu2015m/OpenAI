from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Ülesanne(models.Model):
    kasutaja = models.ForeignKey(User, on_delete=models.CASCADE)
    pealkiri = models.CharField(max_length=200)
    kirjeldus = models.TextField()
    pilt = models.ImageField(upload_to='ülesanded/', blank=True, null=True)
    tähtaeg = models.DateField(null=True, blank=True)  # ← uus väli
    loodud = models.DateTimeField(auto_now_add=True)

    def on_peatne(self):
        if self.tähtaeg:
            return self.tähtaeg <= timezone.now().date()
        return False

class AlamÜlesanne(models.Model):
    ülesanne = models.ForeignKey(Ülesanne, related_name='alamülesanded', on_delete=models.CASCADE)
    sisu = models.CharField(max_length=300)
    tehtud = models.BooleanField(default=False)
