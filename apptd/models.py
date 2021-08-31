from django.db import models

class Tarea(models.Model):
    tarea = models.CharField(max_length=100)

    def __self__(self):
        return self.tarea
