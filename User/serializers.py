from rest_framework import serializers
from .models import MyUser



class MyUserSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = MyUser
        fields = ['email','password','password2','first_name','middle_name','last_name']
        extra_kwargs = {'password':{'write_only':True}}

    def validate(self, attrs):
        password1 = attrs.get('password')
        password2 = attrs.get('password2')
        if password1 != password2:
            raise serializers.ValidationError("Password does not match")
        return attrs

    def create(self, validated_data):
        return MyUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id','email','first_name','middle_name','last_name']
    
class UserDetailsChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['first_name','middle_name','last_name']

class UserChangePasswordSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = MyUser
        fields = ['password','password2']
        extra_kwargs = {'password':{'write_only':True}}
    
    def validate(self, attrs):
        password1 = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')
        if password1 != password2:
            raise serializers.ValidationError("Password does not match")
        user.set_password(password1)
        user.save()
        return attrs


    