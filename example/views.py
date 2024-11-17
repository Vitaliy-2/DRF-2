from gettext import install
from django import views
from rest_framework.decorators import action
from django.core.serializers import serialize
from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from .serializers import CarSerializer
from .models import Car, Category
from rest_framework.views import APIView
from rest_framework.response import Response


# Минимализация кода благодаря наследованию от viewsets.ModelViewSet
# где происходит наследования от миксинов реализующие весь функционал CRUD
class CarViewSet(viewsets.ModelViewSet):
    # queryset = Car.objects.all()
    serializer_class = CarSerializer

    # Чтобы не отображать все данные из БД можно переопределить кверисет
    # который должен возвращать список определенных данных
    # Если запрос будет с конкретным pk, то нужно отобразить одну запись,
    # для этого требуется проверка
    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Car.objects.all()[:3]  # Первые 3 записи из БД

        return Car.objects.filter(pk=pk)


    # Добавляем функционал - расширяем третий путь для вывода списка категорий
    # Парметр methods - указываем метод обращения
    # detail - при фолсе отобразиться именно список, а не одна категория
    @action(methods=['get'], detail=False)
    def categoryes(self, request):
        cats = Category.objects.all()
        return Response({'cats': [c.name for c in cats]})
    
    # Отображение одной категории по pk
    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})









# Наследование от конкретных представлений, отвечающих за определенные действия
# Чтений (GET) и добавление записей (POST)
# class CarAPIList(generics.ListCreateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer


# Редактирование записи (PUT, Patch)
# class CarAPIUpdate(generics.UpdateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer


# CRUD операции в одном классе
# class CarAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer


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
