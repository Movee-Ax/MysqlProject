from django.shortcuts import HttpResponse, render, redirect
import pymysql
from utils import sqlUse
import logging
# 生成一个以当前文件名为名字的logger实例
logger = logging.getLogger(__name__)
# 生成一个名为collect的logger实例
collect_logger = logging.getLogger("collect")

def showShop(request):
    root = request.GET.get('root')
    root2 = request.POST.get('root2')
    if root is None:
        root = root2
    if request.method == 'GET':
        sql = 'select * from shop;'
        shop_list = sqlUse.get_list(sql, [])
        return render(request, 'showShop.html', {'shop_list': shop_list, 'root': root})
    else:
        typeChoose = request.POST.get('type')
        typeValue = request.POST.get('value')
        c1 = '%%' + typeValue + '%%'
        if (typeChoose == '1'):
            sql = 'select * from shop where Shopcode like %s'
            shop_list = sqlUse.get_list(sql, [c1, ])
            return render(request, 'showShop.html', {'shop_list': shop_list, 'root': root})
        elif (typeChoose == '2'):
            sql = 'select * from shop where Shopname like %s'
            shop_list = sqlUse.get_list(sql, [c1, ])
            return render(request, 'showShop.html', {'shop_list': shop_list, 'root': root})
        elif (typeChoose == '3'):
            sql = 'select * from shop where Shoptype like %s'
            shop_list = sqlUse.get_list(sql, [c1, ])
            return render(request, 'showShop.html', {'shop_list': shop_list, 'root': root})
        elif (typeChoose == '4'):
            sql = 'select * from shop where Shopregion like %s'
            shop_list = sqlUse.get_list(sql, [c1, ])
            return render(request, 'showShop.html', {'shop_list': shop_list, 'root': root})
        else:
            sql = 'select * from shop where Wcode like %s'
            shop_list = sqlUse.get_list(sql, [c1, ])
            return render(request, 'showShop.html', {'shop_list': shop_list, 'root': root})


def addShop(request):
    root = request.GET.get('root')
    root2 = request.POST.get('root2')
    if root is None:
        root = root2
    if request.method == 'GET':
        return render(request, 'addShop.html', {'root': root})
    else:
        Shopcode = request.POST.get('Shopcode')
        Shopname = request.POST.get('Shopname')
        Shoptype = request.POST.get('Shoptype')
        Shopregion = request.POST.get('Shopregion')
        Shopadress = request.POST.get('Shopadress')
        Shoparea = request.POST.get('Shoparea')
        Shoplat = request.POST.get('Shoplat')
        Shoplng = request.POST.get('Shoplng')
        Doarea = request.POST.get('Doarea')
        Housearea = request.POST.get('Housearea')
        Shopphone = request.POST.get('Shopphone')
        Wcode = request.POST.get('Wcode')
        sql = 'insert into shop values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
        sqlUse.modify(sql, [Shopcode, Shopname, Shoptype, Shopregion, Shopadress, Shoparea, Shoplat, Shoplng, Doarea,
                            Housearea, Shopphone, Wcode, ])
        sql = 'select * from shop;'
        shop_list = sqlUse.get_list(sql, [])
        return render(request, 'showShop.html', {'shop_list': shop_list, 'root': root})


def editShop(request):
    root = request.GET.get('root')
    root2 = request.POST.get('root2')
    if root is None:
        root = root2
    if request.method == 'GET':
        sql1 = 'select * from shop'
        sql2 = 'select * from shop where Shopcode=%s'
        Shopcode = request.GET.get('Shopcode')
        current_shop = sqlUse.get_one(sql2, [Shopcode, ])
        shop_list = sqlUse.get_list(sql1, [])
        return render(request, 'editShop.html', {'shop_list': shop_list, 'current_shop': current_shop, 'root': root})
    else:
        Shopcode = request.POST.get('Shopcode')
        Shopname = request.POST.get('Shopname')
        Shoptype = request.POST.get('Shoptype')
        Shopregion = request.POST.get('Shopregion')
        Shopadress = request.POST.get('Shopadress')
        Shoparea = request.POST.get('Shoparea')
        Shoplat = request.POST.get('Shoplat')
        Shoplng = request.POST.get('Shoplng')
        Doarea = request.POST.get('Doarea')
        Housearea = request.POST.get('Housearea')
        Shopphone = request.POST.get('Shopphone')
        Wcode = request.POST.get('Wcode')
        sql = 'update shop set Shopcode=%s, Shopname=%s, Shoptype=%s, Shopregion=%s, Shopadress=%s, shoparea=%s, shoplat=%s, shoplng=%s, Doarea=%s, Housearea=%s, Shopphone=%s, Wcode=%s where Shopcode=%s ;'
        sqlUse.modify(sql, [Shopcode, Shopname, Shoptype, Shopregion, Shopadress, Shoparea, Shoplat, Shoplng, Doarea,
                            Housearea, Shopphone, Wcode, Shopcode, ])
        sql = 'select * from shop;'
        shop_list = sqlUse.get_list(sql, [])
        return render(request, 'showShop.html', {'shop_list': shop_list, 'root': root})


def deleteShop(request):
    root = request.GET.get('root')
    Shopcode = request.GET.get('Shopcode')
    sql = 'delete from shop where Shopcode=%s'
    sqlUse.modify(sql, [Shopcode, ])
    sql = 'select * from shop;'
    shop_list = sqlUse.get_list(sql, [])
    return render(request, 'showShop.html', {'shop_list': shop_list, 'root': root})
