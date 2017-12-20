from django.shortcuts import render
from models import User
# Create your views here.
#登录
def login(request):
    username = request.GET['username']
    password = request.GET['password']
    username = str(username)
    password = str(password)
    result = {'verdict': 'success', 'message': 'Successful'}
    userinfo = User.objects.filter(username = username,password = password)
    if userinfo:
        request.session["username"] = username
    else:
        result['verdict'] = 'fail'
        result['message'] = 'The Username or Password is not correct'
    return JsonResponse(result)

#登出
def logout(request):
    del request.session["username"]
    result = {'verdict':'success','message':'Successful'}
    return JsonResponse(result)

#注册
def reg(request):
    result = {}
    username = str(request.GET['username'])
    password = str(request.GET['password'])
    email = str(request.GET['email'])
    if len(User.objects.filter(username=username)) == 0:
        # 未被占用
        user = User.objects.create(username=username, password=password, email=email)
        result['verdict'] = 'ok'
        result['message'] = ''
    else:
        result['verdict'] = 'error'
        result['message'] = '帐号被注册'
    return JsonResponse(result)



@csrf_protect
#新建用户 get用户信息
def get(request):
    result = {'verdict': 'success', 'message': 'Successful!'}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        username = str(username)
        password = str(password)
        email = str(email)
        result['email'] = email
        result['password'] = password
        result['username'] = username
        #return JsonResponse(result)
        userinfo = users.objects.filter(Q(email = email)|Q(username = username))
        if userinfo:
            result['verdict'] = 'fail'
            result['message'] = 'The email or username already exits!'
        else:
            users.objects.create(username = username , password = password ,email = email ,friendnum = 0)
        return JsonResponse(result)
    else :
        username = request.session.get('username','')
        userinfo = users.objects.filter(username=username)
        if userinfo:
            result['username'] = username
            result['email'] = str(list(userinfo.values('email'))[0]['email'])
            #result['avatar'] = '/media/'+str(list(userinfo.values('avatar'))[0]['avatar'])
        else:
            result['verdict'] = 'error'
            result['message'] = 'Please log in first!'
        return JsonResponse(result)
