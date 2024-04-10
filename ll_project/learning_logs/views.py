from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Topic
from .models import Entry
from  .forms import EntryForm, TopicForm
# Create your views here.
def index(request):
    context={'rs':'主页'}
    return render(request,'learning_logs/index.html',context)

def topics(request):
    topics=Topic.objects.order_by('date_added')
    context={'topics':topics}
    return render(request,'learning_logs/topics.html',context)

def topic(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    entries=topic.entry_set.order_by('-date_added')
    context={'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)

def new_topic(request):
    if request.method !='POST':
        form=TopicForm()
    else:
        data=request.POST
        form=TopicForm(data)
        if form.is_valid():
            form.save()
            return redirect('topics')
    
    context={'form':form}

    return render(request,'learning_logs/new_topic.html',context)

def new_entry(request,topic_id):
    
    topic=Topic.objects.get(id=topic_id)
    if request.method !='POST':
        entry=Entry()        
        entry.topic=topic
        form=EntryForm(instance=entry)
    else:
        data=request.POST
        form=EntryForm(data)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            return redirect('topic',topic_id=topic_id)
    
    context={'topic':topic,'form':form}

    return render(request,'learning_logs/new_entry.html',context)

def edit_entry(request,entry_id):
    entry=Entry.objects.get(id=entry_id)
    if request.method !='POST':
        form=EntryForm(instance=entry)
    else:
        form=EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('topic',topic_id=entry.topic.id)
    context={'form':form,'entry':entry}
    return render(request,'learning_logs/edit_entry.html',context)