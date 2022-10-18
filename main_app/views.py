from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import MaintenanceForm
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
    maintenance_form = MaintenanceForm()
    return render(request, 'tools/detail.html', {
        "tool" : tool,
        'maintenance_form':maintenance_form
        })

def add_maintenance(request, tool_id):
    form = MaintenanceForm(request.POST)
    # validate the form
    if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
        new_maintenance = form.save(commit=False)
        new_maintenance.tool_id = tool_id
        new_maintenance.save()
    return redirect('detail', tool_id = tool_id)

class ToolCreate(CreateView):
    model = Tool
    fields = '__all__'

class ToolUpdate(UpdateView):
    model = Tool
    fields = '__all__'

class ToolDelete(DeleteView):
    model = Tool
    success_url = '/tools/'