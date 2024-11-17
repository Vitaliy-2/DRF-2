from dataclasses import field
from email.policy import default
import io
from rest_framework import serializers
from .models import Car
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# Сериализатор связанный с моделью
class CarSerializer(serializers.ModelSerializer):
    # Создается скрытое поле (Hidden) и по дефолту этот юзер
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = "__all__"
        # fields = ("title", "content", "cat")













# class CarModel:
#     def __init__(self, title, content) -> None:
#         self.title = title
#         self.content = content


# Serializer - данный метод не подвязан с моделью
# class CarSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()

#     # Метод добавления записи
#     # validated_data словарь будет состоять из всех проверенных данных,
#     # который пришли с POST запроса
#     def create(self, validated_data):
#         return Car.objects.create(**validated_data)
    
#     # instance - ссылка на объект Car
#     # Пытаемся добыть измененые поля, иначе оставляем как было изначально
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.time_update = validated_data.get("time_update", instance.time_update)
#         instance.is_published = validated_data.get("is_published", instance.is_published)
#         instance.cat_id = validated_data.get("cat_id", instance.cat_id)
#         # Сохраняем в базу данных
#         instance.save()
#         return instance


# Сначала объект преобразовываем в словарь, а потом в json строку.
# def encode():
#     model = CarModel('BMW', 'Content: Очень быстрая')
    # результат сериализации
    # model_sr = CarSerializer(model)
    # data - сериализованные данные
    # print(model_sr.data, type(model_sr.data), sep='\n')
    # json = JSONRenderer().render(model_sr.data)
    # print(json)


# декодирование из json в данные
# def decode():
#     stream = io.BytesIO(b'{"title":"BMW","content":"Content: \xd0\x9e\xd1\x87\xd0\xb5\xd0\xbd\xd1\x8c \xd0\xb1\xd1\x8b\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x8f"}')
#     data = JSONParser().parse(stream)
#     serializer = CarSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)




# Сериалазер, который работает с моделью, представлять данные
# в json формат и отправлять пользователю
# class CarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Car
        # Поля, которые будут отправляться пользователю
        # fields = ('title', 'cat_id')
