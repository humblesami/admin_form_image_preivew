from django.db import models

class App1Model(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
