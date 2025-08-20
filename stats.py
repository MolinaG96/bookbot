# función para contar la cantidad de palabras de un texto
def count_words(text: str):
    words = text.split()
    return len(words)

# contador de caracteres y espacios
def count_chars_and_spaces(text: str):
    lower_text = text.lower()
    total_chars = {}
    for char in lower_text:
        total_chars[char] = total_chars.get(char, 0) + 1
    return total_chars

# lista de diccionario ordenada
def list_of_chars(dict: dict[str, int]):
    sorted_list = []
    for char, count in dict.items():
        sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True, key=lambda x: x["num"])
    return sorted_list