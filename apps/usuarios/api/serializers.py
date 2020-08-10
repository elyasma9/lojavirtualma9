from rest_framework.serializers import ModelSerializer
from apps.usuarios.models import CustomUser


class UsuariosSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'nome', 'sobrenome', 'email', 'cpf', 'rg', 'telefone')


class UsuariosCompletoSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'nome', 'sobrenome', 'email', 'password',
                  'cpf', 'rg', 'telefone')

    def create(self, validated_data):
        user = CustomUser.objects.create(
            nome=validated_data['nome'],
            sobrenome=validated_data['sobrenome'],
            email=validated_data['email'],
            cpf=validated_data['cpf'],
            rg=validated_data['rg'],
            telefone=validated_data['telefone'],
            is_staff=True,
            is_active=True
        )
        if validated_data['password']:
            user.set_password(validated_data['password'])
        user.save()

        return user


class UsuariosChangePasswordSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'password')

    def update(self, validated_data):

        user = CustomUser.objects.filter(pk=validated_data['id'])

        if user and validated_data['password']:
            user.set_password(validated_data['password'])
            user.save()

        return user
