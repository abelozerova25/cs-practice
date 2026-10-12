def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("В строке должно быть ровно три поля!")
        
    city = parts[0].strip()
    temp_str = parts[1].strip()
    date = parts[2].strip()
    
    if city == "" or date == "":
        raise ValueError("Город или дата не могут быть пустыми!")
        
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError("Температура должна быть правильным числом!")
        
    return {"city": city, "temp": temp, "date": date}

def read_valid(lines: list[str]) -> list[dict]:
    good_records = []
    for line in lines:
        cleaned_line = line.strip()
        if cleaned_line == "":
            continue
        try:
            record = parse_record(cleaned_line)
            good_records.append(record)
        except ValueError:
            continue
    return good_records

def average_by_city(records: list[dict]) -> dict:
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

def warmest_city(records: list[dict]) -> str:
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