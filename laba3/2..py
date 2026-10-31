try:
    text = input("Введите текст: ")
    word = input("Введите заданное слово: ")

    text_clean = ""
    for i in range(len(text)): #нижний регистр
        char = text[i].lower()
        if char == "." or char == "," or char == "!" or char == "?":
            text_clean += " "
        else:
            text_clean += char

    text_clean += " "
    word_lower = word.lower()

    count = 0  
    current_word = "" 

    for i in range(len(text_clean)):
        if text_clean[i] != " ":

            current_word += text_clean[i]
        else:
            if current_word == word_lower and current_word != "":
                count += 1
            current_word = "" 

    print("Слово встречается в тексте столько раз:", count)

except ValueError:
    print("ERROR")