from django.shortcuts import render, redirect
from .forms import TopicForm

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
    #This is how you interact with the database
    
    #When building a page that uses data, we pass the context variable to render()
    # as well as the request object and the path to the template
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    #Like ini  MyShell.py
    topic = Topic.objects.get(id=topic_id)
    #Foreign key can be accessed using '_set'
    entries = topic.entry_set.order_by('date_added') # -date_added is in descending order
    context = {'topic':topic, 'entries':entries}
    
    return render(request, 'learning_logs/topic.html',context)

def new_topic(request):
    if request.method != 'POST':
        # No data submitted; create a blank form (create an instance of TopicForm)
        # Because we included no arguments when instantiating TopicForm, Django
        # creates a blank form that the user can fill out.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        # We make an instance of TopicForm and pass it the data entered by the user,
        # stored in request.POST.
        form = TopicForm(data=request.POST)
        #The is_valid() method checks that all required fields have been filled
        # in (all fields in a form are required by default) and that the data entered
        # matches the field types expected.
        if form.is_valid():
            #write the data from the form to the database
            form.save()
            #redirect the user's browser to the topics page
            return redirect('learning_logs:topics')
        
    # Display a blank form using the new_topic.html template
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html',context)
        