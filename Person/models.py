from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.
# Fonction de validation
def verifLength(value):
    if len(str(value)) != 8:
        raise ValidationError("Le CIN doit contenir exactement 8 chiffres.")
    return value

# Fonction de validation pour l'email
def verifEmail(value):
    if (str(value).endswith("@esprit.tn") == False):
        raise ValidationError("L'email {v} doit se terminer par @esprit.tn", params={'v': value},)
    return value
    # return f"Your email {value} must ends with @esprit.tn"
class Person(AbstractUser):
    cin = models.IntegerField(primary_key=True,validators=[verifLength])
    email = models.EmailField(unique=True)

    