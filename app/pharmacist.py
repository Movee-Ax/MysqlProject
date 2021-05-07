from django.shortcuts import HttpResponse, render, redirect
import pymysql
from utils import sqlUse
import logging
# 生成一个以当前文件名为名字的logger实例
logger = logging.getLogger(__name__)
# 生成一个名为collect的logger实例
collect_logger = logging.getLogger("collect")

def showPharmacist(request):
    root = request.GET.get('root')
    root2 = request.POST.get('root2')
    if root is None:
        root = root2
    if request.method == 'GET':
        sql = 'select * from pharmacist;'
        pharmacist_list = sqlUse.get_list(sql, [])
        return render(request, 'showPharmacist.html', {'pharmacist_list': pharmacist_list, 'root': root})
    else:
        typeChoose = request.POST.get('type')
        typeValue = request.POST.get('value')
        c1 = '%%' + typeValue + '%%'
        if (typeChoose == '1'):
            sql = 'select * from pharmacist where Phcode like %s'
            pharmacist_list = sqlUse.get_list(sql, [c1, ])
            return render(request, 'showPharmacist.html', {'pharmacist_list': pharmacist_list, 'root': root})
        elif (typeChoose == '2'):
            sql = 'select * from pharmacist where Phname like %s'
            pharmacist_list = sqlUse.get_list(sql, [c1, ])
            return render(request, 'showPharmacist.html', {'pharmacist_list': pharmacist_list, 'root': root})
        elif (typeChoose == '3'):
            sql = 'select * from pharmacist where Phtitle like %s'
            pharmacist_list = sqlUse.get_list(sql, [c1, ])
            return render(request, 'showPharmacist.html', {'pharmacist_list': pharmacist_list, 'root': root})
        elif (typeChoose == '4'):
            sql = 'select * from pharmacist where Shopcode like %s'
            pharmacist_list = sqlUse.get_list(sql, [c1, ])
            return render(request, 'showPharmacist.html', {'pharmacist_list': pharmacist_list, 'root': root})
        else:
            sql = 'select * from pharmacist where Phcor like %s'
            pharmacist_list = sqlUse.get_list(sql, [c1, ])
            return render(request, 'showPharmacist.html', {'pharmacist_list': pharmacist_list, 'root': root})
        


def addPharmacist(request):
    root = request.GET.get('root')
    root2 = request.POST.get('root2')
    if root is None:
        root = root2
    if request.method == 'GET':
        return render(request, 'addPharmacist.html', {'root': root})
    else:
        Phcode = request.POST.get('Phcode')
        Phname = request.POST.get('Phname')
        Phsex = request.POST.get('Phsex')
        Phage = request.POST.get('Phage')
        Phtitle = request.POST.get('Phtitle')
        Shopcode = request.POST.get('Shopcode')
        Phphone = request.POST.get('Phphone')
        Phcor = request.POST.get('Phcor')
        sql = 'insert into pharmacist values(%s,%s,%s,%s,%s,%s,%s,%s);'
        sqlUse.modify(sql, [Phcode, Phname, Phsex, Phage, Phtitle, Shopcode, Phphone, Phcor, ])
        sql = 'select * from pharmacist;'
        pharmacist_list = sqlUse.get_list(sql, [])
        return render(request, 'showPharmacist.html', {'pharmacist_list': pharmacist_list, 'root': root})


def editPharmacist(request):
    root = request.GET.get('root')
    root2 = request.POST.get('root2')
    if root is None:
        root = root2
    if request.method == 'GET':
        sql1 = 'select * from pharmacist'
        sql2 = 'select * from pharmacist where Phcode=%s'
        Phcode = request.GET.get('Phcode')
        current_pharmacist = sqlUse.get_one(sql2, [Phcode, ])
        pharmacist_list = sqlUse.get_list(sql1, [])
        return render(request, 'editPharmacist.html', {'pharmacist_list': pharmacist_list, 'current_pharmacist': current_pharmacist, 'root': root})
    else:
        Phcode = request.POST.get('Phcode')
        Phname = request.POST.get('Phname')
        Phsex = request.POST.get('Phsex')
        Phage = request.POST.get('Phage')
        Phtitle = request.POST.get('Phtitle')
        Shopcode = request.POST.get('Shopcode')
        Phphone = request.POST.get('Phphone')
        Phcor = request.POST.get('Phcor')
        sql = 'update pharmacist set Phcode=%s, Phname=%s, Phsex=%s, Phage=%s, Phtitle=%s, Shopcode=%s, Phphone=%s, Phcor=%s where Phcode=%s ;'
        sqlUse.modify(sql, [Phcode, Phname, Phsex, Phage, Phtitle, Shopcode, Phphone, Phcor, Phcode])
        sql = 'select * from pharmacist;'
        pharmacist_list = sqlUse.get_list(sql, [])
        return render(request, 'showPharmacist.html', {'pharmacist_list': pharmacist_list, 'root': root})


def deletePharmacist(request):
    root = request.GET.get('root')
    Phcode = request.GET.get('Phcode')
    sql = 'delete from pharmacist where Phcode=%s'
    sqlUse.modify(sql, [Phcode, ])
    sql = 'select * from pharmacist;'
    pharmacist_list = sqlUse.get_list(sql, [])
    return render(request, 'showPharmacist.html', {'pharmacist_list': pharmacist_list, 'root': root})


