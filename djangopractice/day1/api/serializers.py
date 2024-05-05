from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    def numberlimitation(value):
        if value >= 100:
            raise serializers.ValidationError('seat is full')
    
    rollno = serializers.IntegerField(validators=[numberlimitation])

    class Meta:
        model = Student
        fields = ['name', 'rollno', 'description']
        # read_only_fields = ['name']
        # extra_kwargs = {'name': {'read_only': True}}

    def validate_name(self, value):
        if value.lower() == 'demon':
            raise serializers.ValidationError('Name demon is not allowed')
        return value

    def validate(self, data):
        name = data.get('name')
        rollno = data.get('rollno')
        if name.lower() == 'messi' and rollno != 10:
            raise serializers.ValidationError("messi should always be 10")
        return data









# Normal serializer 

# # validators
# def nameiskishor(value):
#     if value.lower() == 'demoncredid':
#         raise serializers.ValidationError('name shouldnout be demoncredid')

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255, validators=[nameiskishor])
#     rollno = serializers.IntegerField()
#     description = serializers.CharField(max_length=255)

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)


#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.rollno = validated_data.get('rollno', instance.rollno)
#         instance.description = validated_data.get('description', instance.description)
#         instance.save()
#         return instance
    

#     # field level validation
#     def validate_rollno(self, value):
#         if value >= 100:
#             raise serializers.ValidationError('rollno should not be more than 100')
#         return value
    
#     # object level validation 
#     def validate(self, data): # data is dictionary here
#         name = data.get('name')
#         description = data.get('description')

#         if name.lower() == 'anshu' and description.lower() != 'angel':
#             raise serializers.ValidationError('Anshu you should always be angel please check correction in description')
        
#         return data
