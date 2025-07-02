
class IncomingWebhook(models.Model):
    received_at = models.DateTimeField(auto_now_add=True)
    payload = models.JSONField()

    def __str__(self):
        return f"Webhook at {self.received_at}"
