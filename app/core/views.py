import os
from django.http import JsonResponse


def home(request):
    """Root endpoint — simple proof-of-life response."""
    return JsonResponse({
        "message": "Production-style DevOps demo app is running",
        "environment": os.environ.get("APP_ENV", "development"),
    })


def health(request):
    """
    Health check endpoint.
    Kept dependency-free on purpose so it's fast and reliable —
    this is what Kubernetes liveness/readiness probes will hit.
    """
    return JsonResponse({"status": "healthy"})


def readiness(request):
    """
    Readiness check — in a real app this would verify DB/cache
    connectivity. Kept simple here since the app has no DB dependency,
    but the endpoint exists so the K8s readinessProbe has a distinct
    target from the liveness probe.
    """
    return JsonResponse({"status": "ready"})
