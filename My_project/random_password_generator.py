import string
import random

# requirements: 1 to 3 uppercase and 1 to 3 punctuation is required for the password
'''
digits        : 0-9
ascii_letters : uppercase letters and lowercase letters
punctuation   : !"#$%&'()*+,-./:;<=>?@[\]^_{|}~
'''
lower_and_digits = string.digits + string.ascii_lowercase
uppercase = string.ascii_uppercase
punctuation = string.punctuation

# length of password bewteen 10 to 16
len = random.randrange(10,17)

# length of each part of password
uppercase_len = random.randrange(1,4)
punctuation_len = random.randrange(1,4)
lower_and_digits_len = len - uppercase_len - punctuation_len

# generate password
password = random.choices(uppercase, k = uppercase_len) + \
           random.choices(punctuation, k = punctuation_len) + \
           random.choices(lower_and_digits, k = lower_and_digits_len)
random.shuffle(password)
password = "".join(password)

print(password," with length ",len)
