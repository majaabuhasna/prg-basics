def f(palindrome):
    palindrome = str(palindrome)
    palindrome_reversed = palindrome[::-1]
    if palindrome == palindrome_reversed:
        return print(True)
    else:
        return print(False)

f("radar")
f("12-11-21")
f("book")