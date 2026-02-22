from rest_framework import serializers

from .models import Category, Task


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class TaskSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    owner_name = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "category",
            "category_name",
            "priority",
            "is_completed",
            "created_at",
            "due_date",
            "owner_name",
        ]
