from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import MaintenanceForm
from .models import Maintenance, Storage, Tool


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
    storage_tools_dont_have = Storage.objects.exclude(id__in = tool.storages.all().values_list('id'))

    return render(
        request,
        "tools/detail.html",
        {
            "tool": tool, 
            "maintenance_form": maintenance_form,
            'storages' : storage_tools_dont_have,
            })


def add_maintenance(request, tool_id):
    form = MaintenanceForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the tool_id assigned
        new_maintenance = form.save(commit=False)
        new_maintenance.tool_id = tool_id
        new_maintenance.save()
    return redirect("detail", tool_id=tool_id)

def assoc_storage(request, tool_id, storage_id):
  # Note that you can pass a tool's id instead of the whole object
   Tool.objects.get(id=tool_id).storages.add(storage_id)
   return redirect('detail', tool_id=tool_id)


class ToolCreate(CreateView):
    model = Tool
    fields = ['name','description']
    success_url = '/tools/'


class ToolUpdate(UpdateView):
    model = Tool
    fields = ['name','description']


class ToolDelete(DeleteView):
    model = Tool
    success_url = "/tools/"

class StorageCreate(CreateView):
    model = Storage
    fields = ['name', 'description']

class StorageUpdate(UpdateView):
    model = Storage
    fields = ['name', 'description']

class StorageDelete(DeleteView):
    model = Storage
    success_url = '/storages/'

class StorageDetail(DetailView):
    model = Storage
    template_name = 'storages/detail.html'

class StorageList(ListView):
    model = Storage
    template_name = 'storages/index.html'