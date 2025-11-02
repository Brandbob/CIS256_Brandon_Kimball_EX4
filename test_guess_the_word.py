from guess_the_word import select_word, is_letter_in_current_word, word_list

def test_select_word():
    assert select_word() in word_list

def test_is_letter_in_current_word():
    word = select_word()
    letter = word[0]
    assert is_letter_in_current_word(letter) == True
