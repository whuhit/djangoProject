from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import time
import json


def index(request):
    # 获取请求方法
    method = request.method
    if method == "GET":
        return HttpResponse(f"Welcome to visit!")
    elif method == "POST":

        # 获取json数据
        json_data = request.body

        # 获取表单数据
        form_data = request.POST
        # 获取文件
        file_obj = request.FILES

        print('json_data', json_data)
        print('form_data', form_data)
        print('file_obj', file_obj)

        return HttpResponse(f"Hello, world. You're at the polls index")


def index2(request):
    id_ = request.POST.get('id', 0)
    time.sleep(3)
    return HttpResponse(f"You're at the polls index2 {id_}")