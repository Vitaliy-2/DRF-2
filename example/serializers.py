import io
from rest_framework import serializers
from .models import Car
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class CarModel:
    def __init__(self, title, content) -> None:
        self.title = title
        self.content = content


# Serializer - данный метод не подвязан с моделью
class CarSerializer(serializers.Serializer):
    # Чтобы при сериализации DRF понимал что title является строкой
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()


# Сначала объект преобразовываем в словарь, а потом в json строку.
def encode():
    model = CarModel('BMW', 'Content: Очень быстрая')
    # результат сериализации
    model_sr = CarSerializer(model)
    # data - сериализованные данные
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)


# декодирование из json в данные
def decode():
    stream = io.BytesIO(b'{"title":"BMW","content":"Content: \xd0\x9e\xd1\x87\xd0\xb5\xd0\xbd\xd1\x8c \xd0\xb1\xd1\x8b\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x8f"}')
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)




# Сериалазер, который работает с моделью, представлять данные
# в json формат и отправлять пользователю
# class CarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Car
        # Поля, которые будут отправляться пользователю
        # fields = ('title', 'cat_id')
