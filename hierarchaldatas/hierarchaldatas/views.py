from django.views import View
from django.shortcuts import render
from hierarchaldatas import models
def show_files(request):
    html = "files.html"
    files = models.File.objects.all()
    return render(request, html, {'files': files})