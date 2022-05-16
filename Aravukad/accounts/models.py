from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_manager=models.BooleanField(default=False)
    is_principal=models.BooleanField(default=False)
    is_admnStaff=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)
    is_parent=models.BooleanField(default=False)


class Institution(models.Model):
    institution=models.CharField(max_length=255,)

    def __str__(self):
        return self.institution

class SchoolManager(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    

    def __str__(self):
        return self.user.username


class Principal(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    phone=models.CharField(max_length=14)
    school=models.ForeignKey(Institution, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class AdmStaff(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    phone=models.CharField(max_length=14)
    school=models.ForeignKey(Institution, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    phone=models.CharField(max_length=14)
    school=models.ForeignKey(Institution, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username


class Students(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    phone=models.CharField(max_length=14)
    school=models.ForeignKey(Institution, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class Parent(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    phone=models.CharField(max_length=14)
    school=models.ForeignKey(Institution, on_delete=models.CASCADE)
    student=models.ForeignKey(Students, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
