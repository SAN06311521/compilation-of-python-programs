class rev_sol:
    def rev_word(s):
        return ' '.join(reversed(s.split()))

str = input("Enter the sentence to be reversed: ")
print(rev_sol.rev_word(str))
