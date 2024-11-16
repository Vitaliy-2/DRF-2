from gettext import install
from django.core.serializers import serialize
from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from .serializers import CarSerializer
from .models import Car
from rest_framework.views import APIView
from rest_framework.response import Response


# Наследование от конкретных представлений, отвечающих за определенные действия
# Чтений (GET) и добавление записей (POST)
class CarAPIList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# Редактирование записи (PUT, Patch)
class CarAPIUpdate(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# CRUD операции в одном классе
class CarAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# class CarAPIView(APIView):
#     def get(self, request):
#         c = Car.objects.all()
#         # Сериализатору передаем весь кверисет из таблицы.
#         # many - говорит о том, что все записи будут сериализованы
#         # data - переводит данные в словарь
#         return Response({'posts': CarSerializer(c, many=True).data})

#     # Метод добавляет новую запись в таблицу Car и возвращает то, что было добавлено
#     def post(self, request):
#         serializer = CarSerializer(data=request.data)
#         # Валидация происходит в сериализаторе (например ограничение поля)
#         # Чтобы в postMan выводились подробные исключения (поле title не определено)
#         serializer.is_valid(raise_exception=True)
#         #  save автоматически вызовет метод create из сериализатора
#         serializer.save()

#         return Response({'post': serializer.data})

#     # Редактирование записей в БД
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})

#         try:
#             instance = Car.objects.get(pk=pk)

#         except:
#             return Response({"error": "Object does not exists"})

#         # передаем данные, которые нужно изменить и объект который будем менять
#         serializer = CarSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         # метод save автоматически вызывает метод update в сериализаторе
#         serializer.save()
#         return Response({"post": serializer.data})
    
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
        
#         Car.objects.get(pk=pk).delete()

#         return Response({"post": "delete post " + str(pk)})



# class CarAPIView(generics.ListAPIView):
#     queryset = Car.objects.all()
#     # Передаем класс сериализатора
#     serializer_class = CarSerializer
