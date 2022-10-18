from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Tool


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

def tools_index(request):
    tools = Tool.objects.all()
    return render(request, "tools/index.html", {"tools": tools})

def tools_detail(request, tool_id):
    tool = Tool.objects.get(id=tool_id)
    return render(request, 'tools/detail.html', {"tool" : tool})

class ToolCreate(CreateView):
    model = Tool
    fields = '__all__'

class ToolUpdate(UpdateView):
    model = Tool
    fields = '__all__'

class ToolDelete(DeleteView):
    model = Tool
    success_url = '/tools/'