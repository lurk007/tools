from django.shortcuts import render, redirect
from .models import User
from django.db import models
from django.http import HttpResponse
from dic_generator.dic_tools import encode_md5, encode_base64, random_str


# Create your views here.
def add(request):
    user = User()
    user.password = encode_md5('llnh990713')
    user.login_name = encode_base64('lurk007')
    user.email = encode_base64('758286797@qq.com')
    user.phone = encode_base64('13145151101')
    user.power = '1'
    user.save()
    return HttpResponse('执行成功')


def get(request):
    li = User.objects.filter()
    for i in li:
        print(i)
    return HttpResponse(li)


def index(request):
    """"""
    login_name = request.session.get('login_name')
    if login_name is None:
        return redirect('shop:login')
    else:
        print(login_name)
        return render(request, 'shop/index.html')


def check_login(request):
    """"""
    login_name = request.POST.get('login_name')
    password = request.POST.get('password')
    user = User.objects.get(login_name=encode_base64(login_name))
    print(user)
    if user.password == encode_md5(password):
        request.session['login_name'] = user.login_name
        request.session['password'] = user.password
        request.session['phone'] = user.phone
        request.session['email'] = user.email
        request.session['power'] = user.power
        request.COOKIES = {'sessionid': request.session.session_key}
        print('login_name:', request.session.get('login_name'))
        return render(request, 'shop/index.html')
    else:
        print('登录失败')
        return redirect('shop:login')


def login(request):
    return render(request, 'shop/login.html')
