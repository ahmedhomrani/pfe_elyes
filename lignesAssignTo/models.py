from django.db import models
from django.conf import settings

from lignes.models import Ligne  # Import settings module

class LignesAssignto(models.Model):
    # ForeignKey to Ligne model
    ligne = models.ForeignKey(Ligne, on_delete=models.CASCADE, related_name='assignments')
    # ForeignKey to User model (technician)
    technician = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='technician_assignments')
    # Status field
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    # Realisation date field
    realisation_date = models.DateField(null=True, blank=True)
    comment = models.TextField(blank=True) 
    affectation_date = models.DateField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ligne.title} - {self.technician.email}"
