from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.conf import settings

# from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# from django.db.models.deletion import CASCADE


class school(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name="user_school",on_delete=models.CASCADE,null=False)
    school_url = models.CharField(max_length=30,null=False)
    school_propic = models.ImageField(upload_to='ProfilePicture/')
    school_address_state = models.CharField(max_length=100,null=False)
    school_address_district = models.CharField(max_length=100,null=False)
    school_address_area = models.CharField(max_length=100,null=False)
    School_description = models.CharField(max_length=300)
    school_noof_batch = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])

    def __str__(self):
        return self.user.username



class batch(models.Model):
    std_choice = [
    (10, 10),
    (12, 12),
]
    batch_year = models.DateField(max_length=100,null=False)
    batch_std = models.IntegerField(choices=std_choice,null=False)
    batch_url = models.CharField(max_length=30,null=False)
    batch_strength = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    batch_description = models.CharField(max_length=300)
    school_reference = models.ForeignKey(school,related_name="school_batch",on_delete=models.CASCADE)

    def __str__(self):
        return 'school: '+str(self.school_reference)+' ,'+' year: '+str(self.batch_year)+' , '+'std: '+str(self.batch_std)    



class student(models.Model):
    std_choice = [
    (10, 10),
    (12, 12),
]  

    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name="user_student",on_delete=models.CASCADE,null=False)
    student_aka_name = models.CharField(max_length=30,null=False)
    student_propic = models.ImageField(upload_to='ProfilePicture/')
    student_std = models.IntegerField(choices=std_choice,null=False)
    student_url =models.CharField(max_length=30,null=False)
    student_address_state = models.CharField(max_length=100,null=False)
    student_address_district = models.CharField(max_length=100,null=False)
    student_address_area = models.CharField(max_length=100,null=False)
    student_description = models.CharField(max_length=300)
    school_reference_id_student = models.ForeignKey(school,related_name="student_school",on_delete=models.CASCADE)
    batch_reference_id_student = models.ForeignKey(batch,related_name="student_batch",on_delete=models.CASCADE)

    def __str__(self):
        return 'School: '+ str(self.school_reference_id_student)+ ' , Name: '+str(self.user.username)+' , '+'Pet Name: '+str(self.student_aka_name)    
    def __unicode__(self): 
        return self.batch_reference_id_student
