from django.db import models

# Create your models here.
class donor_det(models.Model):
    do_name=models.CharField(max_length=20)
    do_mob=models.CharField(max_length=20)
    do_group=models.CharField(max_length=100)
    do_address=models.CharField(max_length=100)
    do_district=models.CharField(max_length=20)
    do_dob=models.CharField(max_length=20)
    do_age=models.CharField(max_length=20)
    do_gender=models.CharField(max_length=20)
    do_datetime=models.CharField(max_length=100)
     
    class Meta:
        db_table='donor'
class bldrec_det(models.Model):
    do_id=models.ForeignKey(donor_det,on_delete=models.CASCADE)
    db_group=models.CharField(max_length=20)
    db_unit=models.CharField(max_length=20,default="1")
    db_date=models.CharField(max_length=20)
    db_datetime=models.CharField(max_length=100)
     
    class Meta:
        db_table='blood_received'