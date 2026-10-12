def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Должно быть ровно 3 поля")
        
    city = parts[0].strip()
    temp_str = parts[1].strip()
    date = parts[2].strip()
    
    if not city or not date:
        raise ValueError("Город или дата пустые")
        
    try:
        # Заменяем запятую на точку на случай формата "-3,5"
        temperature = float(temp_str.replace(",", "."))
    except ValueError:
        raise ValueError("Температура не число")
        
    return {"city": city, "temperature": temperature, "date": date}

def read_valid(lines: list) -> list:
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
    if not records:
        return {}
        
    total_temps = {}
    counts = {}
    for record in records:
        city = record["city"]
        temperature = record["temperature"]
        total_temps[city] = total_temps.get(city, 0.0) + temperature
        counts[city] = counts.get(city, 0) + 1
        
    averages = {}
    for city in total_temps:
        averages[city] = round(total_temps[city] / counts[city], 1)
    return averages

def warmest_city(records: list) -> str:
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