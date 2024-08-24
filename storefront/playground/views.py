from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    #pull data from db
    #transofrm  data
    #send email
    print("say_hello view function called!")
    return render(request, 'hello.html', {'name': 'Pasan'})



















# Create your views here.
# view function
# request -> response
# request handler
# action - view