from django.shortcuts import render
import random
import requests

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

# 1. 사용자가 url 경로에 이름을 입력하면
# 2. 그 이름과 무작위 음식 하나 보여주는 페이지 작성
# 2-1. random.choice(menu)
# 3. urls -> views -> template

def food(request, name):
    foodList = ['냉면', '토마토스튜', '짬뽕탕', '불고기']
    pick = random.choice(foodList)
    context = {
        'name' : name,
        'pick' : pick
    }
    return render(request, 'pages/food.html', context)

def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    context = {
        'name' : name,
        'age' : age
    }
    return render(request, 'pages/catch.html', context)

# 1. 사용자가 숫자 입력
# 2. 입력 받은 횟수 만큼 반복해서
# 3. 리스트에 로또 번호 담는다.
# 3-1. random.sample(range(1, 46), 6)
# 4. 사용자가 입력한 숫자와 로또번호가 담긴 리스트를 출력
# 5. ul태그를 사용하여 각 번호들을 한줄 씩 출력
# 6. urls -> views -> template
# 7. 항상 다수의 요소를 작성할 때는 쉼표 잊지말자.

def lotto(request):
    return render(request, 'pages/lotto.html')

def lotto_result(request):
    ntry = int(request.GET.get('ntry'))
    Llist = []
    for n in range(ntry):
        Llist.append(random.sample(range(1, 46), 6))
    sorted_lottos = sorted(random.sample(range(1, 46), 6))
    sort_lottos = (random.sample(range(1, 46), 6)).sort()
    print(sorted_lottos)
    print("*"*30)
    print(sort_lottos)
    context = {
        'ntry' : ntry,
        'Llist' : Llist,
    }
    return render(request, 'pages/lotto_result.html', context)

def artii(request):
    return render(request, 'pages/artii.html')

def result(request):
    message = request.GET.get('message')
    result = requests.get(f'http://artii.herokuapp.com/make?text={message}').text
    context = {
        'result' : result
    }
    return render(request, 'pages/result.html', context)