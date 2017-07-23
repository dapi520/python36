number = 60
flag = False
while flag == False:
    guess = int(input('Enter on integer : '))
    if guess == number:
        flag = True
        print("all right!")
    elif guess > number:
        print(">")
    elif guess < number:
        print("<")
print("done")
# dict = {'a':1,'b':2}
# for ele in dict:
#     print(ele)
#     print(dict[ele])
