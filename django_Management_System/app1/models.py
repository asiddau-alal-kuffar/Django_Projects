from django.db import models

# Create your models here.

class Students(models.Model):
    StudentID= models.IntegerField(default=0)
    StudentRoll=models.IntegerField(default=0)
    Class=models.CharField(max_length=100)
    Shift=models.CharField(max_length=100)
    StudentsName=models.CharField(max_length=100)
    FatherName=models.CharField(max_length=100)
    MotherName=models.CharField(max_length=100)
    Mobile=models.IntegerField()
    Gender=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Address=models.TextField()
    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s %s %s" % (self.StudentID,self.StudentRoll,self.Class,self.Shift,self.StudentsName,self.FatherName,self.MotherName,self.Mobile,self.Gender,self.Email , self.Address)



# class Department(models.Model):
#     name=models.CharField(max_length=100,null=False)
#     location=models.CharField(max_length=100)
#     def __str__(self):
#         return self.name

# class roll(models.Model):
#     name=models.CharField(max_length=100,null=False)
#     def __str__(self):
#         return self.name

# class Employee(models.Model):
#     firstName=models.CharField(max_length=100, null=False)
#     lastName=models.CharField(max_length=100)
#     dept=models.ForeignKey(Department,on_delete=models.CASCADE)
#     salary=models.IntegerField(default=0)
#     bonus=models.IntegerField(default=0)
#     role=models.ForeignKey(roll,on_delete=models.CASCADE)
#     phone=models.IntegerField(default=+8801)
#     # hire_date=models.DateField()
#     def __str__(self):
#         return "%s %s %s %s %s %s %s" % (self.firstName,self.lastName,self.dept,self.salary,self.bonus,self.role,self.phone)

