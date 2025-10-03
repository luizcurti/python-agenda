from rest_framework import serializers
from ..models import Contact, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ContactSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'phone', 'email', 'description', 'category', 'visible', 'photo')
