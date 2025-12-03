numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
print(min(numbers))
print(max(numbers))

setn = {5, 10, 3, 15, 2, 20}
print(min(setn))
print(max(setn))

def tuple_of_word_by_length(words):
    output = (min(words, key=len), max(words, key=len))
    return output

words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
print(tuple_of_word_by_length(words))