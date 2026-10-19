def parse_event(line: str) -> dict:
    cleaned_line = line.rstrip('\r\n')
    parts = cleaned_line.split(' ', 2)
    if len(parts) < 3:
        raise ValueError("Invalid format")
    time, level, message = parts
    if level not in {'DEBUG', 'INFO', 'WARNING', 'ERROR'}:
        raise ValueError("Invalid level")
    return {"time": time, "level": level, "message": message}

def count_levels(lines) -> dict:
    counts = {"BROKEN": 0, "DEBUG": 0, "ERROR": 0, "INFO": 0, "WARNING": 0}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            counts[event["level"]] += 1
        except ValueError:
            counts["BROKEN"] += 1
    return counts

def top_errors(lines, n: int) -> list[list]:
    error_counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:
            continue
    sorted_errors = sorted(error_counts.items(), key=lambda x: (-x[1], x[0]))
    return [[msg, count] for msg, count in sorted_errors[:n]]

def format_report(counts: dict, errors: list[list]) -> str:
    report = ["Report", ""]
    for level in sorted(counts.keys()):
        report.append(f"{level}: {counts[level]}")
    report.append("")
    report.append("Errors:")
    for msg, count in errors:
        report.append(f"- {msg} - {count}")
    report.append("")
    return "\n".join(report)