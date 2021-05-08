from django.shortcuts import HttpResponse, render, redirect
import pymysql
from utils import sqlUse
import logging
# 生成一个以当前文件名为名字的logger实例
logger = logging.getLogger(__name__)
# 生成一个名为collect的logger实例
collect_logger = logging.getLogger("collect")

def showMedicine(request):
    root = request.GET.get('root')
    root2 = request.POST.get('root2')
    if root is None:
        root = root2
    print(root)
    if request.method == 'GET':
        # sql = 'select * from medicine;'
        sql = 'SELECT * FROM medicine INNER JOIN belong on medicine.Mname = belong.Mname AND medicine.Mlot = belong.Mlot AND medicine.Firmcode = belong.Firmcode;'
        medicine_list = sqlUse.get_list(sql, [])
        return render(request, 'showMedicine.html', {'medicine_list': medicine_list, 'root': root})
    else:
        typeChoose = request.POST.get('type')
        typeValue = request.POST.get('value')
        c1 = '%%'+typeValue+'%%'
        if(typeChoose == '1'):
            sql = 'SELECT * FROM medicine INNER JOIN belong on medicine.Mname = belong.Mname AND medicine.Mlot = belong.Mlot AND medicine.Firmcode = belong.Firmcode where belong.Mname like %s'
            medicine_list = sqlUse.get_list(sql, [c1, ])
            return render(request, 'showMedicine.html', {'medicine_list': medicine_list, 'root': root})
        elif(typeChoose == '2'):
            sql = 'SELECT * FROM medicine INNER JOIN belong on medicine.Mname = belong.Mname AND medicine.Mlot = belong.Mlot AND medicine.Firmcode = belong.Firmcode where belong.Mlot like %s'
            medicine_list = sqlUse.get_list(sql, [c1, ])
            return render(request, 'showMedicine.html', {'medicine_list': medicine_list, 'root': root})
        elif (typeChoose == '3'):
            sql = 'SELECT * FROM medicine INNER JOIN belong on medicine.Mname = belong.Mname AND medicine.Mlot = belong.Mlot AND medicine.Firmcode = belong.Firmcode where belong.Firmcode like %s'
            medicine_list = sqlUse.get_list(sql, [c1, ])
            return render(request, 'showMedicine.html', {'medicine_list': medicine_list, 'root': root})
        else:
            sql = 'SELECT * FROM medicine INNER JOIN belong on medicine.Mname = belong.Mname AND medicine.Mlot = belong.Mlot AND medicine.Firmcode = belong.Firmcode where belong.Belongcode like %s'
            medicine_list = sqlUse.get_list(sql, [c1, ])
            return render(request, 'showMedicine.html', {'medicine_list': medicine_list, 'root': root})


def addMedicine(request):
    root = request.GET.get('root')
    root2 = request.POST.get('root2')
    if root is None:
        root = root2
    if request.method == 'GET':
        return render(request, 'addMedicine.html', {'root': root})
    else:
        Mname = request.POST.get('Mname')
        Mlot = request.POST.get('Mlot')
        Firmcode = request.POST.get('Firmcode')
        Mmoney = request.POST.get('Mmoney')
        Mcount = request.POST.get('Mcount')
        Cdate = request.POST.get('Cdate')
        Sdate = request.POST.get('Sdate')
        Belongcode = request.POST.get('Belongcode')
        Belongnum = request.POST.get('Belongnum')
        sql = 'insert into medicine values(%s,%s,%s,%s,%s,%s,%s);'
        sqlUse.modify(sql, [Mname, Mlot, Firmcode, Mmoney, Mcount, Cdate, Sdate, ])
        sql = 'insert into belong values(%s, %s, %s, %s, %s);'
        sqlUse.modify(sql, [Mname, Mlot, Firmcode, Belongcode, Belongnum, ])
        sql = 'SELECT * FROM medicine INNER JOIN belong on medicine.Mname = belong.Mname AND medicine.Mlot = belong.Mlot AND medicine.Firmcode = belong.Firmcode;'
        medicine_list = sqlUse.get_list(sql, [])
        return render(request, 'showMedicine.html', {'medicine_list': medicine_list, 'root': root})


