# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("Welcome to emobilis")

def about(request):
    return HttpResponse("About emobilis")