from .models import Character

def characters(request):
    online_player_count = Character.objects.filter(ingame=True).count()
    return {
        'ONLINE_PLAYER_NUMBER': online_player_count
    }
