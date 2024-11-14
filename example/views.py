from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from .serializers import CarSerializer
from .models import Car
from rest_framework.views import APIView
from rest_framework.response import Response


class CarAPIView(APIView):
    def get(self, request):
        # Сначала добыли кверисет, а потом набор конкретных значений
        lst = Car.objects.all().values()
        return Response({'posts': list(lst)})
    
    # Метод добавляет новую запись в таблицу Car и возвращает то, что было добавлено
    def post(self, request):
        post_new = Car.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )

        # model_to_dict - встроенная функция которая преобразовывает
        # объект (post_new) класса Car в словарь
        return Response({'post': model_to_dict(post_new)})



# class CarAPIView(generics.ListAPIView):
#     queryset = Car.objects.all()
#     # Передаем класс сериализатора
#     serializer_class = CarSerializer
