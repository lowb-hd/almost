from django.shortcuts import render
from .models import Topic,UserInfo
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .forms import TopicForm,EntryForm
import json
from django.views.decorators.csrf import csrf_exempt






# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    '''显示所有主题'''
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,  'learning_logs/topics.html', context)

def topic(request, topic_id):
    '''显示单个主题及其所有条目'''
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
    # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据,对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request,topic_id):
    """添加新条目"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
    # 未提交数据：创建一个新表单
        form = EntryForm()
    else:
        # POST提交的数据,对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

#新增用户
@csrf_exempt
def add_user(request):
    if request.method == "POST":
        req = json.loads(request.body)
        print(req)
        user_id = req["user_id"]
        user_name = req["user_name"]
        password = req["password"]
        status = req["status"]
        user_exist = UserInfo.objects.filter(user_id=user_id)
        if len(user_exist) != 0:
            return JsonResponse({"status": "BS.400", "msg": "user aleady exist,fail to publish."})
        add_art = UserInfo(user_id=user_id, user_name=user_name,password=password, status="1")
        add_art.save()
        return 'add user success'




