from django.shortcuts import HttpResponse, render, redirect
import pymysql
from utils import sqlUse
import logging
# 生成一个以当前文件名为名字的logger实例
logger = logging.getLogger(__name__)
# 生成一个名为collect的logger实例
collect_logger = logging.getLogger("collect")


def showFirm(request):
    root = request.GET.get('root')
    root2 = request.POST.get('root2')
    if root is None:
        root = root2
    if request.method == 'GET':
        sql = 'select * from firm;'
        firm_list = sqlUse.get_list(sql, [])
        return render(request, 'showFirm.html', {'firm_list': firm_list, 'root': root})
    else:
        typeChoose = request.POST.get('type')
        typeValue = request.POST.get('value')
        c1 = '%%' + typeValue + '%%'
        if(typeChoose == '1'):
            sql = 'select * from firm where Firmcode like %s'
            firm_list = sqlUse.get_list(sql, [c1, ])
            return render(request, 'showFirm.html', {'firm_list': firm_list, 'root': root})
        elif(typeChoose == '2'):
            sql = 'select * from firm where Firmname like %s'
            firm_list = sqlUse.get_list(sql, [c1, ])
            return render(request, 'showFirm.html', {'firm_list': firm_list, 'root': root})
        else:
            sql = 'select * from firm where Firmregion like %s'
            firm_list = sqlUse.get_list(sql, [c1, ])
            return render(request, 'showFirm.html', {'firm_list': firm_list, 'root': root})


def addFirm(request):
    root = request.GET.get('root')
    root2 = request.POST.get('root2')
    if root is None:
        root = root2
    if request.method == 'GET':
        return render(request, 'addFirm.html', {'root': root})
    else:
        Firmcode = request.POST.get('Firmcode')
        Firmname = request.POST.get('Firmname')
        Firmregion = request.POST.get('Firmregion')
        Firmadress = request.POST.get('Firmadress')
        Firmlat = request.POST.get('Firmlat')
        Firmlng = request.POST.get('Firmlng')
        Firmphone = request.POST.get('Firmphone')
        Wcode = request.POST.get('Wcode')
        sql = 'insert into firm values(%s,%s,%s,%s,%s,%s,%s,%s);'
        sqlUse.modify(sql, [Firmcode, Firmname, Firmregion, Firmadress, Firmlat, Firmlng, Firmphone, Wcode, ])
        sql = 'select * from firm;'
        firm_list = sqlUse.get_list(sql, [])
        return render(request, 'showFirm.html', {'firm_list': firm_list, 'root': root})


def editFirm(request):
    root = request.GET.get('root')
    root2 = request.POST.get('root2')
    if root is None:
        root = root2
    if request.method == 'GET':
        sql1 = 'select * from firm'
        sql2 = 'select * from firm where Firmcode=%s'
        Firmcode = request.GET.get('Firmcode')
        current_firm = sqlUse.get_one(sql2, [Firmcode, ])
        firm_list = sqlUse.get_list(sql1, [])
        return render(request, 'editFirm.html', {'firm_list': firm_list, 'current_firm': current_firm,  'root': root})
    else:
        Firmcode = request.POST.get('Firmcode')
        Firmname = request.POST.get('Firmname')
        Firmregion = request.POST.get('Firmregion')
        Firmadress = request.POST.get('Firmadress')
        Firmlat = request.POST.get('Firmlat')
        Firmlng = request.POST.get('Firmlng')
        Firmphone = request.POST.get('Firmphone')
        Wcode = request.POST.get('Wcode')
        sql = 'update firm set Firmcode=%s, Firmname=%s, Firmregion=%s, Firmadress=%s, Firmlat=%s, Firmlng=%s, Firmphone=%s, Wcode=%s where Firmcode=%s ;'
        sqlUse.modify(sql, [Firmcode, Firmname, Firmregion, Firmadress, Firmlat, Firmlng, Firmphone, Wcode, Firmcode, ])
        sql = 'select * from firm;'
        firm_list = sqlUse.get_list(sql, [])
        return render(request, 'showFirm.html', {'firm_list': firm_list, 'root': root})





def deleteFirm(request):
    root = request.GET.get('root')
    Firmcode = request.GET.get('Firmcode')
    sql = 'delete from firm where Firmcode=%s'
    sqlUse.modify(sql, [Firmcode, ])
    sql = 'select * from firm;'
    firm_list = sqlUse.get_list(sql, [])
    return render(request, 'showFirm.html', {'firm_list': firm_list, 'root': root})


