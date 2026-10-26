def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}

    for path in paths:
        filename = path.split("/")[-1]
        extension = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""

        if extension in result:
            result[extension] += 1
        else:
            result[extension] = 1

    return result


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""

    return max(paths, key=lambda path: (-path.count("/"), path))[0]


def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]

    if n_bytes < 1024:
        return f"{n_bytes} Б"

    size = float(n_bytes)
    unit_index = 0

    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1

    return f"{size:.1f} {units[unit_index]}"

