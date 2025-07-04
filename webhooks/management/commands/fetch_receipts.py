from django.core.management.base import BaseCommand
from webhooks.models import IncomingWebhook
import requests
from datetime import datetime, timedelta, timezone

class Command(BaseCommand):
    help = "Fetch recent receipts (last 5 minutes) from Loyverse API and save them individually as IncomingWebhook objects"

    def handle(self, *args, **kwargs):
        now = datetime.now(timezone.utc)
        start_time = now - timedelta(minutes=5)
        end_time = now

        created_at_min = start_time.isoformat(timespec='milliseconds').replace('+00:00', 'Z')
        created_at_max = end_time.isoformat(timespec='milliseconds').replace('+00:00', 'Z')

        url = f"https://api.loyverse.com/v1.0/receipts?created_at_min={created_at_min}&created_at_max={created_at_max}"
        headers = {
            "Authorization": "Bearer d11e0add55c647a7a7b90ae852bcb68a"
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()

            receipts = data.get("receipts", [])
            if not receipts:
                self.stdout.write(self.style.WARNING("⚠ No receipts found in this 5-minute window."))

            for receipt in receipts:
                IncomingWebhook.objects.create(payload=receipt, type="api_receipt")

            self.stdout.write(self.style.SUCCESS(f"✔ {len(receipts)} receipts saved from {start_time} to {end_time}"))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"❌ Error fetching receipts: {e}"))
