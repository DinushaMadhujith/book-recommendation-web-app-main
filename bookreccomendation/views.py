#from django.http import HttpResponse
from django.shortcuts import render
from django.http import FileResponse, Http404
import os

def homepage(request):
    #return HttpResponse("Hello World! I'm Home")
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("Hi this is about page")
    return render(request, 'about.html')

def visualization(request):
    #return HttpResponse("Hi this is about page")
    return render(request, 'visualization.html')

def download_visualization(request, filename):
    # Define the path to the media directory
    file_path = os.path.join('static/images', filename)

    # Check if the file exists
    if os.path.exists(file_path):
        # Serve the file as an attachment
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=filename)
        response['Content-Type'] = 'image/png'
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response
    else:
        raise Http404("File not found.")