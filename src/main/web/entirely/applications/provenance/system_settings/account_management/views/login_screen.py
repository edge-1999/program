from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse

from account_management.forms.account_from import AccountLoginForm


def login(request):
    if request.method == "GET":
        account_login_form = AccountLoginForm()
        return render(request, "account/login.html", {"form": account_login_form})
        # return JsonResponse(data={'login_data': 'GET'})
        # form = LoginForm()
        # return render(request, "login.html", {"form": form})

    # 1.接收并获取数据(数据格式或是否为空验证 - Form组件 & ModelForm组件）
    if request.method == "POST":
        # form = LoginForm(data=request.POST)
        # if not form.is_valid():
        #     return render(request, "login.html", {"form": form})
        #
        # # 2.去数据库校验  1管理员  2客户
        # data_dict = form.cleaned_data
        # role = data_dict.pop('role')
        # if role == "1":
        #     user_object = models.Administrator.objects.filter(active=1).filter(**data_dict).first()
        # else:
        #     user_object = models.Customer.objects.filter(active=1).filter(**data_dict).first()
        #
        # # 2.1 校验失败
        # if not user_object:
        #     form.add_error("username", "用户名或密码错误")
        #     return render(request, "login.html", {'form': form})
        #
        # # 2.2 校验成功，用户信息写入session+进入项目后台
        # mapping = {"1": "ADMIN", "2": "CUSTOMER"}
        # request.session[settings.NB_SESSION_KEY] = {'role': mapping[role], 'name': user_object.username,
        #                                             'id': user_object.id}
        # return redirect(settings.LOGIN_HOME)
        return JsonResponse(data={'login_data': 'POST'})
    else:
        return redirect(reverse('menu_management:HomePage'))
