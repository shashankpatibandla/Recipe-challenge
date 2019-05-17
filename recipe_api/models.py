from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique= True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Recipe(models.Model):
    name = models.CharField(max_length=50,null= False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Step(models.Model):
    step_text = models.CharField(max_length=50, null = False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


    def __str__(self):
        return self.step_text


class Ingredient(models.Model):
    ingredient_text = models.CharField(max_length=50, null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient_text





