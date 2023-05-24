from django.shortcuts import render


def index(request):
    context = {
        'title': 'Flight Dashboard',
        'alerts': ['This is a test alert'],
        'flights': [f'Flight {i + 1}' for i in range(5)]
    }
    return render(request, 'dashboard/index.html', context)
