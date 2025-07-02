from django.db import models

class IncomingWebhook(models.Model):
    received_at = models.DateTimeField(auto_now_add=True)
    payload = models.JSONField()
    type_request = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"Webhook at {self.received_at}"
