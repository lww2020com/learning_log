from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Topic
from .models import Entry
from .forms import EntryForm, TopicForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    context={'rs':'主页'}
    return render(request,'learning_logs/index.html',context)

@login_required
def topics(request):
    # topics=Topic.objects.order_by('date_added')
    # 只允访问用户个用的数据
    topics=Topic.objects.filter(owner=request.user).order_by('date_added')
    context={'topics':topics}
    return render(request,'learning_logs/topics.html',context)

@login_required
def topic(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    if topic.owner!=request.user:
        raise Http404
    entries=topic.entry_set.order_by('-date_added')
    context={'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)

@login_required
def new_topic(request):
    if request.method !='POST':
        form=TopicForm()
    else:
        data=request.POST
        form=TopicForm(data)
        if form.is_valid():
            new_topic=form.save(commit=False)
            new_topic.owner=request.user
            form.save()
            return redirect('learning_logs:topics')
    
    context={'form':form}

    return render(request,'learning_logs/new_topic.html',context)

@login_required
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
            return redirect('learning_logs:topic',topic_id=topic_id)
    
    context={'topic':topic,'form':form}

    return render(request,'learning_logs/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic
    if topic.owner!=request.user:
        raise Http404
    if request.method !='POST':
        form=EntryForm(instance=entry)
    else:
        form=EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic',topic_id=entry.topic.id)
    context={'form':form,'entry':entry}
    return render(request,'learning_logs/edit_entry.html',context)