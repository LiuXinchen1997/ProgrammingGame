"""本模块用于存放挑战/闯关模式相关的请求函数
@author: 刘昕宸
"""


from django.http import *
from django.views.decorators.csrf import csrf_exempt
import urllib.request
import urllib.parse
import http.client
import json
import random
import string
import datetime
import UserManage.models
from django.forms.models import model_to_dict
# Create your views here.

def getLevelByUsername(request):
    """通过用户名获得当前通过关卡

    Arguments:
        request {obj} -- 用户名

    Returns:
        JSON -- 该用户通过的当前关卡数
    """

    username = request.GET['username']
    try:
        entry_id = UserManage.models.Userentry.objects.get(username=username).id
        level = UserManage.models.User.objects.get(entry_id=entry_id).level
        res = {
            'success': True,
            'level': level
        }
    except:
        res = {
            'success': False
        }
    return HttpResponse(json.dumps(res), content_type="application/json")

def getAllLevels(request):
    """获得所有关卡的基本信息

    Arguments:
        request {obj} -- 无

    Returns:
        JSON -- 返回所有关卡的基本信息，包括提示、描述等信息
    """

    try:
        maps = UserManage.models.Challengemap.objects.all()
        hints = []
        descrs = []
        for map in maps:
            hints.append(map.hint)
            descrs.append(map.descr)
        res = {
            'success': True,
            'hints': hints,
            'descrs': descrs
        }
    except:
        res = {
            'success': False
        }

    return HttpResponse(json.dumps(res), content_type="application/json")

def getChallengeMapContent(request):
    """获得闯关模式地图内容

    Arguments:
        request {obj} -- 地图关卡号

    Returns:
        JSON -- 根据关卡号获得该关卡地图元素信息（位置、元素类型）
    """

    level = request.GET['level']
    try:
        map_id = UserManage.models.Challengemap.objects.get(level=level).map_id
        element_objs = UserManage.models.Challengemapcontent.objects.filter(map_id=map_id)
        element_arr = []
        for obj in element_objs:
            item = {}
            x_str = str(obj.position_x)
            if obj.position_x < 10:
                x_str = '0' + x_str
            y_str = str(obj.position_y)
            if obj.position_y < 10:
                y_str = '0' + y_str
            item['pos'] = x_str + '-' + y_str
            item['obj'] = str(obj.element_id)
            element_arr.append(item)
        res = {
            'success': True,
            'map_id': map_id,
            'map_data': element_arr
        }
    except:
        res = {
            'success': False
        }
    return HttpResponse(json.dumps(res), content_type="application/json")

def updateLevelOfUsername(request):
    """通过用户名更新用户通过关卡

    Arguments:
        request {obj} -- 用户名、通过关卡号

    Returns:
        JSON -- 更新成功/失败
    """

    res = {}
    res['success'] = True
    username = request.GET['username']
    level = int(request.GET['level'])
    try:
        entry_id = UserManage.models.Userentry.objects.get(username=username).id
        user = UserManage.models.User.objects.get(entry_id=entry_id)
        if level > user.level:
            user.level = level
            user.save()
    except:
        res['success'] = False

    return HttpResponse(json.dumps(res), content_type="application/json")

@csrf_exempt
def addShareLink(request):
    """添加分享链接

    Arguments:
        request {obj} -- 用户名、通关代码、地图编号

    Returns:
        JSON -- 分享链接的DAO对象
    """

    username = request.POST['username']
    code = request.POST['code']
    isFree = int(request.POST['isFree'])
    map_id = request.POST['map_id']
    res = {}
    try:
        entry_id = UserManage.models.Userentry.objects.get(username=username).id
        user = UserManage.models.User.objects.get(entry_id=entry_id)
        id_nums = len(UserManage.models.Usershare.objects.all()) + 1
        share_data = {
            'id': id_nums,
            'map_id': map_id,
            'isfree': isFree,
            'solution_code': code,
            'user_id': user.user_id
        }
        share_obj = UserManage.models.Usershare.objects.create(**share_data)
        res['success'] = True
        res['share_obj'] = model_to_dict(share_obj)
    except:
        res['success'] = False
    return HttpResponse(json.dumps(res), content_type='application/json')

def getShareLinkById(request):
    """根据id获取分享链接对象

    Arguments:
        request {obj} -- 链接id和用户名

    Returns:
        JSON -- 链接模型对象
    """

    id = request.GET['id']
    res = {}
    try:
        obj = UserManage.models.Usershare.objects.get(id=id)
        user = UserManage.models.User.objects.get(user_id=obj.user_id)
        username = UserManage.models.Userentry.objects.get(id=user.entry_id).username
        res['share_obj'] = model_to_dict(obj)
        res['username'] = username
        if obj.isfree == 0:
            res['level'] = UserManage.models.Challengemap.objects.get(map_id=obj.map_id).level
        res['success'] = True
    except:
        res['success'] = False
    return HttpResponse(json.dumps(res), content_type='application/json')
