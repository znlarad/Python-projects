#Basic binarysearch algorithm
#This code is written by znl_arad
#Code works by continously deviding the stored data in half and by this shorting the arrat until the target element is found and while loop stops there 

def binary_serach(list_of_item,target):#defining the function
    end = (len(list_of_item))
    start = 0
    middle = 0
    print(list_of_item[middle])
    step=0

    while (start<=end):
        step=step+1
        print("step : ",step ,str(list[start:end+1]))
        middle=int((start + end) / 2)

        if target == list_of_item[middle]:
            return middle

        if target < list_of_item[middle]:
            end = middle - 1
        else:
            start = middle + 1

    #return -1




list=[1,2,3,4,5,6,7,8,9,10,11,12]
element=int(input("give me a digit from 1 to 12:"))

binary_serach(list,element)#calling the function


