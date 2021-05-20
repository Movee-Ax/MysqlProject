setInterval("fun(show_time)", 1);

function fun(timeID) {
    var date = new Date();
    var y = date.getFullYear();
    var m = date.getMonth() + 1;
    var d = date.getDate();
    var w = date.getDay();
    var ww = ' 星期' + '日一二三四五六'.charAt(new Date().getDay());
    var h = date.getHours();
    var minute = date.getMinutes()
    var s = date.getSeconds();
    var sss = date.getMilliseconds();
    if (m < 10) {
        m = "0" + m;
    }
    if (d < 10) {
        d = "0" + d;
    }
    if (h < 10) {
        h = "0" + h;
    }


    if (minute < 10) {
        minute = "0" + minute;
    }


    if (s < 10) {
        s = "0" + s;
    }
    document.getElementById(timeID.id).innerHTML
        = y + "-" + m + "-" + d + "   " + h + ":" + minute + ":" + s + ww;
}