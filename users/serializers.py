from rest_framework import serializers

from users.models import User
from users.validators import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    login = serializers.CharField(
        required=True,
    )
    password = serializers.CharField(
        validators=[validate_password], write_only=True, required=True)
    password2 = serializers.CharField(validators=[validate_password], write_only=True, required=True)

    class Meta:
        model = User
        fields = ('login', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            login=validated_data['login'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
