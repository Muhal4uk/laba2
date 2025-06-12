import hashlib
import sys

def generate_file_hashes(*file_paths):
    hashes = {}
    for path in file_paths:
        try:
            with open(path, 'rb') as file:
                content = file.read()
                sha256 = hashlib.sha256(content).hexdigest()
                hashes[path] = sha256
        except FileNotFoundError:
            print(f"Файл '{path}' не знайдено.")
        except IOError:
            print(f"Помилка читання файлу '{path}'.")

    return hashes


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть хоча б один файл як аргумент командного рядка.")
    else:
        file_paths = sys.argv[1:]
        result = generate_file_hashes(*file_paths)
        print("SHA-256 хеші файлів:")
        for path, hash_val in result.items():
            print(f"{path} — {hash_val}")
