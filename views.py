from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'user.html')

def dashboard(request):
    return render(request, 'vote_participate.html')

def vote(request):
    return render(request, 'vote_page.html')

def participate(request):
    return render(request, 'participate_page.html')

def profile(request):
    return render(request, 'profile.html')

def forgotpassword(request):
    return render(request, 'reset_password.html')

def register(request):
    return render(request, 'registration.html')

def adminpage(request):
    return render(request, 'admin.html')

def createpage(request):
    return render(request, 'create_manage.html')

def create(request):
    return render(request, 'create_contest.html')

def manage(request):
    return render(request, 'manage_contest.html')
