import time

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from app1.models import *
from django.core.exceptions import ObjectDoesNotExist
from app1.kaoshi_t import KaoShiClass


# Create your views here.


def admin(request):
    if request.session['user'] == "admin":
        tikuguanlis = []
        kemus = KaoShi.objects.all()
        users = UserAccount.objects.all()
        tikus = TiKu_xzt.objects.all()
        lts = LunTan.objects.filter().all()
        for kemu in kemus:
            tikuguanli = TiKuGuanLi.objects.filter(key_KaoShi_b_id=kemu.id)
            tikuguanlis.append(tikuguanli)
        return render(request, 'admin/admin.html', context={
            'kemu': kemus,
            'user': users,
            'tiku': tikus,
            'tgs': tikuguanlis,
            'lts': lts,
        })
    else:
        return redirect('main')


def delete_data(request):
    data = request.GET

    if request.GET.get('b_id') == "1":
        d = KaoShi.objects.filter(id=int(data.get('b_b_id')))
    elif request.GET.get('b_id') == "2":
        d = UserAccount.objects.filter(id=int(data.get('b_b_id')))
    elif request.GET.get('b_id') == '4':
        d = TiKuGuanLi.objects.filter(id=int(data.get('b_b_id')))
    elif request.GET.get('b_id') == '6':
        d = TiKu_xzt.objects.filter(id=int(data.get('b_b_id')))
    elif request.GET.get('b_id') == '7':
        d = LunTan.objects.filter(id=int(data.get('b_b_id')))
    d.delete()
    return HttpResponse("删除")


def update_data(request):
    data = request.GET
    datas = data.getlist('datas')
    print(datas)
    if data.get('b_id') == "1":
        KaoShi.objects.filter(id=int(data.get('b_b_id'))).update(a=datas[0], other=datas[1], img=datas[2])
    elif data.get('b_id') == '2':
        UserAccount.objects.filter(id=int(data.get('b_b_id'))).update(user=datas[0], password=datas[1])
    elif data.get('b_id') == '4':
        TiKu_xzt.objects.filter(id=int(data.get('b_b_id'))).update(t=datas[0], a=datas[1], b=datas[2], c=datas[3], d=datas[4],daan=datas[5])
    elif data.get('b_id') == '7':
        datas[-1] = datas[-1].replace("年", "-")
        datas[-1] = datas[-1].replace("月", "-")
        datas[-1] = datas[-1].replace("日", "")
        LunTan.objects.filter(id=int(data.get('b_b_id'))).update(title=datas[1], text=datas[2], date=datas[3])
    return HttpResponse("修改")


def create_data(request):
    data = request.GET
    datas = data.getlist('datas')
    if data.get('b_id') == "1":
        datas = {
            'a': datas[0],
            'other': datas[1],
            'img': datas[2],
        }
        k = KaoShi(**datas)
        k.save()
        kaoshi = KaoShiClass()
        ti = kaoshi.get_ti()
        kaoshi.set_KaoShi_db(k.id, ti)
    elif data.get('b_id') == "2":
        datas = {
            'user': datas[0],
            'password': datas[1],
        }
        k = UserAccount(**datas)
    elif data.get('b_id') == "5":
        datas = {
            'key_KaoShi_b_id': int(datas[1]),
            'key_TiKu_a_id': int(datas[0]),
        }
        k = TiKuGuanLi(**datas)
    elif data.get('b_id') == '6':
        datas = {
            't': datas[0],
            'a': datas[1],
            'b': datas[2],
            'c': datas[3],
            'd': datas[4],
            'daan': datas[5],
        }
        k = TiKu_xzt(**datas)
    elif data.get('b_id') == '7':
        datas[0] = UserAccount.objects.get(user=datas[0]).id
        datas = {
            'key_UserAccount_id': datas[0],
            'title': datas[1],
            'text': datas[2],
        }
        k = LunTan(**datas)
    k.save()
    return HttpResponse(k.id)


def main(request):
    if request.session.get("is_login"):
        return render(request, "main.html", context={'user': request.session.get('user')})
    else:
        return redirect("login")


def login_html(request):
    if request.session.get("is_login"):
        return redirect("main")
    else:
        return render(request, "login/login.html")


def login_panduan(request):
    if request.method == "POST":
        user = request.POST.get('account')
        password = request.POST.get('pwd')
        try:
            is_user = UserAccount.objects.get(user=user, password=password)
            request.session["is_login"] = True
            request.session["user"] = is_user.user
            return redirect("main")
        except ObjectDoesNotExist:
            return HttpResponse("<html><body><script>alert('密码错误！');window.location.href=''</script></body></html>")
    else:
        return redirect("login")


