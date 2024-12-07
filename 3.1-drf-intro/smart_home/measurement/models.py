from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, null=True)

class TemperatureMeasurment(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name= 'measurements')
    temperature = models.DecimalField(max_digits=4, decimal_places=2)
    datetime = models.DateTimeField(auto_now_add=True)
