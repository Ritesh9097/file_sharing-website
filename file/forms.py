from django.db import models
from django.forms import ModelForm
from django.conf import settings
from .models import File


class FileForm(ModelForm):

    class Meta:
        model = File
        fields = ('name', 'path')
