from rest_framework import serializers

from ..models import PersonType, Gender, Nationality, MaritalStatus, State
from .base import CaseInsensitiveUniqueMixin, CodeValueFormatMixin

class PersonTypeSerializer(CodeValueFormatMixin, CaseInsensitiveUniqueMixin,serializers.ModelSerializer):
    class Meta:
        model = PersonType
        fields = '__all__'

class GenderSerializer(CodeValueFormatMixin, CaseInsensitiveUniqueMixin, serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'

class NationalitySerializer(CodeValueFormatMixin, CaseInsensitiveUniqueMixin, serializers.ModelSerializer):
    class Meta:
        model = Nationality
        fields = '__all__'

class MaritalStatusSerializer(CodeValueFormatMixin, CaseInsensitiveUniqueMixin, serializers.ModelSerializer):
    class Meta:
        model = MaritalStatus
        fields = '__all__'

class StateSerializer(CodeValueFormatMixin, CaseInsensitiveUniqueMixin, serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