def login_out(request):
    request.session["is_login"] = False
    return redirect("login")


def pwd_update_html(request):
    return render(request, "login/pwd_update.html")


def pwd_update(request):
    if request.method == "POST":
        user = request.POST.get("account")
        pwd = request.POST.get("pwd")
        try:
            user = UserAccount.objects.get(user=user)
            user.password = pwd
            user.save()
            return HttpResponse("<html><body><script>alert('修改成功！');window.location.href='../'</script></body></html>")

        except ObjectDoesNotExist:
            print(1)
            return HttpResponse(
                "<html><body><script>alert('当前用户不存在');window.location.href='pwd_update_html'</script></body></html>")
            # return redirect("pwd_update_html")
    else:
        return redirect("pwd_update_html")


def new_account_html(request):
    return render(request, "login/new_account.html")


def new_account(request):
    if request.method == "POST":
        user = request.POST.get('account')
        pwd = request.POST.get('pwd')
        try:
            user = UserAccount.objects.get(user=user)
            return HttpResponse(
                "<html><body><script>alert('账号已存在，添加失败！');window.location.href='new_account_html'</script></body></html>")
        except ObjectDoesNotExist:
            user = UserAccount(user=user, password=pwd)
            user.save()
            return HttpResponse(
                "<html><body><script>alert('账号注册成功！');window.location.href='../'</script></body></html>")
    else:
        return redirect("new_account_html")


def iframe1(request):
    n = []
    y = []
    user_id = UserAccount.objects.get(user=request.session['user']).id
    ks_datas = KaoShi.objects.all()
    ks_datas_y = ChengJi.objects.filter(key_user_a_id=user_id)
    if len(ks_datas_y) != 0:
        for ks_data in ks_datas:
            n.append(ks_data)
            for ks_data_y in ks_datas_y:
                if ks_data.id == ks_data_y.keu_KaoShi_b_id:
                    y.append([ks_data, ks_data_y.fenshu])
                    n.pop(-1)
    else:
        n = ks_datas

    return render(request, 'iframe1.html', context={
        'ks_datas_n': n,
        'ks_datas_y': y,
    })


def iframe2(request):
    luntan = LunTan.objects.filter().all()
    return render(request, 'iframe2.html', context={
        "lts": luntan
    })


def iframe2_add_data(request):
    if request.method == "POST":
        title = request.POST.get("title_input")
        text = request.POST.get("text_input")
        user_id = UserAccount.objects.get(user=request.session["user"]).id
        lt = LunTan(title=title, text=text, key_UserAccount_id=user_id)
        lt.save()
        return HttpResponse("<script>alert('评论成功！');window.location.href='../iframe2'</script>")
    else:
        return redirect('main')


def kaoshi(request, kaoshi_id):
    ti_s = []
    if request.session['is_login']:
        tiku = TiKuGuanLi.objects.filter(key_KaoShi_b_id=int(kaoshi_id))
        for t in tiku.all():
            ti = [t.key_TiKu_a.a, t.key_TiKu_a.b]
            if t.key_TiKu_a.c:
                ti.append(t.key_TiKu_a.c)
                if t.key_TiKu_a.d:
                    ti.append(t.key_TiKu_a.d)
            ti_s.append([t.key_TiKu_a.t, ti])
        return render(request, 'kaoshi.html', context={
            "kaoshi_id": kaoshi_id,
            "ti": ti_s,
            "user": request.session["user"],
        })
    else:
        return render(request, 'login/login.html')


def chengji(request, kaoshi_id):
    if request.method == "POST":
        daans = TiKuGuanLi.objects.filter(key_KaoShi_b_id=kaoshi_id).values_list('key_TiKu_a__daan')
        sum = 0
        print("运行到此")
        fenzhi = int(100/len(daans))
        kaoshi = KaoShi.objects.get(id=kaoshi_id)
        user = UserAccount.objects.get(user=request.session["user"])
        for i in range(1, int(len(daans))+1):
            # 获取input的答案
            daan = request.POST.get(str(i))
            print(daan, daans[i - 1][0], type(daan), type(daans[i - 1][0]))
            if daan == daans[i - 1][0]:
                sum += fenzhi
        print(sum)
        print(fenzhi)
        cj = ChengJi(keu_KaoShi_b_id=kaoshi_id, key_user_a_id=user.id, fenshu=sum)
        cj.save()
        return HttpResponse(f"<script>alert('{kaoshi.a}，得分：{sum}，任务完成');window.location.href=''</script>")
    else:
        return redirect("main")
