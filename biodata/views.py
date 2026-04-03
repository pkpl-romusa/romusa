from django.shortcuts import render
from django.http import HttpResponse
from accounts.utils import check_is_group_member

def index(request):
    
    is_group_member = check_is_group_member(request.user)
            
    context = {
        'is_group_member': is_group_member,
    }
    
    return render(request, 'index.html', context)