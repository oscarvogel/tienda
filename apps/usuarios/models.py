from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Nacimiento')
    cel_no = models.CharField(max_length=100, default='', verbose_name='Numero de celular')
    email_confirmed = models.BooleanField(default=False, verbose_name='Correo confirmado')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Perfil usuario'
        verbose_name_plural = 'Perfiles usuario'

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
