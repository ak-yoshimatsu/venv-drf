from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """本モデル用シリアライザ"""

    class Meta:
        model = Book
        """対称のモデルクラス"""
        fields = ["id", "uuid", "title", "price"]
        """利用するモデルのフィールドを指定"""


class BookListSerializer(serializers.ListSerializer):
    """複数の本モデルを扱うシリアライザ"""

    # 扱うシリアライザを指定
    child = BookSerializer()
