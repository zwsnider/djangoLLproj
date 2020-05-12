from django.shortcuts import render, redirect
from .forms import TopicForm, EntryForm

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

def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        
        if form.is_valid():
            # When we call save(), we include the argument commit=False to tell Django to create
            # a new entry object and assign it to new_entry without saving it to the database yet.
            new_entry = form.save(commit=False)
            #Need to assign the topic of the new entry based on the topic we pulled from topic_id
            new_entry.topic = topic
            new_entry.save()
            form.save()
            return redirect('learning_logs:topic',topic_id=topic_id)
        
    context = {'form': form, 'topic': topic}
    return render(request, 'learning_logs/new_entry.html', context)
            