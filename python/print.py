phrase = {'0D': 9, '0R': 9, '0Z': 5, '0S': 5, '0Y': 9, '0H': 8, '0V': 8, '0J': 7, '0W': 5, '0F': 9, '0U': 6, '0X': 9, '0T': 9, '0C': 3, '0K': 6, '0M': 5, '0Q': 12, '0B': 7, '0A': 5, '0N': 7, '0E': 5, '0P': 7, '0G': 9}
#limitedWords = phrase.split(",")
count = 1
bigSum = 0
for i in phrase.values():
    bigSum += i
print(bigSum)
