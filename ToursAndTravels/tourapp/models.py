from django.db import models

# Create your models here.

class Car(models.Model):
	car_name	=models.CharField(max_length=100)
	car_no		=models.CharField(max_length=100)
	car_capacity=models.IntegerField()
	car_price	=models.FloatField()
	car_luggage_capa=models.IntegerField()
	car_img		=models.ImageField()

	class Meta:
		db_table='tour'


	def __str__(self):
		return self.name

   
