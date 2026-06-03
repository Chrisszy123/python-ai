import sentiments
# get input

text = input("Enter a sentence: ").lower()

words = text.split()


print(words)

#count the positive and negatiive words

negative_count = 0
positive_count = 0

#track the words we found
found_negative =[]
found_positive = []

for word in words: 
    if word in sentiments.positive_words:
        positive_count += 1
        found_positive.append(word)
    elif word in sentiments.negative_words:
        negative_count += 1
        found_negative.append(word)
    else:
        pass

if positive_count > negative_count:
    print("The sentiment is positive")
elif negative_count > positive_count:
    print("The sentiment is negative")
else:
    print("The sentiment is neutral")

scores = {
    "positive": positive_count,
    "negative": negative_count
}

print(scores)
print("Found positive words: ", found_positive)
print("Found negative words: ", found_negative)