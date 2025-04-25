from django.db import models

# Modelo para usuários
class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

# Modelo para equipes
class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)

# Modelo para atividades
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    duration = models.IntegerField()  # em minutos
    created_at = models.DateTimeField(auto_now_add=True)

# Modelo para leaderboard
class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

# Modelo para treinos
class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()  # em minutos
    created_at = models.DateTimeField(auto_now_add=True)