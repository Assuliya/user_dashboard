from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from models import User, Message, Comment

def index(request):
    return render(request, 'user_dashboard/index.html')

def login(request):
    return render(request, 'user_dashboard/login.html')

def register(request):
    return render(request, 'user_dashboard/register.html')

def edit(request, user_id):
    return render(request, 'user_dashboard/edit.html')

def dashboard(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request, 'user_dashboard/dashboard.html', context)





def register_process(request):
    result = User.manager.validateReg(request)
    if result[0] == False:
        print_messages(request, result[1])
        return redirect(reverse('register'))
    return log_user_in(request, result[1])

def login_process(request):
    result = User.manager.validateLogin(request)
    if result[0] == False:
        print_messages(request, result[1])
        return redirect(reverse('login'))
    return log_user_in(request, result[1])

def log_user_in(request, user):
    request.session['user'] = user.id
    return redirect(reverse('show', kwargs={'user_id':request.session['user']}))

def show(request, user_id):
    if not 'user' in request.session:
        return redirect(reverse('index'))
    user = User.manager.get(id=user_id)
    messages = Message.objects.filter(user_id_to=user_id)
    comments = Comment.objects.all()

    context = {'user':user, 'messages':messages, 'comments': comments}

    return render(request, 'user_dashboard/show.html', context)

def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.ERROR, message)

def logout(request):
    request.session.pop('user')
    return redirect(reverse('index'))

def delete(request, user_id):
    User.objects.delete(user_id)
    request.session.pop('user')
    return redirect('/')



def add_message(request, page_id):
    if request.method == "POST":
        user = User.objects.get(id=request.session['user'])
        page = User.objects.get(id=page_id)
        Message.objects.create(message = request.POST['message'], user_id = user, user_id_to = page)
        return redirect(reverse('show', kwargs={'user_id':page_id}))
    else:
	    return redirect(reverse('show'))

def add_comment(request, message_id):
    if request.method == "POST":
        user = User.objects.get(id=request.session['user'])
        message = Message.objects.get(id=message_id)
        page = message.user_id_to.id
        Comment.objects.create(comment = request.POST['comment'], user_id = user, message_id = message)
        return redirect(reverse('show', kwargs={'user_id':page}))
    else:
	    return redirect(reverse('show'))
