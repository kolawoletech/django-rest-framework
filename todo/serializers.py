from rest_framework import serializers
from todo.models import Item, LANGUAGE_CHOICES, STYLE_CHOICES

from django.contrib.auth.models import User

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='item-highlight', format='html')

    class Meta:
        model = Item
        fields = ('url', 'id', 'highlight', 'owner',
                  'title', 'item_description', 'completed', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    todo = serializers.HyperlinkedRelatedField(many=True, view_name='item-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'todo')