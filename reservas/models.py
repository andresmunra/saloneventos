from django.db import models
from django.utils import timezone
from users.models import UserProfile

class Salones(models.Model):
    id = models.AutoField(primary_key=True),
    name = models.CharField(max_length=120, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='imagenes/', default='imagenes/default.png')
    
    def __str__(self):
        return self.name 
    
class Reservas(models.Model):
    id = models.AutoField(primary_key=True),
    date = models.DateField()
    codReserva = models.CharField(max_length=120, blank=False, null=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    salon = models.ForeignKey(Salones, on_delete=models.CASCADE)