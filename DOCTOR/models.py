from django.db import models
from ADMIN.models import doctor_det,patient_det

# Create your models here.
class prescription_det(models.Model):
    p_id=models.ForeignKey(patient_det,on_delete=models.CASCADE)
    d_id=models.ForeignKey(doctor_det,on_delete=models.CASCADE)
    pres=models.CharField(max_length=500)
    status=models.CharField(max_length=20,default="Pending")
    datetime=models.CharField(max_length=100)
      
    class Meta:
        db_table='prescription'
