from rest_framework import Serializers


class productSerializer(Serializers.Serializers):

    id = Serializers.IntegerField()
    title = Serializers.CharField(max_length=255)
    unit_price = Serializers.DecimalFields(max_digits=6, decimal_places=2)
