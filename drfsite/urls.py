"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from example.views import CarAPIList, CarAPIUpdate, CarAPIDestroy



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/car/', CarAPIList.as_view()),
    path('api/v1/car/<int:pk>/', CarAPIUpdate.as_view()),
    path('api/v1/cardelete/<int:pk>/', CarAPIDestroy.as_view()),
]






# # Создаем объект роутера
# router = routers.DefaultRouter()
# # регистрируем его.
# # 1 аргумент - префикс для набора маршрутов (car)
# # 2 аргумент - указать класс вью сета
# # router.register(r'car', CarViewSet, basename='car') # можно менять название путей таким образом
# # basename - обязательный параметр, если во views в классе не указан параметр queryset
# router.register(r'car', CarViewSet, basename='car')
# print(router.urls)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/car/ или http://127.0.0.1:8000/api/v1/car/7/

#     # path('api/v1/carlist/', CarViewSet.as_view({'get': 'list'})),
#     # path('api/v1/carlist/<int:pk>/', CarViewSet.as_view({'put': 'update'})),
# ]
