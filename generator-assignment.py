# This generator function yields an infinite sequence of Fibonacci numbers.
def infinite_sequence_fibonacci():
    a, b= 0,1
    while True:
        yield a
        a, b = b, a + b

n_fib= infinite_sequence_fibonacci()
for _ in range(10):
    print(next(n_fib))

# This generator function yields an infinite sequence of multiples of a given number n.
def infinite_multiples(n):
    """Generate an infinite sequence of multiples of n."""
    multiple = n
    while True:
        yield multiple
        multiple += n

mltiple_n = infinite_multiples(3)

for _ in range(10):
    print(next(mltiple_n))

# This generator function yields a specified word a given number of times.
def repeat_word(word, times):
    for _ in range(times):
         yield word

words = repeat_word("hello", 3)

for w in words:
    print(w)