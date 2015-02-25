The main logic behind the module is to generate random numbers and with every url associate that random number with it.And the convert that number to the base 62.

Why 62?

Let me explain.If we combine lowercase, uppercase and the numbers we get 62 characters in total
('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz').

So converting that number into a base 62 format would give us a number which would consist of uppercase or lowercase or numbers.


For example, if we convert 12 to the base 62 we would get C(index of the character in the string), or if we convert 63 to the base 62 we would get 10 as the result.
So hashing these numbers to a unique value and by assigning them to specific string or urls in this case, our problem can be solved. We can store both the enteries in the db and then while decoding we can read the particular url's value for a particular hash.
I have used  sqlite as the database in the module

How to Use it?

You can run this command in the terminal:
python ShortLy.py <url to encode or decode>

Or you can import this module and can
Encode it using "ShortLy.encode_url(<url to encode>)"


To decode it you can use "ShortLy.py.decode_url(<url to decode>)"
