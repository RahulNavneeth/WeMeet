from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# from django.db.models.deletion import CASCADE


class school(models.Model):
    school_name = models.CharField(max_length=100,null=False)
    school_email = models.EmailField(max_length=50,null=False)
    school_joined_WeMeet = models.DateTimeField(auto_now_add=True)
    school_password = models.CharField(max_length=15,null=False)
    school_url = models.CharField(max_length=30,null=False)
    school_propic = models.ImageField()
    school_address_state = models.CharField(max_length=100,null=False)
    school_address_district = models.CharField(max_length=100,null=False)
    school_address_area = models.CharField(max_length=100,null=False)
    School_description = models.CharField(max_length=300)
    school_noof_batch = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])

    def __str__(self):
        return self.school_name


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
    school_reference = models.ForeignKey(school,on_delete=models.CASCADE)

    def __str__(self):
        return 'school: '+str(self.school_reference)+' ,'+' year: '+str(self.batch_year)+' , '+'std: '+str(self.batch_std)    



class student(models.Model):
    
    student_name = models.CharField(max_length=30,null=False)
    student_aka_name = models.CharField(max_length=30,null=False)
    student_email = models.EmailField(max_length=50,null=False)
    student_password = models.CharField(max_length=30,null=False)
    student_propic = models.ImageField()
    student_description = models.CharField(max_length=300)
    school_reference_id_student = models.ForeignKey(school,on_delete=models.CASCADE)
    batch_reference_id_student = models.ForeignKey(batch,on_delete=models.CASCADE)

    def __str__(self):
        return 'Name: '+str(self.student_name)+' , '+'Pet Name: '+str(self.student_aka_name)    
    def __unicode__(self): 
        return self.batch_reference_id_student
