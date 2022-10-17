from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


class Tool:  # Note that parens are optional if not inheriting from another class
    def __init__(self, name, description):
        self.name = name
        self.description = description


tools = [
    Tool("hammer", "used for hitting nails"),
    Tool("screwdriver", "used for tightening/loosening screws"),
    Tool("wrench", "used for tightening/loosening hex nuts"),
    Tool("pliers", "used for grasping things"),
]


def tools_index(request):
    return render(request, "tools/index.html", {"tools": tools})
