from django.db import models

class CustomOrder(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()
    DEPARTMENT_CHOICES = [
        ('computerscience', 'Computer Science'),
        ('biologyscience', 'Biology Science'),
        ('commerce', 'Commerce'),
        ('humanities', 'Humanities'),
        ('journalism', 'Journalism'),
    ]
    department_id = models.CharField(max_length=15, choices=DEPARTMENT_CHOICES)
    course_id = models.CharField(max_length=100)
    PURPOSE_CHOICES = [
        ('enquiry', 'Enquiry'),
        ('order', 'Place Order'),
        ('return', 'Return'),
    ]
    purpose = models.CharField(max_length=7, choices=PURPOSE_CHOICES)
    materials_provide = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name