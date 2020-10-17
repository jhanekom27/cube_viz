def load_text(path_to_text):
    with open(path_to_text, "r") as f:
        text = f.read()
    return text
