from django.db import models

# Create your models here.
class login_det(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    status=models.CharField(max_length=20)
    datetime=models.CharField(max_length=100)
    
    class Meta:
        db_table='login'
class doctor_det(models.Model):
    d_name=models.CharField(max_length=20)
    d_mob=models.CharField(max_length=20)
    d_email=models.CharField(max_length=100)
    d_address=models.CharField(max_length=100)
    d_district=models.CharField(max_length=20)
    d_dob=models.CharField(max_length=20)
    d_department=models.CharField(max_length=20)
    d_gender=models.CharField(max_length=20)
    d_username=models.CharField(max_length=100)
    d_password=models.CharField(max_length=100)
    d_datetime=models.CharField(max_length=100)
    
    
    class Meta:
        db_table='doctor'
class patient_det(models.Model):
    p_name=models.CharField(max_length=20)
    p_mob=models.CharField(max_length=20)
    p_email=models.CharField(max_length=100)
    p_address=models.CharField(max_length=100)
    p_district=models.CharField(max_length=20)
    p_dob=models.CharField(max_length=20)
    p_age=models.CharField(max_length=20)
    p_gender=models.CharField(max_length=20)
    p_username=models.CharField(max_length=100)
    p_password=models.CharField(max_length=100)
    p_datetime=models.CharField(max_length=100)
    
    class Meta:
        db_table='patient'
class lab_det(models.Model):
    l_name=models.CharField(max_length=20)
    l_num=models.CharField(max_length=20)
    l_details=models.CharField(max_length=100)
    l_username=models.CharField(max_length=100)
    l_password=models.CharField(max_length=100)
    l_datetime=models.CharField(max_length=100)
    
    class Meta:
        db_table='lab'
class pharmacy_det(models.Model):
    ph_name=models.CharField(max_length=20)
    ph_num=models.CharField(max_length=20)
    ph_details=models.CharField(max_length=100)
    ph_username=models.CharField(max_length=100)
    ph_password=models.CharField(max_length=100)
    ph_datetime=models.CharField(max_length=100)
    
    class Meta:
        db_table='pharmacy'
class bloodbank_det(models.Model):
    b_name=models.CharField(max_length=20)
    b_num=models.CharField(max_length=20)
    b_details=models.CharField(max_length=100)
    b_username=models.CharField(max_length=100)
    b_password=models.CharField(max_length=100)
    b_datetime=models.CharField(max_length=100)
    
    class Meta:
        db_table='bloodbank'



