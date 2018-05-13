"""本模块用于存放自由模式相关的请求函数
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
import traceback
# Create your views here.

def test(request):
    username = 'liuxinchen'
    res = {}
    try:
        entry = UserManage.models.Userentry.objects.get(username=username)
        nowtime = datetime.datetime.now()
        print(nowtime)
        freemap_data = {
            'creator': entry,
            'isrelease': 0,
            'createdtime': nowtime
        }
        UserManage.models.Freemap.objects.create(**freemap_data)
        res['success'] = True
    except:
        traceback.print_exc()
        res['success'] = False
    return HttpResponse(json.dumps(res), content_type="application/json")

def getAllCreatedMapByUsername(request):
    """根据用户名获取该用户创建的所有地图

    Arguments:
        request {obj} -- 用户名

    Returns:
        JSON -- 该用户创建的所有地图的信息
    """

    username = request.GET['username']
    condition = {}
    condition['isRelease'] = 0
    res = {}
    try:
        entry_id = UserManage.models.Userentry.objects.get(username=username).id
        condition['creator'] = entry_id
        map_list = []
        maps = UserManage.models.Freemap.objects.filter(creator=entry_id)
        for map in maps:
            obj = {}
            obj['map_id'] = int(map.map_id)
            obj['hint'] = map.hint
            obj['descr'] = map.descr
            obj['username'] = username
            obj['time'] = str(map.createdtime)
            if int(map.isrelease) == 0:
                map_list.append(obj)
        res['maps'] = map_list
        res['success'] = True
    except:
        res['success'] = False
    return HttpResponse(json.dumps(res), content_type="application/json")

def getAllReleasedMapByUsername(request):
    """根据用户名获得该用户发布的所有地图信息

    Arguments:
        request {obj} -- 用户名

    Returns:
        JSON -- 该用户名的所有已发布的地图的信息
    """

    username = request.GET['username']
    condition = {}
    condition['isRelease'] = 1
    res = {}
    try:
        entry_id = UserManage.models.Userentry.objects.get(username=username).id
        condition['creator'] = entry_id
        map_list = []
        maps = UserManage.models.Freemap.objects.filter(creator=entry_id)
        for map in maps:
            obj = {}
            obj['map_id'] = int(map.map_id)
            obj['hint'] = map.hint
            obj['descr'] = map.descr
            obj['username'] = username
            obj['time'] = str(map.createdtime)
            if int(map.isrelease) == 1:
                map_list.append(obj)
        res['maps'] = map_list
        res['success'] = True
    except:
        res['success'] = False
    return HttpResponse(json.dumps(res), content_type="application/json")

def getAllCollectedMapByUsername(request):
    """根据用户名获得所有已收藏的地图信息

    Arguments:
        request {obj} -- 用户名

    Returns:
        JSON -- 该用户名所有已收藏的地图信息（包括点赞数等）
    """

    username = request.GET['username']
    res = {}
    try:
        entry_id = UserManage.models.Userentry.objects.get(username=username).id
        user = UserManage.models.User.objects.get(entry_id=entry_id)
        map_list = []
        map_collects = UserManage.models.Usercollect.objects.filter(user_id=user.user_id)
        for map_collect in map_collects:
            map = UserManage.models.Freemap.objects.get(map_id=map_collect.map_id)
            obj = {}
            obj['map_id'] = int(map.map_id)
            obj['hint'] = map.hint
            obj['descr'] = map.descr
            obj['username'] = map.creator.username
            obj['time'] = str(map.createdtime)
            obj['like_num'] = len(UserManage.models.Userlike.objects.filter(map_id=map.map_id))
            if len(UserManage.models.Userlike.objects.filter(user_id=user.user_id, map_id=map.map_id)) == 0:
                obj['is_like'] = False
            else:
                obj['is_like'] = True
            map_list.append(obj)
        res['maps'] = map_list
        res['success'] = True
    except:
        res['success'] = False
    return HttpResponse(json.dumps(res), content_type="application/json")

def getAllReleasedMap(request):
    """获得所有已发布的地图的信息

    Arguments:
        request {obj} -- 用户名

    Returns:
        JSON -- 所有已发布的地图的信息
    """

    username = request.GET['username']
    res = {}
    try:
        entry_id = UserManage.models.Userentry.objects.get(username=username).id
        user = UserManage.models.User.objects.get(entry_id=entry_id)
        map_list = []
        maps = UserManage.models.Freemap.objects.filter(isrelease=1)
        for map in maps:
            obj = {}
            obj['map_id'] = int(map.map_id)
            obj['hint'] = map.hint
            obj['descr'] = map.descr
            obj['username'] = map.creator.username
            obj['time'] = str(map.createdtime)
            obj['like_num'] = len(UserManage.models.Userlike.objects.filter(map_id=map.map_id))
            if len(UserManage.models.Userlike.objects.filter(user_id=user.user_id, map_id=map.map_id)) == 0:
                obj['is_like'] = False
            else:
                obj['is_like'] = True
            obj['collect_num'] = len(UserManage.models.Usercollect.objects.filter(map_id=map.map_id))
            if len(UserManage.models.Usercollect.objects.filter(user_id=user.user_id, map_id=map.map_id)) == 0:
                obj['is_collect'] = False
            else:
                obj['is_collect'] = True
            map_list.append(obj)
        res['maps'] = map_list
        res['success'] = True
    except:
        res['success'] = False
    return HttpResponse(json.dumps(res), content_type="application/json")

def deleteMapById(request):
    """根据地图id删除地图

    Arguments:
        request {obj} -- 地图id

    Returns:
        JSON -- 删除结果（成功/失败）
    """

    map_id = request.GET['map_id']
    res = {}
    try:
        UserManage.models.Freemapcontent.objects.filter(map_id=map_id).delete()
        UserManage.models.Userlike.objects.filter(map_id=map_id).delete()
        UserManage.models.Usershare.objects.filter(map_id=map_id, isfree=1).delete()
        UserManage.models.Usercollect.objects.filter(map_id=map_id).delete()
        UserManage.models.Freemap.objects.filter(map_id=map_id).delete()
        res['success'] = True
    except:
        res['success'] = False
    return HttpResponse(json.dumps(res), content_type='application/json')

def setLikeById(request):
    """为指定的地图点赞

    Arguments:
        request {obj} -- 用户名、地图id

    Returns:
        JSON -- 点赞成功/失败
    """

    username = request.GET['username']
    map_id = request.GET['map_id']
    res = {}
    try:
        entry_id = UserManage.models.Userentry.objects.get(username=username).id
        user = UserManage.models.User.objects.get(entry_id=entry_id)
        like_data = {
            'user_id': user.user_id,
            'map_id': map_id
        }
        like_obj = UserManage.models.Userlike.objects.create(**like_data)
        res['success'] = True
        res['like_obj'] = model_to_dict(like_obj)
    except:
        res['success'] = False
    return HttpResponse(json.dumps(res), content_type='application/json')

def cancelLikeById(request):
    """取消对指定地图的赞

    Arguments:
        request {obj} -- 用户名、地图编号

    Returns:
        JSON -- 取消成功/失败
    """

    username = request.GET['username']
    map_id = request.GET['map_id']
    res = {}
    try:
        entry_id = UserManage.models.Userentry.objects.get(username=username).id
        user = UserManage.models.User.objects.get(entry_id=entry_id)
        UserManage.models.Userlike.objects.filter(user_id=user.user_id, map_id=map_id).delete()
        res['success'] = True
    except:
        res['success'] = False
    return HttpResponse(json.dumps(res), content_type='application/json')

def setCollectById(request):
    """收藏指定地图

    Arguments:
        request {obj} -- 用户名、指定地图编号

    Returns:
        JSON -- 收藏成功/失败
    """

    username = request.GET['username']
    map_id = request.GET['map_id']
    res = {}
    try:
        entry_id = UserManage.models.Userentry.objects.get(username=username).id
        user = UserManage.models.User.objects.get(entry_id=entry_id)
        collect_data = {
            'user_id': user.user_id,
            'map_id': map_id
        }
        collect_obj = UserManage.models.Usercollect.objects.create(**collect_data)
        res['success'] = True
        res['collect_obj'] = model_to_dict(collect_obj)
    except:
        res['success'] = False
    return HttpResponse(json.dumps(res), content_type='application/json')

def cancelCollectById(request):
    """为指定地图取消收藏

    Arguments:
        request {obj} -- 用户名、地图id

    Returns:
        JSON -- 取消成功/失败
    """

    username = request.GET['username']
    map_id = request.GET['map_id']
    res = {}
    try:
        entry_id = UserManage.models.Userentry.objects.get(username=username).id
        user = UserManage.models.User.objects.get(entry_id=entry_id)
        UserManage.models.Usercollect.objects.filter(user_id=user.user_id, map_id=map_id).delete()
        res['success'] = True
    except:
        res['success'] = False
    return HttpResponse(json.dumps(res), content_type='application/json')

@csrf_exempt
def saveCreateMap(request):
    """保存新创建的地图

    Arguments:
        request {obj} -- 地图信息、用户名

    Returns:
        JSON -- 保存成功/失败
    """

    username = request.POST['username']
    str_data = request.POST['data']
    obj_data = json.loads(str_data)
    map_elems = obj_data['map_data']
    res = {}
    try:
        entry_obj = UserManage.models.Userentry.objects.get(username=username)
        nowtime = datetime.datetime.now()
        freemap_data = {
            'creator': entry_obj,
            'isrelease': 0,
            'createdtime': nowtime
        }
        freemap_obj = UserManage.models.Freemap.objects.create(**freemap_data)
        for elem in map_elems:
            str_pos = elem['pos']
            obj_elem = UserManage.models.Element.objects.get(element_id=elem['obj'])
            elem_data = {
                'position_x': int(str_pos[0:2]),
                'position_y': int(str_pos[3:]),
                'element_id': obj_elem.element_id,
                'map_id': freemap_obj.map_id
            }
            UserManage.models.Freemapcontent.objects.create(**elem_data)
        res['success'] = True
    except:
        traceback.print_exc()
        res['success'] = False
    return HttpResponse(json.dumps(res), content_type='application/json')

def getFreeMapContent(request):
    """获得自由模式关卡地图的内容

    Arguments:
        request {obj} -- 地图编号

    Returns:
        JSON -- 地图元素集合
    """

    map_id = request.GET['map_id']
    try:
        element_objs = UserManage.models.Freemapcontent.objects.filter(map_id=map_id)
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
            #item['obj'] = str(obj.element_id)
            item['obj'] = obj.element_id
            element_arr.append(item)
        res = {
            'success': True,
            'map_data': element_arr
        }
    except:
        res = {
            'success': False
        }
    return HttpResponse(json.dumps(res), content_type="application/json")

@csrf_exempt
def updateFreeMapContent(request):
    """更新地图元素

    Arguments:
        request {obj} -- 修改之后的地图元素内容

    Returns:
        JSON -- 更新成功/失败
    """

    map_id = request.POST['map_id']
    str_data = request.POST['data']
    obj_data = json.loads(str_data)
    map_elems = obj_data['map_data']
    res = {}
    try:
        UserManage.models.Freemapcontent.objects.filter(map_id=map_id).delete()
        for elem in map_elems:
            str_pos = elem['pos']
            obj_elem = UserManage.models.Element.objects.get(element_id=elem['obj'])
            elem_data = {
                'position_x': int(str_pos[0:2]),
                'position_y': int(str_pos[3:]),
                'element_id': obj_elem.element_id,
                'map_id': map_id
            }
            UserManage.models.Freemapcontent.objects.create(**elem_data)
        res['success'] = True
    except:
        traceback.print_exc()
        res['success'] = False
    return HttpResponse(json.dumps(res), content_type='application/json')

def uploadFreeMapById(request):
    """发布特定地图

    Arguments:
        request {obj} -- 地图编号

    Returns:
        JSON -- 发布成功/失败
    """

    map_id = request.GET['map_id']
    res = {}
    try:
        freemap_obj = UserManage.models.Freemap.objects.get(map_id=map_id)
        freemap_obj.isrelease = 1
        freemap_obj.save()
        res['success'] = True
    except:
        res['success'] = False

    return HttpResponse(json.dumps(res), content_type='application/json')
