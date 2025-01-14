def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary_str = line.strip().split(',')
                salary = int(salary_str)  # Перетворюємо рядок зарплати на ціле число
                total += salary
                count += 1

        # Обчислення середньої зарплати
        average = total / count if count > 0 else 0
        return total, average

    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return 0, 0
    except ValueError:
        print("Помилка у форматі даних у файлі.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
