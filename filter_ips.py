def filter_ips(input_file_path, output_file_path, allowed_ips):
    ip_counts = {}

    try:
        with open(input_file_path, 'r') as infile:
            for line in infile:
                parts = line.strip().split()
                if parts:
                    ip = parts[0]
                    if ip in allowed_ips:
                        ip_counts[ip] = ip_counts.get(ip, 0) + 1

        try:
            with open(output_file_path, 'w') as outfile:
                for ip, count in ip_counts.items():
                    outfile.write(f"{ip} - {count}\n")
        except IOError:
            print(f"Помилка запису до файлу '{output_file_path}'.")

    except FileNotFoundError:
        print(f"Вхідний файл '{input_file_path}' не знайдено.")
    except IOError:
        print(f"Помилка читання вхідного файлу '{input_file_path}'.")

    return ip_counts


if __name__ == "__main__":
    allowed_ips = ['71.212.224.97', '108.174.55.234']
    result = filter_ips("apache_logs.txt", "filtered_ips.txt", allowed_ips)
    print("Результати фільтрації IP-адрес:")
    for ip, count in result.items():
        print(f"{ip} — {count} разів")
