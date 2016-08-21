from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from models import User, Message, Comment
import bcrypt

def index(request):
    return render(request, 'user_dashboard/index.html')

def login(request):
    return render(request, 'user_dashboard/login.html')

def register(request):
    return render(request, 'user_dashboard/register.html')

def show(request, user_id):
    if not 'user' in request.session:
        return redirect(reverse('index'))
    user = User.manager.get(id=user_id)
    messages = Message.objects.filter(user_id_to=user_id)
    comments = Comment.objects.all()
    context = {'user':user, 'messages':messages, 'comments': comments}
    return render(request, 'user_dashboard/show.html', context)

def edit(request, user_id):
    user = User.objects.get(id = user_id)
    context = {'user':user}
    return render(request, 'user_dashboard/edit.html', context)

def dashboard(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request, 'user_dashboard/dashboard.html', context)

def register_process(request):
    result = User.manager.validateReg(request)
    resultPass = User.manager.validateRegPass(request)

    if result[0] == False or resultPass[0] == False:
        errors = result[1]+resultPass[1]
        print_messages(request, errors)
        return redirect(reverse('register'))
    pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.manager.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], pw_hash=pw_hash)
    return log_user_in(request, user)

def login_process(request):
    result = User.manager.validateLogin(request)
    if result[0] == False:
        print_messages(request, result[1])
        return redirect(reverse('login'))
    return log_user_in(request, result[1])

def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.ERROR, message)

def log_user_in(request, user):
    request.session['user'] = user.id
    user.user_level = 1
    user.save(update_fields=None)
    return redirect(reverse('show', kwargs={'user_id':request.session['user']}))

def update(request, user_id):
    result = User.manager.validateReg(request)
    if result[0] == False:
        print_messages(request, result[1])
        return redirect(reverse('edit', kwargs={'user_id':request.session['user']}))
    update = User.objects.get(id = user_id)
    update.first_name = request.POST['first_name']
    update.last_name = request.POST['last_name']
    update.email = request.POST['email']
    update.save(update_fields=None)
    return redirect(reverse('show', kwargs={'user_id':request.session['user']}))

def update_pass(request, user_id):
    result = User.manager.validateRegPass(request)
    if result[0] == False:
        print_messages(request, result[1])
        return redirect(reverse('edit', kwargs={'user_id':request.session['user']}))
    pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    update = User.objects.get(id = user_id)
    update.pw_hash = pw_hash
    update.save(update_fields=None)
    return redirect(reverse('show', kwargs={'user_id':request.session['user']}))

def logout(request):
    user = User.manager.get(id=request.session['user'])
    user.user_level = 0
    user.save(update_fields=None)
    request.session.pop('user')
    return redirect(reverse('index'))

def delete(request, user_id):
    User.manager.delete(user_id)
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
