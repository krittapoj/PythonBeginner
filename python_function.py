x = "awesome" #Global Variables

def myfunc():
    #global x "สามารถใช้ global ทำให้ Variables ให้ข้างนอกได้"
    x = "fantastic" #Local Variables ไม่สามารถเอไปใช้ข้างนอก funciton ได้
    print("Python is " + x)
    
myfunc()

print("Python is " + x)

#------------------------------------------------------------------
def myFunction(fname = "Krittapoj"): #ในวงเล็บเป็นตัวรับค่าส่งไปให้ที่เราเรียก function ถ้ากำหนดค่าไว้แล้วไม่จำเป็นต้องส่งค่าไปที่function
    print(fname + "John")
    
myFunction() #ในวงเล็บจะเป็นตัวรับค่าจากfunction

#-------------------------------------------------------------------
def myFunction2(x):
    return 5 * x
print(myFunction2(5))