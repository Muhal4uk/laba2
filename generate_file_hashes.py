import hashlib

def generate_file_hash(file_path):
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            sha256 = hashlib.sha256(content).hexdigest()
            return sha256
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    except IOError:
        print(f"Помилка читання файлу '{file_path}'.")

    return None


if __name__ == "__main__":
    file_path = "apache_logs.txt"  # 👉 тут вкажи свій файл
    hash_result = generate_file_hash(file_path)
    
    if hash_result:
        print(f"SHA-256 хеш файлу {file_path}:")
        print(hash_result)
