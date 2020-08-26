from rest_framework.serializers import ModelSerializer
from enderecos.models import Endereco


class EnderecossSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = (
            "id",
            "logradouro",
            "bairro",
            "cep",
            "cidade",
            "estado",
            "numero",
            "user",
        )

    def create(self, validated_data):
        endereco = Endereco.objects.create(
            logradouro=validated_data["logradouro"],
            bairro=validated_data["bairro"],
            cep=validated_data["cep"],
            cidade=validated_data["cidade"],
            estado=validated_data["estado"],
            numero=validated_data["numero"],
            user=validated_data["user"],
        )
        endereco.save()

        return endereco
