#write a python program to print first 25 integerz using loop
print("Before")
count:int = 1
while count <= 25:
    print("Integer !" , count)
    count = count + 1
print("After")

#write a python program to print 10 even numberz using loops
count:int = 1
while count <= 10:
    print( 2 * count)
    count = count + 1

#write a python program to insert values in list
studentNames=["Saad" , "Ali" , "Imran" , "Hassan" , "Moiz"]
print(studentNames)
studentNames.insert(2,"Ahmed")
print(studentNames)

#write a program to add and remove various items from the shoppig cart
#FOR ADDING VALUES
shoppingCart = ["Ghee" , "Oil" , "Kethup" , "ToothPaste" ]
print(shoppingCart)
shoppingCart.append("Mayonize")
print(shoppingCart)
shoppingCart.insert(0,"Cold Drink")
print(shoppingCart)
#FOR REMOVING VALUES
shoppingCart = ["Ghee" , "Oil" , "Kethup" , "ToothPaste" ]
print(shoppingCart)
shoppingCart.remove("Kethup")
print(shoppingCart)
shoppingCart.pop(0)
print(shoppingCart)


#write a python program to find the sum of the numberz in the array
nums = [ 10, 20, 30, 40, 50]
for num in nums:
    result = nums[0] + nums[1] + nums[2] + nums[3] + nums[4]
print(result)


#write a python program to remove all the odd numbers from the array
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums)
nums.remove(1)
print(nums)
nums.remove(3)
print(nums)
nums.remove(5)
print(nums)
nums.remove(7)
print(nums)
nums.remove(9)
print(nums)


#write the factorial of the given number using function
def factorial(n: int) -> int:
    result = 1
    while n > 0:
        result *= n
        n -= 1
    
    return result
number:int = int(input("Enter the NUMBER : "))
print(f"The Factoral of {number} is {factorial(number)}")




#write a python program which converts temp from celsius to farenhit
celsius1:int = int(input("Enter the Temp 1: "))
celsius2:int = int(input("Enter the temp 2: "))
celsius3:int = int(input("Enter the temp 3: "))
celsiusTemp:list[int] = [celsius1 , celsius2 , celsius3]
def celsius1ToFarenhit1():
    farenhit1 = ( celsius1 * 9/5 ) + 32
    return farenhit1
def celsius2ToFarenhit2():
    farenhit2 = ( celsius2 * 9/5 ) + 32
    return farenhit2
def celsius3ToFarenhit3():
    farenhit3 = ( celsius3 * 9/5 ) + 32
    return farenhit3
celsius1ToFarenhit1()
celsius2ToFarenhit2()
celsius3ToFarenhit3()
farenhitTemp:list[int] = [celsius1ToFarenhit1() , celsius2ToFarenhit2() , celsius3ToFarenhit3() ]
print(farenhitTemp)