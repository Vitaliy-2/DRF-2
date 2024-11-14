from django.core.serializers import serialize
from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from .serializers import CarSerializer
from .models import Car
from rest_framework.views import APIView
from rest_framework.response import Response


class CarAPIView(APIView):
    def get(self, request):
        c = Car.objects.all()
        # Сериализатору передаем весь кверисет из таблицы.
        # many - говорит о том, что все записи будут сериализованы
        # data - переводит данные в словарь
        return Response({'posts': CarSerializer(c, many=True).data})
    
    # Метод добавляет новую запись в таблицу Car и возвращает то, что было добавлено
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        # Валидация происходит в сериализаторе (например ограничение поля)
        # Чтобы в postMan выводились подробные исключения (поле title не определено)
        serializer.is_valid(raise_exception=True)

        post_new = Car.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )

        return Response({'post': CarSerializer(post_new).data})



# class CarAPIView(generics.ListAPIView):
#     queryset = Car.objects.all()
#     # Передаем класс сериализатора
#     serializer_class = CarSerializer
