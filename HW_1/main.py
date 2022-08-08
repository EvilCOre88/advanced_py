from application.salary import calculate_salary as c_s
from application.db.people import get_employees
from datetime import datetime


if __name__ == '__main__':
    print(f'Сегодня {datetime.today().strftime("%d/%m/%Y")} и вот чем мы заняты:')
    c_s()
    get_employees()
