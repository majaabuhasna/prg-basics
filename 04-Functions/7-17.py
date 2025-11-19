def f(palindrome):
    palindrome = str(palindrome)
    palindrome_reversed = palindrome[::-1]
    if palindrome == palindrome_reversed:
        return True
    else:
        return False

print(f("radar"), f("12-11-21"), f("book"), sep="\n")