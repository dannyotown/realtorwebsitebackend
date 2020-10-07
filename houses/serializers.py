from rest_framework import serializers

from .models import House


class HouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = House
        fields = ('id', 'street_name', 'city', 'state', 'zip_code',
                  'price', 'amount_of_beds', 'amount_of_baths', 'square_feet')
