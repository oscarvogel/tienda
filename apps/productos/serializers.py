from rest_framework import serializers

from apps.productos.models import Favoritos


class FavoritosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favoritos
        fields = ['articulo', 'usuario']