# (c) hughes

import re
from collections import defaultdict

# 1. Read book into string
def readbook(Alice, clean=True):
    with open("Lab 2/Alice.txt", 'r') as f:
        data = f.read().replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    if clean:
        data = data.replace(';', ' ').replace(',', ' ').replace(':', ' ')
        data = data.replace('-', ' ').replace('"', '').replace("'", "").lower()
    return data

# 2. Get list of sentences
def get_sentences(text):
    return [s.strip() for s in text.split('.') if s.strip()]

# 3. Count words per sentence
def count_words(sentences):
    total_words = sum(len(s.split()) for s in sentences)
    return total_words / len(sentences), total_words

# 4. Count characters per word + 1–20 word lengths
def count_chars_and_word_lengths(sentences):
    total_chars = 0
    length_freq = [0] * 21
    all_words = []

    for sentence in sentences:
        words = sentence.split()
        all_words.extend(words)
        for word in words:
            length = len(word)
            total_chars += length
            if length <= 20:
                length_freq[length] += 1

    avg_word_length = total_chars / len(all_words)
    return avg_word_length, length_freq, all_words

# 5. Top 100 most common words
def top_100_words(words):
    count = defaultdict(int)
    for word in words:
        count[word] += 1
    return sorted(count.items(), key=lambda x: x[1], reverse=True)[:100]

# Run stats
if __name__ == "__main__":
    for book in ["Alice.txt", "The Strange Case.txt"]:
        print(f"\n📘 {book}")
        text = readbook(book)
        sentences = get_sentences(text)

        avg_sentence_length, total_words = count_words(sentences)
        avg_word_length, word_len_dist, all_words = count_chars_and_word_lengths(sentences)
        top_100 = top_100_words(all_words)

        print(f"Average sentence length: {avg_sentence_length:.2f} words")
        print(f"Average word length: {avg_word_length:.2f} chars")
        print(f"Word length distribution (1–20): {word_len_dist[1:]}")
        print(f"Top 100 words: {[word for word, _ in top_100]}")
