import re
from rest_framework import serializers

class CaseInsensitiveUniqueMixin:

    def validate(self, attrs):
        model = self.Meta.model

        for field in ['code_value', 'name']:
            if field in attrs:
                value = attrs[field]

                filter_kwargs = {f"{field}__iexact": value}
                queryset = model.objects.filter(**filter_kwargs)

                # Excluir instancia actual en update
                if self.instance:
                    queryset = queryset.exclude(pk=self.instance.pk)

                if queryset.exists():
                    raise serializers.ValidationError({
                        field: f"{field} already exists (case-insensitive)."
                    })

        return attrs
    
class CodeValueFormatMixin:
    def validate_code_value(self, value):
        if not value:
            raise serializers.ValidationError("Code value cannot be empty.")
        
        value = value.upper()

        if not re.fullmatch(r'[A-Z]+', value):
            raise serializers.ValidationError("Only letters are allowed.")
        
        return value