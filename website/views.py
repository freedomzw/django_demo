from django.shortcuts import render, redirect
from django.http import HttpResponse
from website import models


def login(request):
    """登录验证"""
    # 定义空的错误提示
    err_msg = ''
    print(request.method)
    print(request.path)
    print(request.path_info)
    # 判断请求的方法是POST
    if request.method == 'POST':
        print(request.POST, type(request.POST))  # <QueryDict: {'user': ['root'], 'pwd': ['123']}>字典
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        if user == 'root' and pwd == '123':
            # 重定向 return redirect('https://xxxxx')
            return redirect('/website/articles/index/')
            # return redirect('https://www.baidu.com')

        elif models.User.objects.filter(name=user, password=pwd):
            return redirect('/website/articles/index/')
        else:
            err_msg = "用户名或者密码错误!!!!"

    return render(request, 'login.html', {'err_msg': err_msg})


def index(request):
    print(request.path)
    return HttpResponse("欢迎来到我的地盘")


def publisher_list(request):
    # 查询一张表的所有的记录
    publishers = models.Publisher.objects.all()


    for i in publishers:
        print(i.name, i.id, i.pk)

    return render(request, 'publisher_list.html', {'pub': publishers})


def add_publisher(request):
    if request.method == 'POST':
        pub_name = request.POST.get('pub_name')
        ret = models.Publisher.objects.create(name=pub_name)
        return redirect('/website/articles/publisher_list/')
    return render(request, 'add_publisher.html')


def del_publisher(request):
    """删除出版社"""

    # 从URL上获取删除的id
    print(request.GET)
    del_id = request.GET.get('id')
    models.Publisher.objects.filter(id=del_id).delete()

    return redirect('/website/articles/publisher_list/')


def edit_publisher(request):
    # 从浏览器中请求url的id获取到<QueryDict: {'id': ['14']}>
    edit_id = request.GET.get('id')
    obj = models.Publisher.objects.get(id=edit_id)
    print(obj, type(obj))

    if request.method == "POST":
        pub_name = request.POST.get('pub_name')

        obj.name = pub_name
        obj.save()

        return redirect('/website/articles/publisher_list/')
    return render(request, 'edit_publisher.html', {'obj': obj})
