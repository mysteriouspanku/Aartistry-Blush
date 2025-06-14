from django.contrib import admin
from .models import Posts, SiteSettings, CarouselImage, HomeCard

# Register your models here
admin.site.register(Posts)
admin.site.register(SiteSettings)
admin.site.register(CarouselImage)
admin.site.register(HomeCard)