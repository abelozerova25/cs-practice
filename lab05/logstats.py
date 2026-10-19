def parse_event(line: str) -> dict:
    if not line:
        raise ValueError("Empty line")
    cleaned_line = line.rstrip('\r\n')
    parts = cleaned_line.split(' ', 2)
    if len(parts) < 3:
        raise ValueError("Invalid format")
    time, level, message = parts
    if level not in {'DEBUG', 'INFO', 'WARNING', 'ERROR'}:
        raise ValueError("Invalid level")
    return {"time": time, "level": level, "message": message}

def count_levels(lines) -> dict:
    counts = {"BROKEN": 0}
    for line in lines:
        # Проверяем, если строка совсем пустая
        if not line or not line.strip():
            continue
        try:
            event = parse_event(line)
            lvl = event["level"]
            counts[lvl] = counts.get(lvl, 0) + 1
        except ValueError:
            counts["BROKEN"] += 1
    return counts

def top_errors(lines, n: int) -> list[list]:
    error_counts = {}
    for line in lines:
        if not line or not line.strip():
            continue
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:
            continue
    sorted_errors = sorted(error_counts.items(), key=lambda x: (-x, x))
    return [[msg, count] for msg, count in sorted_errors[:n]]

def format_report(counts: dict, errors: list[list]) -> str:
    report = ["Отчёт по журналу", ""]
    # Выводим сначала все уровни кроме BROKEN по алфавиту
    for level in sorted(counts.keys()):
        if level != "BROKEN":
            report.append(f"{level}: {counts[level]}")
    # BROKEN обязательно выводим в самом конце списка уровней
    if "BROKEN" in counts:
        report.append(f"BROKEN: {counts['BROKEN']}")
    report.append("")
    report.append("Частые ошибки:")
    for msg, count in errors:
        report.append(f"- {msg} - {count}")
    report.append("")
    return "\n".join(report)