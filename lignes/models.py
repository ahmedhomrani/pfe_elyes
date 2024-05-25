from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from account.models import User

class Ligne(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    datecreation = models.DateTimeField(auto_now_add=True)
    sem = models.CharField(max_length=50,default="sem")

    def __str__(self):
        return self.title
    
class Test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    nbr_banc = models.IntegerField(default=0)
    

    def __str__(self):
        return self.name
    
class LigneTest(models.Model):
    ligne = models.ForeignKey(Ligne, related_name='ligne_tests', on_delete=models.CASCADE)
    test = models.ForeignKey(Test, related_name='test_lignes', on_delete=models.CASCADE)
    periodicity = models.CharField(max_length=100,default="Hebdo")

    def __str__(self):
        return f"{self.ligne.title} - {self.test.name}"
    
class Banc(models.Model):
    ligne_test = models.ForeignKey(LigneTest, related_name='bancs', on_delete=models.CASCADE)
    banc_name = models.CharField(max_length=100)
    validated_by_technician = models.BooleanField(default=False)
    validated_by_validator = models.BooleanField(default=False)
    technician = models.ForeignKey(User, related_name='banc_technician_validations', on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'role': User.TECHNICIEN})
    validator = models.ForeignKey(User, related_name='banc_validator_validations', on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'role': User.VALIDATEUR})
    validation_date = models.DateField(blank=True, null=True)
    revalidation_date = models.DateField(blank=True, null=True)
    validator_visa = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.ligne_test} - {self.banc_name}"
    
@receiver(post_save, sender=Banc)
def increment_nbr_banc(sender, instance, created, **kwargs):
    if created:
        test = instance.ligne_test.test
        test.nbr_banc = Banc.objects.filter(ligne_test__test=test).count()
        test.save()

@receiver(post_delete, sender=Banc)
def decrement_nbr_banc(sender, instance, **kwargs):
    test = instance.ligne_test.test
    test.nbr_banc = Banc.objects.filter(ligne_test__test=test).count()
    test.save()
