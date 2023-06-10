from shakespeare import *

if __name__ == '__main__':
    s0 = 'The deadline is approximately midnight though it could vary.'
    s1 = 'She is a fascinating lady; she has an astonishing smile, an alluring voice and an entertaining sense of humor.'
    s2 = 'The topic is appealing nertheless the speaker was too monotonous.'

    print(replace_synonyms(s0))
    print(replace_synonyms(s1))
    print(replace_synonyms(s2))
