from django.utils import timezone
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Group, Lesson
from .serializers import ProductSerializer, LessonSerializer


class ProductAccessView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        user = request.user

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'message': 'Продукт не найден.'}, status=status.HTTP_404_NOT_FOUND)

        if product.start_data <= timezone.now():
            groups = Group.objects.filter(product=product)

            if not groups.exists():
                return Response({'message': 'Группы для продукта не найдены.'}, status=status.HTTP_404_NOT_FOUND)

            min_group = min(groups, key=lambda group: group.students.count())
            max_group = max(groups, key=lambda group: group.students.count())

            min_users = min_group.students.count()
            max_users = max_group.students.count()

            if max_users - min_users > 1:
                max_group.students.remove(max_group.students.last())

            if max_group.students.count() >= max_group.max_users:
                return Response({'message': 'Достигнуто максимальное количество пользователей в группе.'}, status=status.HTTP_400_BAD_REQUEST)

            min_group.students.add(user)

            return Response({'message': 'Вы успешно получили доступ к продукту и были добавлены в группу.'})
        else:
            return Response({'message': 'Продукт еще не начался. Пожалуйста, дождитесь начала продукта.'},
                            status=status.HTTP_400_BAD_REQUEST)

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LessonListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LessonSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Lesson.objects.filter(product_id=product_id)
