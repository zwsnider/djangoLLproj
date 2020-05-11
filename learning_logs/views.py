from django.shortcuts import render

# Create your views here.

# When a URL request matches the pattern we just defined,
# Django looks for a function called index() in the views.py file.

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

from .models import Topic

def topics(request):
    topics = Topic.objects.order_by('date_added')
    #A context is a dictionary in which the keys are names we'll use
    # in the template to access the data, and the values are the data
    # we need to send to the template. In this case there's only one key-value pair,
    # which contains the set of topics we'll display on the page.
    context = {'topics':topics}
    #When building a page that uses data, we pass the context variable to render()
    # as well as the request object and the path to the template
    return render(request, 'learning_logs/topics.html', context)
