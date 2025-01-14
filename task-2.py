def get_cats_info(path):
    cats = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age_str = line.strip().split(',')
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age_str  # Залишаємо вік у вигляді рядка
                }
                cats.append(cat_info)

        return cats

    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return []
    except ValueError:
        print("Помилка у форматі даних у файлі.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

cats_info = get_cats_info("cats_file.txt")
print(cats_info)
