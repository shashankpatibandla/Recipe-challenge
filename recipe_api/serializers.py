from rest_framework import serializers
from .models import *

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'url',  'ingredient_text', 'recipe')

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ('id', 'url',  'step_text', 'recipe')

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'url',  'name',  'user', 'step_set', 'ingredient_set')
        read_only_fields = ('step_set', 'ingredient_set',)


class UserSerializer(serializers.ModelSerializer):
    recipe = serializers.StringRelatedField()
    password = serializers.CharField(style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'first_name', 'last_name', 'password', 'recipe')