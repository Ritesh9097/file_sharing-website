from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField, TextField
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    class GenderChoice(TextChoices):
        MALE = 'M',_('male')
        FEMALE = 'F',_('female')
        OTHER = 'O',_('other')

    user = OneToOneField(User, on_delete=models.CASCADE)
    info = TextField(verbose_name="about me")
    gender = CharField(max_length=1,choices=GenderChoice.choices, default=GenderChoice.MALE)
    image = models.ImageField(_("profile pic"), upload_to="profile",)
    mob = models.IntegerField()
    
    def __str__(self):
        return self.user.username