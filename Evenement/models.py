from django.db import models
from Person.models import Person
from django.utils.timezone import now
# Create your models here.
class Evenement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/',blank=True)

    CATEGORY_CHOICES=(
        ('M','Music'),('S','Sport'),('C','Cinema')
    )
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    statut = models.BooleanField(default=False)
    nb_participants = models.IntegerField(default=0)
    evt_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Organizer = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    Participation = models.ManyToManyField(Person, related_name='Participations', through='Participation_event')
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(evt_date__gte=now()),
                name='evt_date_cannot_be_in_past'
            )
        ]
        ordering = ('title', 'evt_date')
class Participation_event(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    participation_date = models.DateField(auto_now_add=True)
    class Meta:
        unique_together = ('person', 'evenement')
