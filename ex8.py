formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
        "Try your",
        "Own text here",
        "Maybe a poem",
        "Or a song about fear"
))


# We define formatter and then pass through it arguments in the spaced format
#that it is defined as. In the last example, we are passing 4 strings. If we were
# to only pass 3 string the print command would fail?
# Yeah, it does. And error message is "tuple index out of range"
#
