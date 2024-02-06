from django.db import models



# Create your models here.

class enquery(models.Model):
    full_Name = models.TextField()
    email = models.EmailField()
    about = models.TextField()

    def __str__(self):
        return self.full_Name
