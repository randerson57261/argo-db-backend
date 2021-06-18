from django.conf.urls import url 
from .views import Sensors, GetSensorMeta
 
urlpatterns = [ 
    url(r'^api/sensors$', Sensors.as_view()),
    url(r'^api/sensor_metadata', GetSensorMeta.as_view()),
]
