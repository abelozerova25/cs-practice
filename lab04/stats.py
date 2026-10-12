def parse_record(line: str) -> dict:
    # Тесты: parse_record("Азов;24.5;2026-07-01") и с пробелами " Азов ; -3,5 ; 2026-01-09"
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Должно быть ровно 3 поля")
        
    city = parts[0].strip()
    temp_str = parts[1].strip()
    date = parts[2].strip()
    
    if not city or not date:
        raise ValueError("Город или дата пустые")
        
    try:
        # Заменяем запятую на точку, если в тесте температуру передали как "-3,5"
        temp = float(temp_str.replace(",", "."))
    except ValueError:
        raise ValueError("Температура не число")
        
    return {"city": city, "temp": temp, "date": date}

def read_valid(lines: list) -> list:
    # Тесты: read_valid(["..."]), read_valid([]), строки с пробелами
    good_records = []
    for line in lines:
        cleaned = line.strip()
        if not cleaned:
            continue
        try:
            record = parse_record(cleaned)
            good_records.append(record)
        except ValueError:
            continue
    return good_records

def average_by_city(records: list) -> dict:
    # Тесты: average_by_city([]), обычные списки словарей
    if not records:
        return {}
        
    total_temps = {}
    counts = {}
    for record in records:
        city = record["city"]
        temp = record["temp"]
        total_temps[city] = total_temps.get(city, 0.0) + temp
        counts[city] = counts.get(city, 0) + 1
        
    averages = {}
    for city in total_temps:
        averages[city] = round(total_temps[city] / counts[city], 1)
    return averages

def warmest_city(records: list) -> str:
    # Тесты: warmest_city([...]) для разных городов (Азов, Батайск, Ростов)
    averages = average_by_city(records)
    if not averages:
        return ""
        
    champion_city = ""
    for city in averages:
        if champion_city == "":
            champion_city = city
        elif averages[city] > averages[champion_city]:
            champion_city = city
        elif averages[city] == averages[champion_city] and city < champion_city:
            champion_city = city
    return champion_city