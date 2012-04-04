#!/usr/bin/env python

UNITS = ["zero", "one", "two", "three", "four", "five",
         "six", "seven","eight", "nine", "ten",
         "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
         "sixteen", "seventeen", "eighteen", "nineteen"]
        
TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", 
        "eighty", "ninety"]

POWERS = {10 ** 3: "thousand",
          10 ** 6: "million",
          10 ** 9: "billion",
          10 ** 12: "trillion",
          10 ** 15: "quadrillion",
          10 ** 18: "quintillion",
          10 ** 21: "sextillion",
          10 ** 24: "septillion",
          10 ** 27: "octillion",
          10 ** 30: "nonillion",
          10 ** 33: "decillion"}


def int_to_words(value):
    """Converts integers to English number strings.
    
    >>> int_to_words(5)
    'five'
    >>> int_to_words(16)
    'sixteen'
    >>> [int_to_words(i**2) for i in xrange(5, 10)]
    ['twenty-five', 'thirty-six', 'forty-nine', 'sixty-four', 'eighty-one']
    >>> int_to_words(123)
    'one hundred and twenty-three'
    >>> int_to_words(2345)
    'two thousand three hundred and forty-five'
    >>> int_to_words(34567)
    'thirty-four thousand five hundred and sixty-seven'
    >>> int_to_words(456789)
    'four hundred and fifty-six thousand seven hundred and eighty-nine'
    >>> int_to_words(5678901)
    'five million six hundred and seventy-eight thousand nine hundred and one'
    >>> int_to_words(-1000001)
    'minus one million and one'
    
    """
    # Special case for zero
    if value == 0:
        return UNITS[0]
    
    # Start building word representation
    word_rep = ""
    if value < 0:
        word_rep += "minus"
        value = abs(value)
    
    # First, handle powers of ten until you get to a number less than 1000
    while True:
        current_power = _highest_power(value)
        if not current_power:
            # Less than 1000
            break
        
        # How many of this power do we have? e.g. for 123,000 we have:
        # current_power = 1000, power_count = 123
        power_count = value / current_power
        if power_count > 999:
            raise OverflowError("Can't handle numbers over %i" %
                                (current_power * 1000 - 1))
        
        # Add the string
        power_count_words = _small_int_to_words(power_count)
        if word_rep:
            word_rep += " "
        word_rep += "%s %s" % (power_count_words, POWERS[current_power])
        
        # Don't consider this power any more
        value -= current_power * power_count
    
    if value:
        # For numbers like 1001 we need to add "and"
        if value < 100 and word_rep:
            word_rep += " and"
        
        # Handle remaining digits
        if word_rep:
            word_rep += " "
        word_rep += _small_int_to_words(value)
    
    return word_rep
        
def _small_int_to_words(value):
    """Convert an integer that's smaller than 1000 to words.
    
    >>> _small_int_to_words(5)
    'five'
    >>> _small_int_to_words(16)
    'sixteen'
    >>> _small_int_to_words(123)
    'one hundred and twenty-three'
    
    """
    if not 0 < value < 1000:
        raise ValueError("Value must be in range 0-999")
    
    # Start building word representation
    word_rep = ""
    
    # Special case for zero
    if value == 0:
        return UNITS[0]
    
    # Count the hundreds
    for i in xrange(9, 0, -1):
        if value >= i * 100:
            word_rep += UNITS[i]
            word_rep += " hundred"
            if not value == i*100:
                word_rep += " and "
            value -= i*100
            break
    
    # Tens
    for i in xrange(9, 1, -1):
        if value >= i * 10:
            word_rep += TENS[i - 2]
            if not value == i * 10:
                word_rep += "-"
            value -= i * 10
            break
    
    for i in xrange(1, 20):
        if value == i:
            word_rep += UNITS[i]
            break
    
    return word_rep

def _highest_power(value):
    """The highest named power of ten (thousand, million, billion etc.)
    that's greater than the value.
    
    """
    for power_value in sorted(POWERS.keys(), reverse=True):
        if power_value <= value:
            return power_value
    return 0


def main():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    main()