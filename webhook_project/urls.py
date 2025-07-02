from django.contrib import admin
from django.urls import path
from webhooks.views import receive_webhook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhook/', receive_webhook),  # <- Aquí está tu endpoint
]