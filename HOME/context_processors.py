from .models import SiteSettings

def global_settings(request):
    return {
        'settings': SiteSettings.objects.first()
    }