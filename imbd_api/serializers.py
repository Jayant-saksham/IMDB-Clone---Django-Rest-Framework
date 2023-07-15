from rest_framework import serializers
from . models import Movie

# def validate_function(value):

#     if len(value) <= 5:
#         raise serializers.ValidationError('Des must be more than 5 characters')
#     return value 

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie 
        fields = '__all__'
        # exclude = ['active']



    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length = 40)
    # desc = serializers.CharField(max_length = 80, validators=[validate_function])
    # active = serializers.BooleanField(default = True)

    # def validate_name(self, value):
    #     if len(value) <= 2:
    #         raise serializers.ValidationError('Name must be more than 2 characters')
    #     return value
    
    # def validate(self, data):
    #     if data['name'] == data['desc']:
    #         raise serializers.ValidationError('Name and description must be different') 
    #     return data 
    

    # def create(self, validated_data):
    #     return Movie.objects.create(**validated_data) 
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.desc = validated_data.get('desc', instance.desc)
    #     instance.active = validated_data.get('active', instance.active)
    #     instance.save()
    #     return instance  