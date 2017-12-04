def sum(start, end):
    if(start>end):
        print("Start should be lesser than end")
        return #here we are not returning any value so a special value None is returned
    result=0
    for i in range(start, end+1):
        result+=i
    return result

resultfromFun = sum(5,1)
print("Result : ", resultfromFun)