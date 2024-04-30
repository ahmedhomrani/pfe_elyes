from django.db import models
from django.conf import settings
from lignes.models import Ligne
from lignesAssignTo.models import LignesAssignto

class ValidateurLignesAssignto(models.Model):
    ligne = models.ForeignKey(Ligne, on_delete=models.CASCADE, related_name='validateur_lignes_assignments')
    technician = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='validateur_technician_assignments')
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    realisation_date = models.DateField(null=True, blank=True)
    comment = models.TextField(blank=True) 
    affectation_date = models.DateField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)  # Add confirmed attribute

    def __str__(self):
        return f"{self.ligne.title} - {self.technician.email}"

class Verification(models.Model):
    lignes_assignto = models.OneToOneField(LignesAssignto, on_delete=models.CASCADE, related_name='verification')
    VerificationFinal = models.BooleanField(default=False)
    DateVerification = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.lignes_assignto.ligne.title} - Verification"
