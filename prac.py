"""
input string of text
store each word
if statement is stored +1 dict
count how many times word is repeated

"""




def main():
    text = " this is a collection of words of nice words this is a fun thing it is"
    # text = input("text: ")
    word_list = text.split()
    count_dict = {}
    for word in word_list:
        count_dict[word] = count_dict.get(word,0)+1
    # print(count_dict)
    max_length = max([len(word) for word in count_dict.keys()])

    for word in sorted(count_dict.keys()):
        print("{:{}} : {}".format(word, max_length, count_dict[word]))


main()