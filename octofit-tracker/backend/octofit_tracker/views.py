from rest_framework import viewsets
from django.http import JsonResponse
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the OctoFit Tracker API!",
        "documentation_url": "https://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev/docs"
    })

# ViewSet para usuários
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ViewSet para equipes
class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

# ViewSet para atividades
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

# ViewSet para leaderboard
class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

# ViewSet para treinos
class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer