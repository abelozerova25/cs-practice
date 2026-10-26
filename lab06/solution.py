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

