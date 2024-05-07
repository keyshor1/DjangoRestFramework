from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    def namekishor(value):
        if value.lower() == 'kishor':
            raise serializers.ValidationError('Common user cannot take kishor name he is admin')
    name = serializers.CharField(validators=[namekishor])

    class Meta:
        model = Student
        fields = ['id', 'name', 'rollno', 'course']

    def validate_rollno(self, value):
        if value >= 100:
            raise serializers.ValidationError('seat is full for you')
        return value

    def validate(self, data):
        name = data.get('name')
        course = data.get('course')

        if course == 'CE' and name.lower() == 'kishor':
            raise serializers.ValidationError("Welcome kishor, kishor who is student in computer engineering is already enrolled you are the boss")
        return data