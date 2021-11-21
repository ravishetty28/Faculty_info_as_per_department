from django.db import models

class Department(models.Model):
    departmentName = models.CharField(max_length=60)
    

    def __str__(self):
        return self.departmentName

class Faculty(models.Model):
    facultyName = models.CharField(max_length=60)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    dateOfJoining = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=60)

    def __str__(self):
        return self.facultyName

    
    class Meta:
        verbose_name = 'faculty'
        verbose_name_plural = 'faculties'