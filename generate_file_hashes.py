import hashlib

def generate_file_hashes(*file_paths):
    result = {}
    for file_path in file_paths:
        try:
            with open(file_path, 'rb') as file:
                content = file.read()
                sha256 = hashlib.sha256(content).hexdigest()
                result[file_path] = sha256
        except FileNotFoundError:
            print(f"Файл '{file_path}' не знайдено.")
        except IOError:
            print(f"Помилка читання файлу '{file_path}'.")
    return result

# Приклад використання
if __name__ == "__main__":
    files = ["apache_logs.txt", "filtered_ips.txt"]
    hashes = generate_file_hashes(*files)
    print(hashes)