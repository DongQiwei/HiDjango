from django.shortcuts import render
from django.http import HttpResponse
from shop.models import USER
# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 返回列表
        user = USER.objects.filter(USERNAME=username, PASSWORD=password)
        if user:
            return HttpResponse('登陆成功')
        else:
            return HttpResponse('登录失败!')
def logout(request):
        pass