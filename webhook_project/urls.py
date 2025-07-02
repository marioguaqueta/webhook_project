from django.contrib import admin
from django.urls import path
from webhooks.views import receive_webhook, article_webhook, client_webhook, receipt_webhook, shift_webhook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhook/inventory', receive_webhook),  
    path('webhook/article/', article_webhook),
    path('webhook/client/', client_webhook),
    path('webhook/receipt/', receipt_webhook),
    path('webhook/shift/', shift_webhook),
]