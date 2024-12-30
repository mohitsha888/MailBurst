# apps/core/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    context = {
        'campaigns': [
            {'name': 'Welcome Series', 'date': '2024-01-01'},
            {'name': 'Newsletter', 'date': '2024-01-15'},
        ],
        'scheduled_emails': [
            {'subject': 'Weekly Update', 'schedule_time': '2024-02-01 10:00'},
            {'subject': 'Monthly Newsletter', 'schedule_time': '2024-02-15 09:00'},
        ]
    }
    return render(request, 'core/index.html', context)