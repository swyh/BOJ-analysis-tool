import database as db
import crawling as cr

problem_list = cr.find_problem_list_of_page(1,150)

db.connect("percentage.db")
db.create_table("problem")

db.insert(problem_list)
db_list = db.select_all()

print("DB에 저장된 문제 수 : {0}개".format(str(len(db_list))))