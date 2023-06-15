#Refactoring CodeWar Problems for better Time Complexity

#Question 1 Link: https://www.codewars.com/kata/52bc74d4ac05d0945d00054e
def first_non_repeating_letter(s):
    d = {}

    for letter in s:
        if letter.lower() not in d:
            if letter.lower() != letter:
                d[letter.lower()] = 1.5
            else:
                d[letter.lower()] = 1
        else:
            if letter.lower() != letter:
                d[letter.lower()] += 1.5
            else:
                d[letter.lower()] += 1
            

    for key, values in d.items():
        if values == 1:
            return key
        elif values == 1.5:
            return key.upper()
        
    return ""  
        
#         for letter in s:
#             if letter.lower() == key:
#                 if values == 1:
#                     return letter
     
# Originally, under the second for loop, I had the above code, which led to a nested for loop,
# which was quadratic. Now, with the new solution, it became a linear problem.
     
print(first_non_repeating_letter("sTreSS"))


# Question 2 Link: https://www.codewars.com/kata/5264d2b162488dc400000001
def spin_words(sentence):
    str_list = sentence.split(' ')
    print(str_list)
    new_sen = []
    for word in str_list:
        if len(word) >= 5:
            new_sen.append(word[::-1])
        else:
            new_sen.append(word)
    return " ".join(new_sen)

#     str_list = sentence.split(' ')
#     new_sen = []
#     for word in str_list:
#         if len(word) >= 5:
#             new_string = ""
#             for i in range(len(word)-1, -1, -1):
#                 new_string += word[i]
#             new_sen.append(new_string)
#         else:
#             new_sen.append(word)
    
#     return " ".join(new_sen)

# For this problem I rewrote the entire problem (code above) as it was originally a quadratic solution with the
# nested loops. With 1 for loop, this has now become linear.

print(spin_words("Hey fellow warriors"))


#Question 3 Link: https://www.codewars.com/kata/55c04b4cc56a697bb0000048
def scramble(s1, s2):
    d = {}
    #Linear 
    for letter in s1:
        #Constant
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1
    #Linear
    for letter in s2:
        #Constant
        if letter not in d:
            return False
        else:
            d[letter] -= 1
    #Linear
    for values in d.values():
        #Constant
        if values < 0:
            return False
    return True

print(scramble('cedewaraaossoqqyt', 'codewarstt'))