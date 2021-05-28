import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
nato_dic = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("enter a word: ").upper()
nato_word = [nato_dic[letter] for letter in word]
print(nato_word)