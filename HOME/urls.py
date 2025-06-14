from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from HOME import views

urlpatterns = [
    path('admin/', admin.site.urls),  # ✅ Add this
    path('', views.index, name='Home'),
    path('about', views.about, name='about'),
    path('upload', views.uploadPosts, name='upload'),
    path('nailart', views.nailart, name='nailart'),
    path('makeup', views.makeup, name='makeup'),
    path('productReview', views.productReview, name='review'),
    path('contact', views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
