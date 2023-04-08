from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from app.mixins import MultipleSerializerMixin, EnablePartialUpdateMixin
from app.serializers import UsersListeSerializer, UsersDetailsSerializer
from rest_framework import permissions
from django.contrib.auth.models import User

class ReadUpdateModelViewSet(ModelViewSet):
    http_method_names = ["get", "put", "patch"]

class CreateModelViewSet(ModelViewSet):
    http_method_names = ["post"]

# class UsersAPIViewset(MultipleSerializerMixin, ModelViewSet):
# class UsersAPIViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
class UsersAPIViewset(MultipleSerializerMixin, ReadUpdateModelViewSet, EnablePartialUpdateMixin):
    serializer_class = UsersListeSerializer
    details_serializer_class = UsersDetailsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = User.objects.all()

        return queryset
