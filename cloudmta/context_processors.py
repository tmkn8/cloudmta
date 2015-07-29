from django.conf import settings

def settings_context_processor(request):
    return {
        'FORUM_LINK': settings.FORUM_LINK
    }
