#include "isogram.h"

int position_of_letter_in_alphabet(char c);

bool is_isogram(const char phrase[]) {

    if (!phrase) return false;

    bool alphabet[26] = {false};

    for (int i = 0; phrase[i]; ++i) {
        int position = position_of_letter_in_alphabet(phrase[i]);
        if (position >= 0) {

            // if this letter occurred before, this phrase is not an isogram.
            if (alphabet[position]) return false;

            // otherwise remember occurrence of this letter
            alphabet[position] = true;
        }
    }
    return true;
}

/**
 * When a letter is in the alphabet (ascii), return its position.
 *
 * first is 0, last is 25
 * not in alphabet is -1
 *
 * @param c the letter
 * @return the position in the alphabet; -1 when argument is no ascii letter
 */
int position_of_letter_in_alphabet(char c) {
    if (c >= 'a' && c <= 'z') return c - 'a';
    if (c >= 'A' && c <= 'Z') return c - 'A';
    return -1;
}