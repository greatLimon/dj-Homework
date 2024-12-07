# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Sensor, TemperatureMeasurment
from .serializers import SensorSerializer, SensorDetailSerializer, TemperatureMeasurmentSerializer
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        Sensor(name = request.data.get('name'), description = request.data.get('description')).save()
        return Response({'status': 'OK'})
    

class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    # def get_queryset(self):
    #     sensor = Sensor.objects.filter(pk=self.kwargs.get('pk', None))
    #     # measurements = TemperatureMeasurment.objects.filter(sensor_id = sensors.id).all()
    #     return sensor
    
    def patch(self, request, pk):
        obj = Sensor.objects.get(id = pk)
        name = request.data.get('name')
        if name != None:
            obj.name = name
        desc = request.data.get('description')
        if desc != None:
            obj.description = desc
        obj.save()
        return Response({'status': 'OK'})
    


class TemperatureMeasurmentView(ListAPIView):
    queryset = TemperatureMeasurment.objects.all()
    serializer_class = TemperatureMeasurmentSerializer

    def post(self, request):
        sensor_id = request.data.get('sensor')
        if sensor_id == None:
            return Response({'status': 'sensor is None'})
        temperature = request.data.get('temperature')
        if temperature == None:
            return Response({'status': 'temperature is None'})
        sensor = Sensor.objects.get(id = sensor_id)
        TemperatureMeasurment(sensor_id = sensor, temperature = temperature).save()
        return Response({'status': 'OK'})