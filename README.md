# BOJ-analysis-tool
백준 유저가 해결한 문제들의 평균 정답 비율을 계산해준다.
<p align="center">
    <img src="./img/img2.jpg", width="400">
    <img src="./img/img.jpg", width="400">
</p>

- 당신이 푼 문제의 정답 비율의 분포도를 나타내 준다.
- 친구들과 랭킹을 매길 수 있다!

### 사용법
![img3](./img/img3.jpg)
- main.py : 단지 분석하고자 하는 아이디들을 넣으면 된다.

### 이외 함수설명
- crawling.py : beautifulsoup을 이용하여 백준의 문제번호와 정답율을 list로 반환
- database.py : sqlite connect, insert, select 기능
- percentage.db : 백준의 문제번호와 정답율이 저장된 Database
- save_at_db.py : 백준의 문제번호와 정답율을 DB에 저장해주는 실행문 ==> 문제의 정답 비율 Update
  - crawling.py, save_at_db는 백준 사이트의 트래픽 부하를 줄 수 있으므로 잦은 실행 자제

### reference
BOJ : https://www.acmicpc.net/
