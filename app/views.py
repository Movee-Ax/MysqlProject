from django.shortcuts import HttpResponse, render, redirect
from utils import sqlUse
import logging
import hashlib

# 生成一个以当前文件名为名字的logger实例
logger = logging.getLogger(__name__)
# 生成一个名为collect的logger实例
collect_logger = logging.getLogger("collect")


def get_str_sha1_secret_str(res: str):
    """
    使用sha1加密算法，返回str加密后的字符串
    """
    sha = hashlib.sha1(res.encode('utf-8'))
    encrypts = sha.hexdigest()
    return encrypts


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        password = get_str_sha1_secret_str(password)
        not_user = '用户不存在！'
        not_password = '密码错误！'
        real_username = sqlUse.get_one('select username from userList where username = %s', [username, ])
        # 在数据库中提取用户名
        real_password = sqlUse.get_one('select password from userList where username = %s', [username, ])
        # 在数据库中提取密码
        root = sqlUse.get_one('select root from userList where username = %s', [username, ])
        if real_username is None:
            # 用户名不存在
            return render(request, 'login.html', {'not_user': not_user})
        else:
            if real_password['password'] != password:
                # 密码错误
                return render(request, 'login.html', {'not_password': not_password})
            else:
                return render(request, 'index.html', {'root': root['root']})


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        password = get_str_sha1_secret_str(password)
        exist_user = '用户已存在！'
        succeed = '创建成功！'
        root = request.POST.get('root')
        repeat_result = sqlUse.get_one('select username from userList where username = %s', [username, ])
        if repeat_result is None:
            sqlUse.modify('insert into userList values(%s,%s,%s)', [username, password, root, ])
            return render(request, 'login.html', {'succeed': succeed})
        else:
            return render(request, 'register.html', {'exist_user': exist_user})


def create(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        exist_user = '用户已存在！'
        succeed = '创建成功！'
        root = request.POST.get('root')
        root1 = request.POST.get('root2')
        repeat_result = sqlUse.get_one('select username from userList where username = %s', [username, ])
        if repeat_result is None:
            sqlUse.modify('insert into userList values(%s,%s,%s)', [username, password, root, ])
            return render(request, 'index.html', {'succeed': succeed, 'root': root1})
        else:
            return render(request, 'create.html', {'exist_user': exist_user})


def logout(request):
    logout_succeed = '退出成功！'
    if request.method == 'GET':
        return render(request, 'login.html', {'logout_succeed': logout_succeed})
