from rest_framework import serializers

from core.models import CustomForm


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomForm
        fields = (
            'form_id',
            'form_title',
            'created_at'
        )


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomForm
        fields = (
            'form_id',
            'field_name',
            'field_description',
            'field_type',
            'field_choices',
            'created_at'
        )
