from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.utils.field_mapping import get_nested_relation_kwargs


class NestedFieldMixin:
    def build_nested_field(self, field_name, relation_info, nested_depth):
        """
        Create nested fields for forward and reverse relationships.
        """
        field_mapping = getattr(self.Meta, 'nested_serializer_fields', {})
        if field_name not in field_mapping:
            return self.build_relational_field(field_name, relation_info)

        class NestedSerializer(serializers.ModelSerializer):
            class Meta:
                model = relation_info.related_model
                depth = nested_depth - 1
                fields = field_mapping[field_name]

        field_class = NestedSerializer
        field_kwargs = get_nested_relation_kwargs(relation_info)

        return field_class, field_kwargs

    def build_property_field(self, field_name, model_class):
        if not field_name.endswith('_id'):
            return super().build_property_field(field_name, model_class)

        related_model = model_class._meta.get_field(field_name).related_model

        field_class = PrimaryKeyRelatedField
        field_kwargs = {
            'source': field_name[:-3],  # remove last '_id'.
            'write_only': True,
            'queryset': related_model.objects.all(),
        }

        return field_class, field_kwargs

    def build_unknown_field(self, field_name, model_class):
        many_related_mapping = getattr(self.Meta, 'many_related_mapping', {})

        if field_name not in many_related_mapping:
            return super().build_unknown_field(field_name, model_class)

        r_field_name = many_related_mapping[field_name]
        related_model = model_class._meta.get_field(r_field_name).related_model

        field_class = PrimaryKeyRelatedField
        field_kwargs = {
            'source': r_field_name,
            'write_only': True,
            'many': True,
            'queryset': related_model.objects.all(),
        }

        return field_class, field_kwargs
