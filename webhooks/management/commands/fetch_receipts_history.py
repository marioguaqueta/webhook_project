from django.core.management.base import BaseCommand
from webhooks.models import IncomingWebhook
import requests
from datetime import datetime, timedelta, timezone
import time

class Command(BaseCommand):
    help = "Carga histórica de recibos por intervalos de 10 minutos desde agosto 2024 hasta ahora"

    def handle(self, *args, **kwargs):
        start_time = datetime(2024, 8, 1, 0, 0, 0, tzinfo=timezone.utc)
        now = datetime.now(timezone.utc)
        step = timedelta(minutes=10)  # <-- Cambiamos a 10 minutos

        headers = {
            "Authorization": "Bearer d11e0add55c647a7a7b90ae852bcb68a"
        }

        while start_time < now:
            end_time = start_time + step

            created_at_min = start_time.isoformat(timespec='milliseconds').replace('+00:00', 'Z')
            created_at_max = end_time.isoformat(timespec='milliseconds').replace('+00:00', 'Z')

            url = f"https://api.loyverse.com/v1.0/receipts?created_at_min={created_at_min}&created_at_max={created_at_max}"

            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()
                data = response.json()
                receipts = data.get("receipts", [])

                for receipt in receipts:
                    IncomingWebhook.objects.create(payload=receipt, type="api_receipt")

                self.stdout.write(self.style.SUCCESS(f"✔ {len(receipts)} recibos guardados entre {created_at_min} y {created_at_max}"))

            except Exception as e:
                self.stderr.write(self.style.ERROR(f"❌ Error en ventana {created_at_min} - {created_at_max}: {e}"))

            time.sleep(30)  # Espera 30 segundos entre llamadas
            start_time = end_time  # Avanza a la siguiente ventana
