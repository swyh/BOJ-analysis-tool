from bs4 import BeautifulSoup
import urllib.request

def find_problem_list_of_page(start_page, end_page = 0):
    if end_page == 0:
        end_page = start_page

    list = []
    for page in range(start_page, end_page + 1):
        req = urllib.request.Request("https://www.acmicpc.net/problemset/{0}".format(str(page)),
                                     headers={'User-Agent': 'Mozilla/5.0'})
        data = urllib.request.urlopen(req).read()
        bs = BeautifulSoup(data, 'html.parser')

        for container in bs.select("tbody tr"):  # container별로 분류
            #print(container.select(".list_problem_id")[0].text, container.select(".click-this a")[0].text, container.select("td")[5].text)
            list.append([container.select(".list_problem_id")[0].text, container.select(".click-this a")[0].text, container.select("td")[5].text])

        print("{0}페이지 저장 성공".format(str(page)))

    return list
