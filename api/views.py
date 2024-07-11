from rest_framework import status, views
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.models import Book

# from api.serializers import BookListSerializer
from api.serializers import BookSerializer


# Create your views here.
class BookListCreateAPIView(views.APIView):
    """一覧・登録API"""

    def get(self, request, *arg, **kwargs):
        """本の一覧取得"""

        # 一覧取得
        book_list = Book.objects.all()
        # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book_list, many=True)
        # serializer = BookListSerializer(instance=book_list)
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


class BookRetrieveUpdateDestroyAPIView(views.APIView):
    """本モデルの詳細取得・更新・削除APIクラス"""

    def get(self, request, uuid, *args, **kwargs):
        """詳細取得"""

        # モデルオブジェクトを取得
        book = get_object_or_404(Book, uuid=uuid)
        # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book)
        # レスポンスオブジェクトを返す
        return Response(data=serializer.data)

    def put(self, request, uuid, *args, **kwargs):
        """更新"""

        # モデルオブジェクトを取得
        book = get_object_or_404(Book, uuid=uuid)
        # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book, data=request.data)
        # # 一部更新（patch）の場合は "partial=True" を指定
        # serializer = BookSerializer(
        #     instance=book,
        #     data=request.data,
        #     partial=True,
        # )
        # バリデーションを実行
        serializer.is_valid(raise_exception=True)
        # モデルオブジェクトを更新
        serializer.save()
        # レスポンスオブジェクトを返す
        return Response(data=serializer.data)

    def delete(self, request, uuid, *args, **kwargs):
        """削除"""

        # モデルオブジェクトを取得
        book = get_object_or_404(Book, uuid=uuid)
        # モデルオブジェクトを削除
        book.delete()
        # レスポンスオブジェクトを返す
        return Response(status=status.HTTP_204_NO_CONTENT)
