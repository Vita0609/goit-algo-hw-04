import sys
import os
from pathlib import Path
from colorama import Fore, init

# Ініціалізація colorama
init(autoreset=True)

def print_directory_structure(directory, indent=0):
    """Функція для рекурсивного виведення структури директорії з кольоровим оформленням"""
    try:
        # Перевірка, чи є це директорією
        p = Path(directory)
        if not p.is_dir():
            print(Fore.RED + f"Помилка: '{directory}' не є директорією або не існує.")
            return

        # Перебір вмісту директорії
        for entry in p.iterdir():
            # Формуємо відступи для кращого вигляду
            space = ' ' * indent
            if entry.is_dir():
                print(Fore.BLUE + space + f"📂 {entry.name}")  # Для директорій блакитний
                # Рекурсивно викликаємо функцію для підкаталогів
                print_directory_structure(entry, indent + 4)
            else:
                print(Fore.GREEN + space + f"📜 {entry.name}")  # Для файлів зелений
    except Exception as e:
        print(Fore.RED + f"Помилка: {e}")

def main():
    """Основна функція для отримання шляху з аргументів командного рядка та виклику виведення"""
    if len(sys.argv) != 2:
        print(Fore.YELLOW + "Будь ласка, вкажіть шлях до директорії як аргумент.")
        sys.exit(1)

    directory = sys.argv[1]
    print_directory_structure(directory)

if __name__ == '__main__':
    main()
