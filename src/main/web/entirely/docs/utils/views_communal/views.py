# import json
# import random
#
# from django.http import JsonResponse, HttpResponse
# from django.shortcuts import render, get_object_or_404
# from django.views import View
# from django.views.decorators.http import require_http_methods
#

# from Blog.models import BlogWritings
# from li.settings import DATABASES_MYSQL, DATABASES_MYSQL_CONN, DATABASES_MYSQL_CURSOR


# from simplepro.monitor.views import JsonResponse
# from django.shortcuts import render, get_object_or_404

# Create your views here.


# def get_post(request):
#     if request.method.upper() == "GET":
#         return JsonResponse(data={'GET': request.method.upper()})
#     elif request.method.upper() == "POST":
#         return JsonResponse(data={'POST': request.method.upper()})
#     else:
#         return JsonResponse(data={})


# class Home(View):
#     def post(self, request):
#         data_home = {}
#         for i in range(10):
#             key_id = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=32))
#             data_home['{}'.format(key_id)] = {}
#             data_home[key_id].update({
#                 "key_id": key_id,
#                 "name": 'name{}'.format(i),
#                 "svg_path": "/docs/media/images/02GOB7JF.png",
#             })
#         return JsonResponse(data=data_home)
#         # return HttpResponse(json.dumps(data_home), content_type="application/json")  # 第二种

# class VueHome(View):
#     def get(self, request):
#         data_home = {}
#         for i in range(10):
#             key_id = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=32))
#             data_home['{}'.format(key_id)] = {}
#             data_home[key_id].update({
#                 "key_id": key_id,
#                 "name": 'name{}'.format(i),
#                 "svg_path": "/docs/media/images/02GOB7JF.png",
#             })
#         return JsonResponse(data=data_home)
#         # return HttpResponse(json.dumps(data_home), content_type="application/json")  # 第二种


# class LeftSidebar(View):
#     def get(self, request, sidebar=None):
#         data_home = {sidebar: {}}
#         for i in range(10):
#             key_id = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=32))
#             data_home[sidebar]['{}'.format(key_id)] = {}
#             data_home[sidebar][key_id].update({
#                 "key_id": key_id,
#                 "name": 'name{}'.format(i),
#                 "svg_path": "/docs/media/images/02GOB7JF.svg",
#             })
#         return JsonResponse(data=data_home)
#
#
# class LeftSidebarSon(View):
#     def get(self, request, sidebar=None):
#         data_home = {sidebar: {}}
#         for i in range(10):
#             key_id = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=32))
#             data_home[sidebar]['{}'.format(key_id)] = {}
#             data_home[sidebar][key_id].update({
#                 # "key_id": "e4c3267869244e90b4a54361a8b9c045",
#                 "key_id": key_id,
#                 "name": 'name{}'.format(i),
#                 "svg_path": "/docs/media/images/02GOB7JF.svg",
#             })
#         return JsonResponse(data=data_home)
#
#
# class LeftSidebarSonContent(View):
#     def get(self, request, sidebar=None):
#         try:
#             content = get_object_or_404(BlogWritings, ID=sidebar)
#             data_home = {sidebar: {
#                 "key_id": sidebar,
#                 "content": content.BLOG_CONTENT
#             }}
#             click_number = content.BLOG_CLINK + 1
#             BlogWritings.objects.filter(ID=sidebar).update(BLOG_CLINK=click_number)
#             return JsonResponse(data=data_home)
#         except Exception as e:
#             content = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))
#             return JsonResponse(data={sidebar: {"key_id": sidebar, "content": '密钥：{}'.format(content)}})
