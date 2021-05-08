from django.shortcuts import HttpResponse, render, redirect
import pymysql
from utils import sqlUse
import logging
# 生成一个以当前文件名为名字的logger实例
logger = logging.getLogger(__name__)
# 生成一个名为collect的logger实例
collect_logger = logging.getLogger("collect")

def showWorker(request):
    root = request.GET.get('root')
    root2 = request.POST.get('root2')
    if root is None:
        root = root2
    if request.method == 'GET':
        sql = 'select * from worker;'
        worker_list = sqlUse.get_list(sql, [])
        return render(request, 'showWorker.html', {'worker_list': worker_list, 'root': root})
    else:
        typeChoose = request.POST.get('type')
        typeValue = request.POST.get('value')
        c1 = '%%' + typeValue + '%%'
        if (typeChoose == '1'):
            sql = 'select * from worker where Wcode like %s'
            worker_list = sqlUse.get_list(sql, [c1, ])
            return render(request, 'showWorker.html', {'worker_list': worker_list, 'root': root})
        elif (typeChoose == '2'):
            sql = 'select * from worker where Wname like %s'
            worker_list = sqlUse.get_list(sql, [c1, ])
            return render(request, 'showWorker.html', {'worker_list': worker_list, 'root': root})
        else:
            sql = 'select * from worker where Wposition like %s'
            worker_list = sqlUse.get_list(sql, [c1, ])
            return render(request, 'showWorker.html', {'worker_list': worker_list, 'root': root})


def addWorker(request):
    root = request.GET.get('root')
    root2 = request.POST.get('root2')
    if root is None:
        root = root2
    if request.method == 'GET':
        return render(request, 'addWorker.html', {'root': root})
    else:
        Wcode = request.POST.get('Wcode')
        Wname = request.POST.get('Wname')
        Wsex = request.POST.get('Wsex')
        Wage = request.POST.get('Wage')
        Wposition = request.POST.get('Wposition')
        Wphone = request.POST.get('Wphone')
        sql = 'insert into worker values(%s,%s,%s,%s,%s,%s);'
        sqlUse.modify(sql, [Wcode, Wname, Wsex, Wage, Wposition, Wphone, ])
        sql = 'select * from worker;'
        worker_list = sqlUse.get_list(sql, [])
        return render(request, 'showWorker.html', {'worker_list': worker_list, 'root': root})


def editWorker(request):
    root = request.GET.get('root')
    root2 = request.POST.get('root2')
    if root is None:
        root = root2
    if request.method == 'GET':
        sql1 = 'select * from worker'
        sql2 = 'select * from worker where Wcode=%s'
        Wcode = request.GET.get('Wcode')
        current_worker = sqlUse.get_one(sql2, [Wcode, ])
        worker_list = sqlUse.get_list(sql1, [])
        return render(request, 'editWorker.html', {'worker_list': worker_list, 'current_worker': current_worker, 'root': root})
    else:
        Wcode = request.POST.get('Wcode')
        Wname = request.POST.get('Wname')
        Wsex = request.POST.get('Wsex')
        Wage = request.POST.get('Wage')
        Wposition = request.POST.get('Wposition')
        Wphone = request.POST.get('Wphone')
        sql = 'update worker set Wcode=%s, Wname=%s, Wsex=%s, Wage=%s, Wposition=%s, Wphone=%s where Wcode=%s ;'
        sqlUse.modify(sql, [Wcode, Wname, Wsex, Wage, Wposition, Wphone, Wcode, ])
        sql = 'select * from worker;'
        worker_list = sqlUse.get_list(sql, [])
        return render(request, 'showWorker.html', {'worker_list': worker_list, 'root': root})


def deleteWorker(request):
    root = request.GET.get('root')
    Wcode = request.GET.get('Wcode')
    sql = 'delete from worker where Wcode=%s'
    sqlUse.modify(sql, [Wcode, ])
    sql = 'select * from worker;'
    worker_list = sqlUse.get_list(sql, [])
    return render(request, 'showWorker.html', {'worker_list': worker_list, 'root': root})


