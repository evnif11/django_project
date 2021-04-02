from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password  # 보안
from .models import Fcuser  # 모델에서 Fcuser 클래스
from .forms import LoginForm


def home(request):
    return render(request, 'home.html')


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            # session
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


# 회원가입
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')  # html 파일을 렌더링
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야합니다'
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다'
        else:
            fcuser = Fcuser(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )
            fcuser.save()

        return render(request, 'register.html', res_data)
