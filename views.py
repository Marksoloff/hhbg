from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')
# The above code directs user to templates/index.html as the default HOME page!

def roll(request):
    return render(request, 'roll.html')


#    return HttpResponse(
#        '<a href="{% url roll %}">HTTP RESPONSE Click Roll Link</a>')


#def firstLink(request):
#    return render(request, 'firstLink.html')



    #return HttpResponse(
    #    "<a href='{% url firstLink %}'>HTTP RESPONSE Navigate to First Link Page</a>"
    #    "<h1>Roll</h1>")
