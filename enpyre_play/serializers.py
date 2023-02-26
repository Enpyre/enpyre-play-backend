from rest_framework.serializers import ModelSerializer


class DynamicFieldsModelSerializer(ModelSerializer):
    '''
    A ModelSerializer that takes an additional `exclude_fields` argument that
    controls which fields should not be included.
    '''

    def __init__(self, *args, **kwargs):
        exclude_fields = kwargs.pop('exclude_fields', None)

        super().__init__(*args, **kwargs)

        if exclude_fields is not None:
            to_exclude = set(exclude_fields)
            existing = set(self.fields)
            for field_name in to_exclude & existing:
                self.fields.pop(field_name)
