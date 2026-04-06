from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import People
from .serializers import PeopleSerializer

@extend_schema_view(
    list=extend_schema(
        summary="List all people",
        description="Returns a list of all registered people."
    ),
    create=extend_schema(
        summary="Create person",
        description="Creates a new person with validated data."
    ),
    retrieve=extend_schema(
        summary="Get person",
        description="Retrieve a person by ID."
    ),
    update=extend_schema(
        summary="Update person",
        description="Update a person by ID."
    ),
    partial_update=extend_schema(
        summary="Partial update person",
        description="Update a person by ID."
    ),
    destroy=extend_schema(
        summary="Delete person",
        description="Delete a person by ID."
    )
)
class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
