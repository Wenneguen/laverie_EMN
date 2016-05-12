from django.utils import timezone
from django.db import models


class Appareil(models.Model):
    duree = models.IntegerField(default=50)
    heure_fin = models.DateTimeField(default=timezone.now)
    temps_restant = models.DurationField(default=timezone.timedelta())
    interesses = models.IntegerField(default=0)
    libre = models.BooleanField(default=True)
    TYPES = (
        ('machine', 'Machine à laver'),
        ('seche_linge', 'Sèche linge'),
    )
    type = models.CharField(max_length=20, choices=TYPES, default='machine')

    def __str__(self):
        return "%s %s" %(self.type, self.id)

    def add_interesse(self):
        self.interesses += 1
        self.save()

    def remove_interesse(self):
        self.interesses -= 1
        self.save()

    def actualiser(self):
        if not self.libre:
            temps_restant = self.temps_restant = self.heure_fin - timezone.now()
            if temps_restant.days >= 0:
                self.temps_restant = temps_restant
            else:
                self.libre = True
                self.temps_restant = timezone.timedelta()
            self.save()

    def get_minutes_restantes(self):
        return (10+self.temps_restant.seconds)//60