def editMedicine(request):
    root = request.GET.get('root')
    root2 = request.POST.get('root2')
    if root is None:
        root = root2
    if request.method == 'GET':
        sql1 = 'SELECT * FROM medicine INNER JOIN belong on medicine.Mname = belong.Mname AND medicine.Mlot = belong.Mlot AND medicine.Firmcode = belong.Firmcode;'
        sql2 = 'SELECT * FROM medicine INNER JOIN belong on medicine.Mname = belong.Mname AND medicine.Mlot = belong.Mlot AND medicine.Firmcode = belong.Firmcode where belong.Mname=%s and belong.Mlot=%s and belong.Firmcode=%s and belong.Belongcode=%s;'
        Mname = request.GET.get('Mname')
        Mlot = request.GET.get('Mlot')
        Belongcode = request.GET.get('Belongcode')
        Firmcode = request.GET.get('Firmcode')
        current_medicine = sqlUse.get_one(sql2, [Mname, Mlot, Firmcode, Belongcode, ])
        medicine_list = sqlUse.get_list(sql1, [])
        return render(request, 'editMedicine.html', {'medicine_list': medicine_list, 'current_medicine': current_medicine, 'root': root})
    else:
        Mname = request.POST.get('Mname')
        Mlot = request.POST.get('Mlot')
        Firmcode = request.POST.get('Firmcode')
        Mmoney = request.POST.get('Mmoney')
        Mcount = request.POST.get('Mcount')
        Cdate = request.POST.get('Cdate')
        Sdate = request.POST.get('Sdate')
        Belongcode = request.POST.get('Belongcode')
        Belongnum = request.POST.get('Belongnum')
        sql = 'update medicine set Mname=%s, Mlot=%s, Firmcode=%s, Mmoney=%s, Mcount=%s, Cdate=%s, Sdate=%s ' \
              'where Mname=%s and Mlot=%s and Firmcode=%s; '
        sqlUse.modify(sql, [Mname, Mlot, Firmcode, Mmoney, Mcount, Cdate, Sdate, Mname, Mlot, Firmcode, ])
        sql = 'update belong set Mname=%s, Mlot=%s, Firmcode=%s, Belongcode=%s, Belongnum=%s where Mname=%s and Mlot=%s and Firmcode=%s and Belongcode=%s;'
        sqlUse.modify(sql, [Mname, Mlot, Firmcode, Belongcode, Belongnum, Mname, Mlot, Firmcode, Belongcode, ])
        sql = 'SELECT * FROM medicine INNER JOIN belong on medicine.Mname = belong.Mname AND medicine.Mlot = belong.Mlot AND medicine.Firmcode = belong.Firmcode;'
        medicine_list = sqlUse.get_list(sql, [])
        return render(request, 'showMedicine.html', {'medicine_list': medicine_list, 'root': root})


def deleteMedicine(request):
    root = request.GET.get('root')
    Mname = request.GET.get('Mname')
    Mlot = request.GET.get('Mlot')
    Belongcode = request.GET.get('Belongcode')
    Firmcode = request.GET.get('Firmcode')
    sql = 'delete from medicine where Mname=%s and Mlot=%s and Firmcode=%s;'
    sqlUse.modify(sql, [Mname, Mlot, Firmcode, ])
    sql = 'delete from belong where Mname=%s and Mlot=%s and Firmcode=%s and Belongcode=%s;'
    sqlUse.modify(sql, [Mname, Mlot, Firmcode, Belongcode, ])
    sql = 'SELECT * FROM medicine INNER JOIN belong on medicine.Mname = belong.Mname AND medicine.Mlot = belong.Mlot AND medicine.Firmcode = belong.Firmcode;'
    medicine_list = sqlUse.get_list(sql, [])
    return render(request, 'showMedicine.html', {'medicine_list': medicine_list, 'root': root})
