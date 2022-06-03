from rest_framework import serializers
from .models import Prestamos


class PrestamosSerializer(serializers.Serializer):
    idPrestamo = serializers.IntegerField(read_only=True)
    idLibro = serializers.IntegerField()
    idUsuario = serializers.IntegerField()
    fecPrestamo = serializers.DateField()
    fecDevolucion = serializers.DateField()

    def create(self, validated_data):
        """
        Create and return a new `Serie` instance, given the validated data.
        """
        return Prestamos.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Serie` instance, given the validated data.
        """
        instance.idPrestamo = validated_data.get('idPrestamo', instance.idPrestamo)
        instance.idLibro = validated_data.get('idLibro', instance.idLibro)
        instance.idUsuario = validated_data.get('idUsuario', instance.idUsuario)
        instance.fecPrestamo = validated_data.get('fecPrestamo ', instance.fecPrestamo )
        instance.fecDevolucion = validated_data.get('fecDevolucion', instance.fecDevolucion)
        instance.save()
        return instance

class PrestamosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamos
        fields = ('id', 'idPrestamo', 'idLibro', 'idUsuario', 'fecPrestamo','fecDevolucion')

