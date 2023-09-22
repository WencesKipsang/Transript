from django.contrib.auth.models import AbstractUser,Permission,Group
from django.db import models

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django. dispatch import receiver
from django.utils.translation import gettext_lazy as _
# from django.utils.translation import gettext as _

# Create your models here.
SEMESTER_CHOICES=(("1","1"),
                  ("2","2"),
                  ("3","3"),)
gender=(("Male","Male"),
        ("Female","Female"),)
religion=(("Christian","Christian"),
          ("Muslim","Muslim"),
          ("Pagan","Pagan"),)
years=((1,1),
       (2,2),
       (3,3),
       (4,4),)
perio=(("3","3"),
       ("4","4"),
       ("5","5"))
class School(models.Model):
    school_name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.school_name
    
class Department(models.Model):
    department_name=models.CharField(max_length=200)
    school= models.ForeignKey(School,related_name='school',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.department_name

class Course(models.Model):
    course_code=models.CharField(max_length=20,unique=True)
    course_name=models.CharField(max_length=100)
    total_gredit=models.CharField(max_length=50)
    period=models.CharField(choices=perio,default="4")
    department=models.ForeignKey(Department,on_delete=models.CASCADE,related_name='depertment')
    
    def __str__(self):
        return self.course_name
        # return str(self.course_code) + " " + str(self.course_name)
    

class Units(models.Model):
    unit_code= models.CharField(max_length=20)
    unit_name= models.CharField(max_length=200)
    course= models.ForeignKey(Course,related_name='course', on_delete= models.CASCADE)
    
    def __str__(self):
        return self.unit_name


class Student(models.Model):
    student_reg_no=models.CharField(unique=True)
    id_number=models.IntegerField()
    password= models.CharField()
    first_name=models.CharField(max_length=20)
    second_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20,null=True,blank=True)
    phone_no=models.CharField(max_length=12)
    email_address=models.EmailField()
    date_of_birth=models.DateField(auto_now=False,auto_now_add=False)
    gender= models.CharField(max_length=20,choices=gender,default="Male")
    religion=models.CharField(max_length=20,choices=religion,default="Christian")
    admission_date=models.DateField()
    course_code=models.ForeignKey(Course,on_delete=models.CASCADE,to_field='course_code', related_name='students_with_course_code')
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='students_with_course_name')
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    school_name=models.ForeignKey(School,on_delete=models.CASCADE)
    place_of_residence=models.CharField(max_length=50)   
    
    
class Teacher(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return (
            str(self.first_name)
            + " "
            + str(self.last_name)
        )
    
class Marks(models.Model):
    student_reg_no=models.ForeignKey(Student,on_delete=models.CASCADE)    
    sub_code1= models.CharField(max_length=20)
    sub_1= models.CharField(max_length=200)
    marks_1= models.IntegerField(null=True,blank=True) 
    grade_1=models.CharField(max_length=1,null=True,blank=True)
    sub_code2= models.CharField(max_length=20)
    sub_2= models.CharField(max_length=200)
    marks_2= models.IntegerField(null=True,blank=True)
    grade_2=models.CharField(max_length=1,null=True,blank=True)  
    sub_code3= models.CharField(max_length=20)
    sub_3= models.CharField(max_length=200)
    marks_3= models.IntegerField(null=True,blank=True)
    grade_3=models.CharField(max_length=1,null=True,blank=True)
    sub_code4= models.CharField(max_length=20)
    sub_4= models.CharField(max_length=200)
    marks_4= models.IntegerField(null=True,blank=True)
    grade_4=models.CharField(max_length=1,null=True,blank=True)
    sub_code5= models.CharField(max_length=20)
    sub_5= models.CharField(max_length=200)
    marks_5= models.IntegerField(null=True,blank=True)
    grade_5=models.CharField(max_length=1,null=True,blank=True)
    sub_code6= models.CharField(max_length=20)
    sub_6= models.CharField(max_length=200)
    marks_6= models.IntegerField(null=True,blank=True)
    grade_6=models.CharField(max_length=1,null=True,blank=True)
    sub_code7= models.CharField(max_length=20)
    sub_7= models.CharField(max_length=200)
    marks_7= models.IntegerField(null=True,blank=True)
    grade_7=models.CharField(max_length=1,null=True,blank=True)
    remark= models.CharField(max_length=200)
    semester =models.CharField(max_length=20,choices=SEMESTER_CHOICES,default='1')
    student_year= models.IntegerField(choices=years)

  
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Units, on_delete=models.CASCADE)
class CusomUser(AbstractUser):
    student= models.OneToOneField('Student', on_delete=models.CASCADE,null=True,blank=True)
    
    class Meta:
        # Add this line to specify unique related names
        permissions = (("can_change_status", "Can change status"),)
    
    
    # Add a related_name to resolve the clash
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name="customuser_set",  # Add a unique related_name
        related_query_name="customuser",
        help_text=_("Specific permissions for this user."),
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_("The groups this user belongs to. A user will get all permissions granted to each of their groups."),
        related_name="customuser_groups",  # Add a unique related_name
        related_query_name="customuser_group",
    )  
    
    is_teacher = models.BooleanField("teacher status", default=False)
    is_student = models.BooleanField("student status", default=False)
    
    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = [
    #     "is_teacher",
    # ]
    
  
#   `registered_units` varchar(255) NOT NULL,
#   `unit_reg_status` varchar(255) NOT NULL,
#   `reg_status` varchar(50) NOT NULL,  
User= get_user_model()
def create_user_for_student(sender, instance, created, **kwargs):
    if created:
        User.objects.create_user(
            username= instance.student_reg_no,
            password= instance.password
        )
# Connect the signal
post_save.connect(create_user_for_student, sender=Student)