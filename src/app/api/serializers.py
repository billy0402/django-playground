from rest_framework.serializers import ModelSerializer

from src.app.books.models import Author, Book, Classification, Publisher, Tag
from src.utils.serializers import NestedFieldMixin


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class ClassificationSerializer(ModelSerializer):
    class Meta:
        model = Classification
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class BookSerializer(NestedFieldMixin, ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    publisher = PublisherSerializer(read_only=True)
    classification = ClassificationSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        depth = 1
        fields = (
            'id',
            'created_at',
            'updated_at',
            'name',
            'introduction',
            'price',
            'authors',
            'author_ids',
            'publisher',
            'publisher_id',
            'classification',
            'classification_id',
            'tags',
            'tag_ids',
        )
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
        )
        nested_serializer_fields = {
            'authors': ['id', 'name'],
            'publisher': ['id', 'name'],
            'classification': ['id', 'name'],
            'tags': ['id', 'name'],
        }
        many_related_mapping = {
            'author_ids': 'authors',
            'publisher_id': 'publisher',
            'classification_id': 'classification',
            'tag_ids': 'tags',
        }
