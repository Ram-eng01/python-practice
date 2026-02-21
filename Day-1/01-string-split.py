text = "I am learning devops, aws, python"


word = text.split()

word1 = text.split(",")

word2 = text.split(" ")

print("Words:", word)
print("Words:", word1)
print("Words:", word2)


arn = "arn:aws:ec2:*:123456789012:volume/rammohan"
print(arn.split("/")[1])