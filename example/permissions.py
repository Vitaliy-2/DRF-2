from rest_framework import permissions


# Если запрос безопасный (типо на чтение) то даем доступ,
# Если запрос на какие-то действия, то только администротор может зайти
class IsAdminOrReadOnly(permissions.BasePermission):
    # Проверяем права на уровне всего запроса
    def has_permission(self, request, view):
        # Если пришедший запрос безопасный
        # SAFE_METHODS запросы только на чтение, никаких действий (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True  # То предоставляем права доступа
        
        # Проверяем что пользователь вошел как администратор и даем права на действия (удаление)
        return bool(request.user and request.user.is_staff)


# Право на редактирование записей, но только тех, который ты добавил
class IsOwnerOrReadOnly(permissions.BasePermission):
    # Ограничение на конкретную запись (на уровне объекта - одной записи)
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Если юзер из базы данных равен юзеру пользователя, который пришел с запросом тогда даем доступ
        return obj.user == request.user
