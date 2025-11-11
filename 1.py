import csv
input_file = "data.csv"      
output_file = "result.csv"   
try:
    with open(input_file, mode="r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        data = list(reader)
        start_index = 0
        for i, row in enumerate(data):
            if row and row[0] == "Country Name":
                start_index = i
                break

        header = data[start_index]      
        rows = data[start_index + 1:]    
        print("Заголовок:", header)
        print("\nДані:")
        for row in rows:
            print(row)
except FileNotFoundError:
    print(f"Помилка: файл '{input_file}' не знайдено.")
    exit()
except Exception as e:
    print(f"Помилка при відкритті або читанні файлу: {e}")
    exit()
try:
    start_year = int(input("\nВведіть початковий рік: "))
    end_year = int(input("Введіть кінцевий рік : "))
except ValueError:
    print("Помилка: введено нечислове значення року.")
    exit()
year_indices = []
for i, col in enumerate(header):
    if col.isdigit() and start_year <= int(col) <= end_year:
        year_indices.append(i)

if not year_indices:
    print("Не знайдено даних у заданому діапазоні років.")
    exit()
#Фільтруємо дані лише для України

result = []
for row in rows:
    if row[0].strip().lower() == "ukraine":
        result.append(["Country Name"] + [header[i] for i in year_indices])
        result.append([row[0]] + [row[i] for i in year_indices])
        break
if not result:
    print("Не знайдено даних для України.")
    exit()
with open(output_file, mode="w", encoding="utf-8", newline="") as out:
    writer = csv.writer(out)
    writer.writerows(result)
print(f"\n✅ Результати записано у файл '{output_file}'.")
