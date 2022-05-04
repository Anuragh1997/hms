from django.db import models
from ADMIN.models import patient_det

# Create your models here.
class report_det(models.Model):
    p_id=models.ForeignKey(patient_det,on_delete=models.CASCADE)
    r_name=models.CharField(max_length=20)
    r_details=models.CharField(max_length=100)
    r_path=models.ImageField(upload_to='reports/')
    r_date=models.CharField(max_length=20)
    r_addedby=models.CharField(max_length=20)
    r_datetime=models.CharField(max_length=100)
    
    
    class Meta:
        db_table='lab_reports'