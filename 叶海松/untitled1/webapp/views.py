from django.shortcuts import render
from django.http import *
from webapp.models import  *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def   hello(request) :
   # Users(name='yangzhen',password='123456').save()
   #  for var in Users.objects.all():
   #     print(var.name , '   ',var.password)
   #  users = Users.objects.all()
   #  content ={
   #         'user':users
   #  }
    return render(request,"login.html")


@csrf_exempt
def login(request):
    content = {}
    var = None
    Name = request.POST['username']
    Password = request.POST['password']
    content['Username'] = Name
    content['Password'] = Password
    if Name.strip() =='':
        content['nameNull'] = "用户名不能为空"
    if Password.strip() =='':
        content['PasswordNull'] = "密码不能为空"
    if(Name.strip() =='' or Password.strip() ==''):
        return render(request, "login.html", context=content)
    if request.POST:
        try:
            var = Users.objects.get(username=Name)
        except:
            content['wrong'] = "请检查输入的用户名或密码"
            return render(request, "login.html", context=content)
        if(var.password != Password):
            content['wrong'] = "请检查输入的用户名或密码"
            return render(request, "login.html", context=content)
        else:
            content['user'] = var
            request.session['UserId'] = var.id
            request.session['Username'] = var.name
            return render(request, "manageCourse.html", context=content)

@csrf_exempt
def selectCourse(request):
    try:
       uid = int(request.session['UserId'])
    except:
       return render(request, "login.html")
    content = {}
    var = Courses.objects.all()
    content['allCourse'] = var
    return render(request,"selectCourse.html",context=content)

@csrf_exempt
def submitSelectCourse(request,nid):
    target = None
    condition = {}
    content = {}
    try:
        uid = int(request.session['UserId'])
    except:
        return render(request, "login.html")
    Nid = int(nid)
    condition['userid'] = uid
    condition['courseid'] = Nid
    try:
       target = Selectcourse.objects.filter(**condition)
    except:
        print("hello 54646")
    print(target)
    try:
        var11 = Courses.objects.get(courseid=Nid)
    except:
        content['response'] = "系统检测到你有异常操作，请立即停止"
        var = Courses.objects.all()
        content['allCourse'] = var
        return render(request, "selectCourse.html", context=content)
    if target.count() == 0:
       obj = Selectcourse(userid = uid,courseid = nid)
       obj.save()
       content['response'] = "选课成功"
    else:
      content['response'] = "不能重复选课"
    var = Courses.objects.all()
    content['allCourse'] = var
    return render(request, "selectCourse.html", context=content)

@csrf_exempt
def myClassSelected(request):
    context ={}
    course = set()
    try:
       uid = int(request.session['UserId'])
    except:
       return render(request, "login.html")
    selectCoursed = Selectcourse.objects.filter(userid=uid)
    for i  in selectCoursed:
         selectedCourse = Courses.objects.get(courseid=i.courseid)
         course.add(selectedCourse)
    context['selected'] = course
    return render(request,"myCourse.html",context=context)

@csrf_exempt
def deleteCourse(request,courseid):
    context = {}
    selectedCourse = None
    try:
      uid = int(request.session['UserId'])
    except:
      return render(request, "login.html")
    if Selectcourse.objects.filter(userid=uid).count() !=0 :
        try:
         Selectcourse.objects.filter(userid=uid).get(courseid=courseid).delete()
        except:
         context['suggestion'] = "系统检查到有异常操作,请立即停止"
         return render(request, "myCourse.html", context=context)
    course = set()
    selectCoursed = Selectcourse.objects.filter(userid=uid)
    for i in selectCoursed:
          selectedCourse = Courses.objects.get(courseid=i.courseid)
          course.add(selectedCourse)
    context['selected'] = course
    context['suggestion'] = "退课成功"
    return render(request, "myCourse.html", context=context)

def mainPage(request):
    content = {}
    uid = 0
    try:
      uid = int(request.session['UserId'])
    except:
      return render(request, "login.html")
    var = Users.objects.get(id = uid)
    content['user'] =var
    return render(request,"manageCourse.html",context=content)

def myInformation(request):
    content = {}
    uid = 0
    try:
        uid = int(request.session['UserId'])
    except:
        return render(request, "login.html")
    var = Users.objects.get(id=uid)
    content['user'] = var
    return render(request, "myInformation.html", context=content)

def loginOut(request):
    request.session['UserId'] = None
    return render(request,"login.html")