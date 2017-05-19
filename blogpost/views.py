from django.shortcuts import render

def post_list(request):
    return render(request, 'blogpost/post_list.html', {})
