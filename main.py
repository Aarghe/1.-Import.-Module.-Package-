import datetime
from lecture1.application.db.people import get_employees
from lecture1.application.salary import calculate_salary


if __name__ == '__main__':
    print(datetime.datetime.now())
    get_employees()
    calculate_salary()
