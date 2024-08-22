from django.db import models

# Create your models here.

class Patient(models.Model):
    firstName=models.CharField(max_length=100, null=False)
    lastName=models.CharField(max_length=100)
    username0=models.CharField(max_length=100, null=False)
    pasword=models.CharField(max_length=100)
    phone=models.IntegerField(default=+8801)
    # hire_date=models.DateField()

    def __str__(self):
        return "%s %s %s %s %s" % (self.firstName,self.lastName,self.username0,self.pasword,self.phone)


# class MedicalPrescriptionApp(models.Model):
#     PatientName= models.CharField(max_length=255, null=False)
#     Age=models.IntegerField(default=0)
#     Date = models.DateField(null=True)

#     Class=models.CharField(max_length=100)
#     Shift=models.CharField(max_length=100)
#     StudentsName=models.CharField(max_length=100)
#     FatherName=models.CharField(max_length=100)
#     MotherName=models.CharField(max_length=100)
#     Mobile=models.IntegerField()
#     Gender=models.CharField(max_length=100)
#     Email=models.EmailField(max_length=100)
#     Address=models.TextField()
#     def __str__(self):
#         return "%s %s %s %s %s %s %s %s %s %s %s" % (self.StudentID,self.StudentRoll)






