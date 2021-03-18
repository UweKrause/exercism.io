#ifndef ISOGRAM_H
#define ISOGRAM_H

#include <stdbool.h>

/**
  * An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter.
  *
  * Spaces and hyphens are allowed to appear multiple times.
  * Currently only works for ascii: umlauts or accents are silently ignored.
  *
  * @param phrase Phrase to check if it is an isogram
  * @return true if isogram; false otherwise
  */
bool is_isogram(const char phrase[]);

#endif
