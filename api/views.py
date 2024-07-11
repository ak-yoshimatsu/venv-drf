from rest_framework import status, views
from rest_framework.response import Response

from api.models import Book
from api.serializers import BookListSerializer, BookSerializer


# Create your views here.
class BookListCreateAPIView(views.APIView):
    """一覧・登録API"""

    def get(self, request, *arg, **kwargs):
        """本の一覧取得"""
        # 一覧取得
        book_list = Book.objects.all()
        # シリアライザオブジェクトを作成
        # serializer = BookSerializer(instance=book_list, many=True)
        serializer = BookListSerializer(instance=book_list)
        # レスポンスオブジェクトを返す
        return Response(data=serializer.data)

    def post(self, reqest, *args, **kwargs):
        """本の登録"""
        # シリアライザオブジェクトを作成
        serializer = BookSerializer(data=reqest.data)
        # バリデーションを実行
        serializer.is_valid(raise_exception=True)
        # モデルオブジェクトを登録
        serializer.save()
        # レスポンスオブジェクトを返す
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
