from rest_framework import serializers
from todo.models import Item, LANGUAGE_CHOICES, STYLE_CHOICES

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'title', 'item_description', 'completed', 'language', 'style')

'''     def create(self, validated_data):
        """
        Create and return a new `Item` instance, given the validated data.
        """
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Item` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.item_description = validated_data.get('item_description', instance.item_description)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance '''