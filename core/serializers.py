from rest_framework import serializers

from .models import MenuItem, Restaurant, School, Student


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class SchoolSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
    # Don't pass the 'fields' arg up to the superclass
        # Instantiate the superclass normally
        super(SchoolSerializer, self).__init__(*args, **kwargs)
        allow_students = self.context.get("allow_students",None)
        if allow_students:
            self.fields['students'] = StudentSerializer(many=True, context=kwargs['context'], fields=['name','age','is_adult']) 


    class Meta():
        model = School
        fields = '__all__'


class StudentSerializer(DynamicFieldsModelSerializer):
    class Meta():
        model = Student
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta():
        model = MenuItem
        fields = '__all__'

class ResturantSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(source='filtered_menu_items', many=True, read_only=True)
    class Meta():
        model = Restaurant
        fields = '__all__'
