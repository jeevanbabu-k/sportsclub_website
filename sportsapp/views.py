from django.shortcuts import render


# Create your views here.

users=[
    {'id':1, 'name': 'jeevan'},
    {'id':12, 'name': 'isaac'},
]

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    return render(request, 'sportsapp/login_register.html')


def home(request):
    context =  {'about_us':about_us}
    return render(request,'sportsapp/home.html', context)


def about_us(request,pk):
    return render(request,'sportsapp/about_us.html')

