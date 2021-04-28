from django.db import models


class cityweather(models.Model):
    name = models.CharField(max_length=200) 
    fetch_date = models.DateTimeField()
    sunrise = models.DateTimeField()
    sunset = models.DateTimeField()
    temp = models.DecimalField(max_digits=10, decimal_places=2)
    feels = models.DecimalField(max_digits=10, decimal_places=2)
    pressure = models.DecimalField(max_digits=10, decimal_places=2)
    humidity = models.IntegerField()
    dew_point = models.DecimalField(max_digits=10, decimal_places=2)
    uvi= models.DecimalField(max_digits=10, decimal_places=2)
    clouds = models.IntegerField()
    wind_speed = models.DecimalField(max_digits=10, decimal_places=2)
    wind_deg = models.IntegerField()
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=200) 
    
    

    def __str__(self):
        return self.name

    class Meta:
       unique_together = ("name", "fetch_date")