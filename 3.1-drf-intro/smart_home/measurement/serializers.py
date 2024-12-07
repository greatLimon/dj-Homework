from rest_framework import serializers

from .models import Sensor, TemperatureMeasurment
# TODO: опишите необходимые сериализаторы

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class TemperatureMeasurmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureMeasurment
        fields = ['sensor_id', 'temperature', 'datetime']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = TemperatureMeasurmentSerializer(read_only = True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']