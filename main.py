# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.





# Press the green button in the gutter to run the script.
F1 = 1
F2 = 1
i = 2
n= int(input("Количество элементов ряда Фибоначчи: "))
array = [F1,F2]
print(array)
while i < n :
    sum = F1+F2
    print(sum)
    F1= F2
    F2 = sum
    i=i+1
    array.append(sum)
print(array)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
