def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    score = {}
    try:
        for word in wordList:
            if isValidWord(word, hand, wordList):
                score[word] = score.get(word, 0) + getWordScore(word, n)
        return max(score, key = score.get)
    except:
        return None
