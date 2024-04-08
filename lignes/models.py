from django.db import models

class Ligne(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    daterealisation = models.DateField()
    datecreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
