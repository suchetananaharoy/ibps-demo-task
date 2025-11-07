from django.http import HttpResponse, JsonResponse

def home(request):
    return HttpResponse("<h1>Welcome to the IBPS Job Portal API</h1><p>Server is running successfully.</p>")

def list_jobs(request):
    data = {
        "jobs": [
            {"title": "IBPS PO 2025", "status": "Active"},
            {"title": "IBPS RRB Clerk 2025", "status": "Closed"},
        ]
    }
    return JsonResponse(data)
