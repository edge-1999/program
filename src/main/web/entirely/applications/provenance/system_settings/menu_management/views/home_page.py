import copy

from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse

from docs.utils.response_communal.return_format_communal import JsonResponsePostJsonBasic
from menu_management.models import ProvenanceSystemSettingsMenuManagementMenu


def home(request):
    """
    主目录
    :param request:
    :type request:
    :return:
    :rtype:
    """
    if request.method == "GET":
        menu_home_title = ProvenanceSystemSettingsMenuManagementMenu.objects.filter(ID_PARENT=None).values('id', 'NAME')
        menu_home_title_data = copy.deepcopy(JsonResponsePostJsonBasic())
        for i in menu_home_title:
            menu_home_title_data.data.append(i)
        menu_home_title_data.success = True
        menu_home_title_data.appCode = 1
        menu_home_title_data.appMessage = "数据查询成功"
        menu_home_title_data.expandKeys = ''
        return render(request, 'cornerstone.html', context={'data': menu_home_title_data.dict})
    else:
        return JsonResponse(data={'error_data': '监测到异常，已报警处理！'})


def emperor_menu(request):
    """
    菜单管控
    :param request:
    :type request:
    :return:
    :rtype:
    """
    if request.method == "GET":
        return JsonResponse(data={'error_data': 'GET'})
    else:
        return redirect(reverse('menu_management:HomePage'))


def logout(request):
    """ 注销 """
    request.session.clear()
    return redirect(reverse('menu_management:HomePage'))
