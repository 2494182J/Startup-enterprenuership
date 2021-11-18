#views is define the web page function
from django.shortcuts import render 
#这个函数作为输入用户的请求、模板文件名和上下文字典。
from django.http import HttpResponse 
def index(request):
    return HttpResponse("this is idea roast project")
