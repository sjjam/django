from django.shortcuts import render
import random
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request):
    menu = ['닭갈비', '탕수육', '초밥', '스파게티돈가스']
    pick = random.choice(menu)
    return render(request, 'hello.html', {'pick':pick})

def name(request):
    my_name = '네임'
    return render(request, 'name.html', {'my_name':my_name})

def introduce(request):
    my_info = ['jm', '27', '남']
    name = 'jm'
    age = 27
    git = 'https://github.com/sjjam'
    context = {
        'name' : name,
        'age' : age,
        'git' : git
    }
    return render(request, 'introduce.html', context)

def class_name(request):
    class_list = ['dqxxx', '부러럭', '한숨잘란다', '강인선인장', '우황자황청심환']
    pick = random.choice(class_list)
    context = {
        'pick' : pick
    }
    return render(request, 'class_name.html', context)

def yourname(request, name):
    context = {
        'name' : name
    }
    return render(request, 'yourname.html', context)

def yourinfo(request, name, age):
    context = {
        'name' : name,
        'age' : age
    }
    return render(request, 'yourinfo.html', context)

def times(request, num1, num2):
    result = num1 * num2
    context = {
        'result' : result
    }
    return render(request, 'times.html', context)

def gugu(request, big, small):
    gu = []
    if big < small:
        big, small = small, big
    for num in range(1, small+1):
        gu.append(big*num)
    context = {
        'gu' : gu
    }
    return render(request, 'gugu.html', context)

def dtl(request):
    my_list = ['짜장면', '차돌짬뽕', '탕수육', '콩국수']
    empty_list = []
    my_string = "Life is short, You need Python"
    today = datetime.now()
    context = {
        'my_list' : my_list,
        'empty_list' : empty_list,
        'my_string' : my_string,
        'today' : today
    }
    return render(request, 'dtl.html', context)

def forif(request):
    my_list = [100, 50, 30, 20, 10]
    my_string = '간단한 문자열'
    data_a = '첫번째 데이터'
    data_b = '두번째 데이터'
    data_a, data_b = data_b, data_a
    context = {
        'my_list' : my_list,
        'my_string' : my_string,
        'data_a' : data_a,
        'data_b' : data_b
    }
    return render(request, 'forif.html', context)