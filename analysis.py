import database as db
from bs4 import BeautifulSoup
import urllib.request

def print_rank(list):
    list.sort()

    print("정답률 순위")
    for i in range(len(list)):
        print("{0}.{1}[{2}문제, {3:.2f}%]".format(i + 1, list[i][2], list[i][1], list[i][0]))


def calculate_percent(userID):
    list = []

    for id in userID:
        db.connect("percentage.db", "problem")
        db_list = db.select_all()

        req = urllib.request.Request("https://www.acmicpc.net/user/{0}".format(id),
                                     headers={'User-Agent': 'Mozilla/5.0'})
        data = urllib.request.urlopen(req).read()
        bs = BeautifulSoup(data, 'html.parser')

        count = 0
        percent = 0
        percent_distribution = [0 for i in range(10)]

        seccess_div = bs.select(".panel-body")[0]

        for container in seccess_div.select(".problem_number a"):  # container별로 분류
            percent_unit = db.select(container.text)
            percent += float(percent_unit[0:6])
            count += 1

            percent_distribution[int(percent_unit[0:2])//10] += 1


        awnser = percent / count

        print("{0}님은 {1}개 문제를 풀었고, 해결한 문제의 평균 정답 비율은 {2:.2f}% 입니다.".format(id, count, awnser))
        print("정답 비율 분포")
        for i in range(10):
            print("{0:>2d} ~{1:>3d}% : {2:>3d}개".format(i*10, (i+1)*10,percent_distribution[i]), end="")
            for j in range(round(percent_distribution[i]/10)):
                print("■", end ="")
            print()

        list.append([awnser, count, id])
    return list