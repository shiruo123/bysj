from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from app1.models import *
from django.core.exceptions import ObjectDoesNotExist
from app1.kaoshi_t import KaoShiClass


# Create your views here.


def admin(request):
    kemu = KaoShi.objects.all()
    user = UserAccount.objects.all()
    tiku = TiKu_xzt.objects.all()
    return render(request, 'admin/admin.html', context={
        'kemu': kemu,
        'user': user,
        'tiku': tiku,
    })


def delete_data(request):
    data = request.GET

    if request.GET.get('b_id') == "1":
        kemu = KaoShi.objects.filter(id=int(data.get('b_b_id')))
    elif request.GET.get('b_id') == "2":
        kemu = UserAccount.objects.filter(id=int(data.get('b_b_id')))
    elif request.GET.get('b_id') == '3':
        kemu = TiKu_xzt.objects.filter(id=int(data.get('b_b_id')))
    kemu.delete()
    return HttpResponse("删除")


def update_data(request):
    data = request.GET
    datas = data.getlist('datas')
    print(datas)
    if data.get('b_id') == "1":
        KaoShi.objects.filter(id=int(data.get('b_b_id'))).update(a=datas[0], other=datas[1], img=datas[2])
    elif data.get('b_id') == '2':
        UserAccount.objects.filter(id=int(data.get('b_b_id'))).update(user=datas[0], password=datas[1])
    elif data.get('b_id') == '3':
        TiKu_xzt.objects.filter(id=int(data.get('b_b_id'))).update(t=datas[0], a=datas[1], b=datas[2], c=datas[3], d=datas[4],daan=datas[5])
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
    elif data.get('b_id') == "2":
        datas = {
            'user': datas[0],
            'password': datas[1],
        }
        k = UserAccount(**datas)
    elif data.get('b_id') == "3":
        datas = {
            't': datas[0],
            'a': datas[1],
            'b': datas[2],
            'c': datas[3],
            'd': datas[4],
            'daan': datas[5],
        }
        k = TiKu_xzt(**datas)
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


def kaoshi(request, kaoshi_id):
    text_dict = {
        "tx": [],
        "d": [],
    }
    if request.session['is_login']:
        kaoshi_ = KaoShiClass()
        kaoshi_.input(int(kaoshi_id))
        texts = kaoshi_.text()
        # 将元组转化为列表方便修改数据
        for j, t in enumerate(texts):
            texts = list(texts)
            texts[j] = list(t)
        # 设置序号 如题1.***
        for i in range(1, 11):
            texts[i - 1][1] = str(i) + "." + texts[i - 1][1]
            texts[i - 1].pop(0)
        # 将题、选项、答案进行分类
        for text in texts:
            xs_list = []
            text_dict.get("d").append(text[-1])
            for xs in text[1:-1]:
                xs_list.append(xs)
            text_dict.get("tx").append([text[0], xs_list])
        return render(request, 'kaoshi.html', context={
            "kaoshi_id": kaoshi_id,
            "ti": text_dict,
            "user": request.session["user"],
        })
    else:
        return render(request, 'login/login.html')


def chengji(request, kaoshi_id, daans):
    if request.method == "POST":
        daans = eval(daans)
        sum = 0
        kaoshi = KaoShi.objects.get(id=kaoshi_id)
        user = UserAccount.objects.get(user=request.session["user"])
        for i in range(1, 11):
            daan = request.POST.get(str(i))
            print(daan, daans[i - 1], type(daan), type(daans[i - 1]))
            if daan == daans[i - 1]:
                sum += 10
        cj = ChengJi(keu_KaoShi_b_id=kaoshi_id, key_user_a_id=user.id, fenshu=sum)
        cj.save()
        return HttpResponse(f"<script>alert('{kaoshi.a}，得分：{sum}，任务完成');window.location.href=''</script>")
    else:
        return redirect("main")
