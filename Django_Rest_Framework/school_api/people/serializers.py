from rest_framework import serializers
from .models import People

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'

    def validate(self, data):
        ssn = data.get('ssn')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        date_of_birth = data.get('date_of_birth')

        instance = getattr(self, 'instance', None)

        qs = People.objects.all()

        if instance:
            qs = qs.exclude(pk=instance.pk)

        if ssn:
            qs = qs.filter(ssn=ssn)
            if qs.exists():
                raise serializers.ValidationError("A person with this SSN already exists.")
            
        else:
            qs = qs.filter(
                first_name__iexact=first_name,
                last_name__iexact=last_name,
                date_of_birth=date_of_birth
            )
            if qs.exists():
                raise serializers.ValidationError("A person with this name and date of birth already exists.")
            
        return data

    def validate_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone must be a number.")
        
        if len(value) != 10:
            raise serializers.ValidationError("Phone must be 10 digits.")
        
        return value
