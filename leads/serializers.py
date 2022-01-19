from dataclasses import field
import imp
from rest_framework import serializers
from leads.models import lead


class leadSerializer(serializers.ModelSerializer):
    class meta:
        model = lead
        fields = '__all__'