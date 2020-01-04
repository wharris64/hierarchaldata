from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ghostback.quickstart import models


class RoastBoastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RoastBoast
        fields = ['roast', 'content','votes','downvotes','posttime']
        