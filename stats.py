def get_num_words(book):
    with open(book) as f:
        file_content = f.read()
        word_count = len(file_content.split())
        print(f"Found {word_count} total words")

def get_num_chars(book):
    charDict = {}
    with open(book) as f:
        file_content = f.read()
        for char in file_content.lower():
            if char in charDict:
                charDict[char] +=1
            else:
                charDict[char] = 1
    for key, value in charDict.items():
        key = key+":"
        print(key, value)
