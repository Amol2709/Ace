from rest_framework import serializers

class FarmerInfoSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    state_name = serializers.CharField()
    district_name = serializers.CharField()
    village_name = serializers.CharField()
    phone = serializers.CharField()