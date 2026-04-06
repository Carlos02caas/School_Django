from rest_framework import serializers
from .models import School

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

    def validate(self, data):
        name = data.get('name')
        address = data.get('address')
        zip_code = data.get('zip_code')

        instance = getattr(self, 'instance', None)

        qs = School.objects.all()

        if instance:
            qs = qs.exclude(pk=instance.pk)

        if name:
            qs = qs.filter(
                name__iexact=name,
                address__iexact=address,
                zip_code=zip_code
            )
            if qs.exists():
                raise serializers.ValidationError("A School with this information already exists.")
            
        return data