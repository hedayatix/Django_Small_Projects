# Needed imports here
from .models import *
from django.http import HttpResponse

def list_create_tasks(request):
    if request.method == 'GET':
        # tsk = Task.objects.all().order_by('name')
        # rsp = []
        # for t in tsk:
        #     rsp.append(f'{t}\n')
        # return HttpResponse(rsp, content_type="text/plain")
        return HttpResponse('\n'.join(Task.objects.all().order_by('name').values_list('name', flat=True)))



def count_tasks(request):
    if request.method == 'GET':
        cnt = Task.objects.count()

        return HttpResponse(f'You have \'{cnt}\' tasks to do')
