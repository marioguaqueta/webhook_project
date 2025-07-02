from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import IncomingWebhook
import json

@csrf_exempt
def receive_webhook(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            IncomingWebhook.objects.create(payload=data, type_request='inventario')
            return JsonResponse({"status": "ok"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"message": "Only POST allowed"}, status=405)


@csrf_exempt
def article_webhook(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            IncomingWebhook.objects.create(payload=data, type_request='articulo')
            return JsonResponse({"status": "ok"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"message": "Only POST allowed"}, status=405)

@csrf_exempt
def client_webhook(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            IncomingWebhook.objects.create(payload=data, type_request='cliente')
            return JsonResponse({"status": "ok"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"message": "Only POST allowed"}, status=405)


@csrf_exempt
def receipt_webhook(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            IncomingWebhook.objects.create(payload=data, type_request='recibo')
            return JsonResponse({"status": "ok"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"message": "Only POST allowed"}, status=405)


@csrf_exempt
def shift_webhook(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            IncomingWebhook.objects.create(payload=data, type_request='turno')
            return JsonResponse({"status": "ok"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"message": "Only POST allowed"}, status=405)