from django.shortcuts import render
from .models import History

def history_list(request):
    model = History
    template_name = 'history.html'
    context_object_name = 'all-history'
    history = History.objects.all().order_by('-date')
    return render(request, 'history.html', {'history': history})