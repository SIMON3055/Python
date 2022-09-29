s = "I am working on reversing a string"
s1="Let's take LeetCode contest"

s3 = "abcdefg"
k = 2
class solution:
    def reverse(s):
        words = s.split(' ')
        s = []
        for word in words:
            s.append(word[::-1])

        return (' '.join(s))

    print(reverse(s))
    print(reverse(s1))

