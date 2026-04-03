from django.db import models

class GlobalSetting(models.Model):
    tema = models.CharField(max_length=50, default='', blank=True)
    font = models.CharField(max_length=50, default='', blank=True)

    def __str__(self):
        return "Pengaturan Tampilan Global"