
def create_files(input):
    pass # TODO

    file_name = f'files/{input}'
    unique_words = set()
    with open("files/large-words.txt", "w") as file1, open("files/small-words.txt", "w") as file2, open(file_name,"r") as file3:
        for line in file3:
            for word in line.split():
                if len(word) >= 3 and word not in unique_words:
                    file1.write(word + '\n')
                    unique_words.add(word)
                elif len(word) < 3 and word not in unique_words:
                    file2.write(word + '\n')
                    unique_words.add(word)
    return len(unique_words)

def ex3():
    total_words = create_files("words.txt")
    print(f"Total words: {total_words}.")

ex3()