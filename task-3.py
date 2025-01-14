import os
import sys
from colorama import Fore, init

# Ініціалізація colorama
init(autoreset=True)

def print_directory_structure(path, indent=0):
    
    try:
        # Перевіряємо, чи це директорія
        if os.path.isdir(path):
            # Отримуємо список файлів та піддиректорій
            items = os.listdir(path)
            
            for item in items:
                # Повний шлях до елементу
                full_item_path = os.path.join(path, item)
                
                if os.path.isdir(full_item_path):
                    # Виводимо директорію зеленим кольором
                    print("  " * indent + Fore.GREEN + f"📂 {item}")
                    # Рекурсивний виклик для піддиректорії
                    print_directory_structure(full_item_path, indent + 1)
                elif os.path.isfile(full_item_path):
                    # Виводимо файл синім кольором
                    print("  " * indent + Fore.BLUE + f"📜 {item}")
        else:
            print(Fore.RED + "Помилка: вказаний шлях не є директорією.")
            sys.exit(1)
    except Exception as e:
        print(Fore.RED + f"Сталася помилка: {e}")
        sys.exit(1)

def main():
    # Перевірка наявності аргументів командного рядка
    if len(sys.argv) < 2:
        print(Fore.RED + "Будь ласка, вкажіть шлях до директорії як аргумент.")
        sys.exit(1)
    
    # Отримуємо шлях до директорії
    directory_path = sys.argv[1]
    
    # Викликаємо функцію для виведення структури директорії
    print_directory_structure(directory_path)

if __name__ == "__main__":
    main()
