from django.shortcuts import render


# Create your views here.

about_us=[
    {'id':1, 'name': 'jeevan'},
    {'id':12, 'name': 'isaac'},
]

def home(request):
    context =  {'about_us':about_us}
    return render(request,'sportsapp/home.html', context)


def about_us(request,pk):
    
    return render(request,'sportsapp/about_us.html')

