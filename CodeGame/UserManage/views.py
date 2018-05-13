"""用户管理模块后台请求函数
@author: 刘昕宸、叶海松
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
def send_sms(apikey, text, mobile):
    params = {
        'apikey': apikey,
        'text': text,
        'mobile':mobile
    }
    data = urllib.parse.urlencode(params).encode('utf-8')
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/plain"
    }
    sms_host = "sms.yunpian.com"
    sms_send_uri = 'https://sms.yunpian.com/v2/sms/single_send.json'
    port = 443

    conn = http.client.HTTPSConnection(sms_host, port=port, timeout=30)
    conn.request("POST", sms_send_uri, data, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str.decode('utf-8')

def getDemo(request):
    """本函数为测试函数，用于测试get请求是否可以正常处理

    Arguments:
        request {obj} -- HTTP请求对象

    Returns:
        JSON -- 返回前端数据
    """

    users = UserManage.models.Userentry.objects.all()
    data = {
        "username": users[1].username,
        "password": users[1].password,
        "tel": users[1].tel_number
    }
    return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def postDemo(request):
    """本函数为测试函数，用于测试post请求是否可以正常处理

    Arguments:
        request {obj} -- HTTP请求对象

    Returns:
        JSON -- 返回前端数据
    """

    print(request.POST['username'])

    user = UserManage.models.Userentry.objects.get(username=request.POST['username'])
    data = {
        "username": user.username,
        "password": user.password,
        "tel": user.tel_number
    }
    return HttpResponse(json.dumps(data), content_type="application/json")

def sendMessage(request):
    apikey = '262c0efbdeb17b346a5b67f90b296446'
    tel_number = request.GET['tel_number']

    verifyCode = ''
    for _ in range(6):
        verifyCode = verifyCode + str(random.randint(0,9))
    text = '【卓越创客】您的验证码是' + verifyCode + '。如非本人操作，请忽略本短信'

    res_str = send_sms(apikey, text, tel_number)
    res = json.loads(res_str)

    if res["code"] == 0:
        flag = True
    else:
        flag = False

    data = {
        "success": flag,
        "status_code": res["code"],
        "verifyCode": verifyCode
    }
    return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def telNumExists(request):
    """此函数用于判断手机号码是否已经存在

    Arguments:
        request {obj} -- HTTP请求对象

    Returns:
        JSON -- 返回前端数据
    """

    tel_number = request.GET['tel_number']
    data = {
        'exists': True
    }

    try:
        users = UserManage.models.Userentry.objects.get(tel_number=tel_number)
    except:
        data = {
            'exists': False
        }

    return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def register(request):
    """用于用户注册用例，向用户表中添加数据

    Arguments:
        request {obj} -- HTTP请求对象

    Returns:
        JSON -- 返回注册成功/失败
    """

    username = request.POST['username']
    password = request.POST['password']
    gender = request.POST['gender']
    age = request.POST['age']
    email = request.POST['email']
    descr = request.POST['descr']
    tel_number = request.POST['tel_number']
    fullname = request.POST['fullname']

    userentry_data = {
        'username': username,
        'password': password,
        'tel_number': tel_number
    }

    try:
        userentry_obj = UserManage.models.Userentry.objects.create(**userentry_data)
        user_data = {
            'fullname': fullname,
            'age': age,
            'gender': gender,
            'email': email,
            'descr': descr,
            'entry_id': userentry_obj.id,
            'level': 1
        }
        user_obj = UserManage.models.User.objects.create(**user_data)
    except:
        data = { 'success': False }
        return HttpResponse(json.dumps(data), content_type="application/json")

    data = { 'success': True }
    return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def member(request):
    """此函数用于充值会员用例，用会员表中更新数据

    Arguments:
        request {obj} -- HTTP请求对象

    Returns:
        JSON -- 返回充值会员成功/失败
    """

    username = request.POST['username']
    priority = request.POST['type']
    add_months = request.POST['month']
    starttime = datetime.datetime.now()

    try:
        entry_id = UserManage.models.Userentry.objects.get(username=username).id
        user_id = UserManage.models.User.objects.get(entry_id=entry_id).user_id
    except:
        return HttpResponse(json.dumps({'success': False}), content_type="application/json")

    start_month = starttime.month
    start_year = starttime.year
    if start_month + int(add_months) > 12:
        start_year = start_year + 1
    start_month = start_month + int(add_months)
    if start_month > 12:
        start_month = start_month - 12
    endtime = starttime.replace(year=start_year, month=start_month, day=1)
    UserManage.models.Membership.objects.filter(user_id=user_id).delete()
    data = {
        'user_id': user_id,
        'priority': priority,
        'starttime': starttime,
        'endtime': endtime
    }
    flag = True
    try:
        UserManage.models.Membership.objects.create(**data)
    except:
        flag = False
    res = {'success': flag}
    return HttpResponse(json.dumps(res), content_type="application/json")

@csrf_exempt
def UpdatePsw(request):
    """此函数用于更新密码用例

    Arguments:
        request {obj} -- HTTP请求对象，包含用户名和密码

    Returns:
        JSON -- 更新密码成功/失败
    """

    username = request.POST['userName']
    password = request.POST['password']

    try:
        user = UserManage.models.Userentry.objects.get(username=username)
        user.password = request.POST['password']
        user.save()
    except:
        data = { 'success': False }
        return HttpResponse(json.dumps(data), content_type="application/json")

    data = { 'success': True }
    return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def UpdatePsdByTelNum(request):
    """此函数用于找回密码用例

    Arguments:
        request {obj} -- HTTP请求对象，包含电话号码和密码

    Returns:
        JSON -- 更新密码成功/失败
    """

    telNumber = request.POST['telNumber']
    password = request.POST['password']
    try:
        user = UserManage.models.Userentry.objects.get(tel_number=telNumber)
        user.password = password
        user.save()
    except:
        data = { 'success': False }
        return HttpResponse(json.dumps(data), content_type="application/json")

    data = { 'success': True }
    return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def Login(request):
    """此函数用于登录用例

    Arguments:
        request {obj} -- HTTP请求对象，包括用户名和密码

    Returns:
        JSON -- 返回登录状态
    """

    content = {}
    var = None
    if request.POST:
        userName = request.POST['userName']
        password = request.POST['password']
        try:
            var = UserManage.models.Userentry.objects.get(username=userName)
        except:
            content['status'] = 0
        if var is None:
            content['status'] = 0
        elif var.password == password:
            content['status'] = 1
        else:
            content['status'] = 0
    return JsonResponse(content)

def getByUsername(request):
    """通过用户名来获取用户基本信息

    Arguments:
        request {obj} -- 用户名

    Returns:
        JSON -- 用户所有个人信息
    """

    username = request.GET['username']
    try:
        user_entry = UserManage.models.Userentry.objects.get(username=username)
        user = UserManage.models.User.objects.get(entry_id=user_entry.id)
        data = {
            'success': True,
            'user_entry': model_to_dict(user_entry),
            'user': model_to_dict(user)
        }
        return HttpResponse(json.dumps(data), content_type="application/json")
    except:
        data = {
            'success': False
        }
        return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def modifyInfo(request):
    """此函数用于修改用户个人信息用例

    Arguments:
        request {obj} -- 用户名

    Returns:
        JSON -- 返回修改成功/失败
    """

    username = request.POST['username']
    try:
        user_entry = UserManage.models.Userentry.objects.get(username=username)
        user = UserManage.models.User.objects.get(entry_id=user_entry.id)
        user.gender = request.POST['gender']
        user.age = request.POST['age']
        user.email = request.POST['email']
        user.descr = request.POST['descr']
        user.fullname = request.POST['fullname']
        user.save()
        data = {
            'success': True
        }
    except:
        data = {
            'success': False
        }
        return HttpResponse(json.dumps(data), content_type="application/json")

    return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def checkPassword(request):
    """此函数用于检查密码是否输入正确

    Arguments:
        request {obj} -- 包括用户名和原密码

    Returns:
        JSON -- 密码正确/错误
    """

    username = request.POST['username']
    password = request.POST['oldPassword']
    data = {}

    try:
        user_entry = UserManage.models.Userentry.objects.get(username=username)
        if user_entry.password == password:
            data['success'] = True
        else:
            data['success'] = False
    except:
        data['success'] = False

    return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def getUsernameByTel(request):
    """通过手机号码获得用户名

    Arguments:
        request {obj} -- 手机号码

    Returns:
        JSON -- 成功/失败，用户名
    """

    telnumber = request.POST['telnumber']
    try:
        username = UserManage.models.Userentry.objects.get(tel_number=telnumber).username
        res = {
            'success': True,
            'username': username
        }
    except:
        res = {
            'success': False
        }
    return HttpResponse(json.dumps(res), content_type="application/json")

def getMemberByUsername(request):
    """通过用户名获得会员信息

    Arguments:
        request {obj} -- 用户名

    Returns:
        JSON -- 会员信息
    """

    username = request.GET['username']
    print(username)
    try:
        user_entry = UserManage.models.Userentry.objects.get(username=username)
        user = UserManage.models.User.objects.get(entry_id=user_entry.id)
        membership = UserManage.models.Membership.objects.filter(user_id=user.user_id)
        data = {}
        data['success'] = True
        if len(membership) == 0:
            data['isMember'] = False
            return HttpResponse(json.dumps(data), content_type="application/json")
        else:
            data['isMember'] = True
            data['starttime'] = str(membership[0].starttime)
            data['endtime'] = str(membership[0].endtime)
            data['priority'] = membership[0].priority
            return HttpResponse(json.dumps(data), content_type="application/json")
    except:
        data = {
            'success': False
        }
        return HttpResponse(json.dumps(data), content_type="application/json")
