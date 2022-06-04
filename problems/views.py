from django.shortcuts import render
from problems.models import Problems

# Create your views here.


def problems(request):
    context = {
        'problems': Problems.objects.all()
    }
    return render(request, 'problems.html', context=context)


def problemDetail(request, pk):
    context = {
        'problem': Problems.objects.get(id = pk)
    }
    return render(request, 'problem.html', context=context)


def groups(request):
    return render(request, 'group.html')