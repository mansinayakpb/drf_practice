from rest_framework import serializers
from .models import Student


def start_with_r(value):
    if value[0].lower() != "r":
        raise serializers.ValidationError("Name should be start with R")


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.roll = validated_data.get("roll", instance.roll)
        instance.city = validated_data.get("city", instance.city)

        instance.save()
        return instance

    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("seat Full")
        return value

    def validate(self, data):
        name = data.get("name")
        city = data.get("city")
        if name.lower() == "Jomon" and city.lower() != "ranchi":
            raise serializers.ValidationError("city must be Ranchi")
        return data
