from django.db import models



# Create your models here.

class enquery(models.Model):
    full_Name = models.TextField()
    email = models.EmailField()
    about = models.TextField()

    def __str__(self):
        return self.full_Name

class apply(models.Model):
    first_Name = models.CharField(max_length = 50)
    last_Name = models.CharField(max_length = 50)
    email = models.EmailField()
    mobile = models.CharField(max_length = 20)
    notice_Period = models.TextField()
    years_Of_Experience = models.CharField(max_length = 20)
    skills = models.TextField()
    applied_Role = models.CharField(max_length = 100, null= True)
    
    def __str__(self):
        return self.first_Name