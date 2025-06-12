def analyze_log_file(log_file_path):
    result = {}

    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                parts = line.strip().split()
                for part in parts:
                    if part.isdigit() and len(part) == 3 and part.startswith(('1', '2', '3', '4', '5')):
                        code = int(part)
                        result[code] = result.get(code, 0) + 1
                        break

    except FileNotFoundError:
        print(f"Файл '{log_file_path}' не знайдено.")
    except IOError:
        print(f"Помилка читання файлу '{log_file_path}'.")

    return result


if __name__ == "__main__":
    result = analyze_log_file("apache_logs.txt")
    print("Результати аналізу HTTP-кодів:")
    for code, count in result.items():
        print(f"{code} — {count} разів")