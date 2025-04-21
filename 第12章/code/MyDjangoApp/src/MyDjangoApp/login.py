from django.shortcuts import render

def enterLoginPage(request):
    return render(request, 'login.html')
    
def loginAction(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    if username == 'Django' and password == 'Python':
        return render(request, 'welcome.html', {
            'username': username
        })
    else:
        return render(request, 'login.html')    