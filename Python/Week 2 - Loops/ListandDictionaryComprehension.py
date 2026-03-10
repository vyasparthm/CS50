import helper_Compresion as hc

def main():
    counts= {}
    words = hc.get_words("Addresses.txt")
    lowercase_words = [word.lower() for word in words if len(word) >7]

    counts = {word: words.count(word) for word in lowercase_words}
    
    # for word in lowercase_words:
    #     if word in counts:
    #         counts[word] += 1
    #     else:
    #         counts[word] = 1
    hc.save_counts(counts)
if __name__ == '__main__':
    main()