from django.http import HttpResponse

def home(request):
    return HttpResponse("Kyle says Hello!")  # Warm welcome message