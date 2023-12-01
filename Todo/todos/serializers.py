from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField(read_only=True)

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d %b %Y")

    class Meta:
        model = Todo
        fields = '__all__'
        read_only_field = ['user']
