def validation(self):
    try:
        with open("test_data.json", "r") as file:
            data = json.load(file)
            return {data}
    except json.JSONDecodeError:
        return f"Error: {file} contains invalid JSON formatting."