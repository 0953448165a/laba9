import json
import os
FILENAME = "employees.json"
RESULT_FILE = "result.json"

def init_data():
    if not os.path.exists(FILENAME):
        employees = [
            {"surname": "Іваненко", "salary": 15000, "position": "менеджер", "gender": "чоловік"},
            {"surname": "Петренко", "salary": 22000, "position": "інженер", "gender": "чоловік"},
            {"surname": "Сидоренко", "salary": 18000, "position": "бухгалтер", "gender": "жінка"},
            {"surname": "Коваленко", "salary": 26000, "position": "директор", "gender": "жінка"},
            {"surname": "Шевченко", "salary": 19500, "position": "маркетолог", "gender": "жінка"},
            {"surname": "Ткаченко", "salary": 17000, "position": "аналітик", "gender": "чоловік"},
            {"surname": "Бондар", "salary": 15500, "position": "секретар", "gender": "жінка"},
            {"surname": "Мельник", "salary": 21000, "position": "дизайнер", "gender": "жінка"},
            {"surname": "Кравченко", "salary": 24000, "position": "програміст", "gender": "чоловік"},
            {"surname": "Гриценко", "salary": 16000, "position": "тестувальник", "gender": "чоловік"}
        ]
        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump(employees, f, ensure_ascii=False, indent=4)

def show_data():
    with open(FILENAME, "r", encoding="utf-8") as f:
        employees = json.load(f)
        print("\nВміст JSON файлу:")
        for emp in employees:
            print(emp)
def add_employee():
    with open(FILENAME, "r", encoding="utf-8") as f:
        employees = json.load(f)

    surname = input("Прізвище: ")
    salary = int(input("Зарплата: "))
    position = input("Посада: ")
    gender = input("Стать: ")

    employees.append({"surname": surname, "salary": salary, "position": position, "gender": gender})

    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(employees, f, ensure_ascii=False, indent=4)
    print("✅ Запис додано.")

def delete_employee():
    with open(FILENAME, "r", encoding="utf-8") as f:
        employees = json.load(f)
    surname = input("Введіть прізвище для видалення: ")
    employees = [e for e in employees if e["surname"].lower() != surname.lower()]
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(employees, f, ensure_ascii=False, indent=4)
    print("✅ Запис(и) видалено.")

def search_employee():
    with open(FILENAME, "r", encoding="utf-8") as f:
        employees = json.load(f)
    field = input("Введіть поле для пошуку (surname / position / gender): ").strip().lower()
    value = input("Введіть значення для пошуку: ").strip().lower()
    results = [e for e in employees if str(e.get(field, "")).lower() == value]
    print("\nРезультати пошуку:")
    for emp in results:
        print(emp)
    if not results:
        print("Нічого не знайдено.")
def find_min_max_salary():
    with open(FILENAME, "r", encoding="utf-8") as f:
        employees = json.load(f)
    min_emp = min(employees, key=lambda e: e["salary"])
    max_emp = max(employees, key=lambda e: e["salary"])
    result = {
        "Мінімальна зарплата": min_emp,
        "Максимальна зарплата": max_emp
    }
    print("\n Результат:")
    print(result)
    with open(RESULT_FILE, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
    print(f"Результат записано у файл '{RESULT_FILE}'.")
def menu():
    init_data()

    while True:
        print("\n=== МЕНЮ ===")
        print("1. Показати всі дані")
        print("2. Додати запис")
        print("3. Видалити запис")
        print("4. Пошук за полем")
        print("5. Знайти найменшу та найбільшу зарплату")
        print("0. Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            show_data()
        elif choice == "2":
            add_employee()
        elif choice == "3":
            delete_employee()
        elif choice == "4":
            search_employee()
        elif choice == "5":
            find_min_max_salary()
        elif choice == "0":
            print("Вихід із програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    menu()
