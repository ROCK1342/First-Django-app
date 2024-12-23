from django.shortcuts import render

def index(request):
    return render(request, 'nice/index.html')  # Ensure this points to the correct template
