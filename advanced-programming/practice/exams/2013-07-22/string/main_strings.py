from strings import *

if __name__ == "__main__":
    s0 = "The deadline is approximately midnight though it could vary."
    s1 = "She is a fascinating lady; she has an astonishing smile, an alluring voice and an entertaining sense of humor."
    s2 = "The topic is appealing nevertheless the speaker was too monotonous."
    s3 = "The topic ais appealing nevertheless the speaker was too monotonous."
    print(strip(s0, 'aeiou'))
    print(reverse(s0))
    print(strip(reverse(s0), 'aeiou'))
    print(split(s1, ' ;,.'))
    print(reverse(s2))
    print("tests on find:")
    print()
    print(find(s2, 'a'))
    print(find(s2, 'a'))
    print(find(s2, 'a'))
    print(find(s3, 'a'))
    print(find(s3, 't'))
    print(find(s3, 't'))
    print(find(s3, 't'))
    print(find(s3, 't'))
    print(find(s3, 't'))
    print(find(s3, 't'))
    print(find(s3, 't'))
