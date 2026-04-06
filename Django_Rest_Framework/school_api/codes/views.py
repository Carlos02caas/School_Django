from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from .models import PersonType, Gender, Nationality, MaritalStatus, State
from .serializer.serializers import PersonTypeSerializer, GenderSerializer, NationalitySerializer, MaritalStatusSerializer, StateSerializer
# Create your views here.

@extend_schema(tags=['Person Type'])
class PersonTypeViewSet(viewsets.ModelViewSet):
    queryset = PersonType.objects.all()
    serializer_class = PersonTypeSerializer

@extend_schema(tags=['Gender'])
class GenderViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer

@extend_schema(tags=['Nationality'])
class NationalityViewSet(viewsets.ModelViewSet):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer

@extend_schema(tags=['Marital Status'])
class MaritalStatusViewSet(viewsets.ModelViewSet):
    queryset = MaritalStatus.objects.all()
    serializer_class = MaritalStatusSerializer

@extend_schema(tags=['State'])
class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer