
from rest_framework import viewsets

from .serializers import HouseSerializer
from .models import House


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all().order_by('id')
    serializer_class = HouseSerializer
