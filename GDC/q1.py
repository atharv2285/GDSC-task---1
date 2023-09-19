def check_characters(s1, s2):
    
    s1 = s1.lower()
    char_set = set(s2)

    for char in s1:
        if char not in char_set:
            return "No"
    
    return "Yes"

s1 = input("Enter first string ")
s2 = input("Enter second string ")

ans = check_characters(s1, s2)
print(ans)




