from rest_framework import serializers
from leads.models import lead


class leadSerializer(serializers.ModelSerializer):
    class Meta:
        model = lead
        fields = '__all__'