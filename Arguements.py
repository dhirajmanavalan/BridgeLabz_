# positional Arguements

# def add(x,y):
#     z=x**y
#     print(z)
# add(2,3)

# # default Arguements

# def sub(x,y=0):
#     z=x+y
#     print(z)
# sub(1)

#keyword Arguements

def add(x,y):
    z=x+y
    print("x",x)
add(y=2,x=1)

#Variable length Arguement

def pizza(*toppings):
    print(toppings)
pizza("a","b","c")

#Variable length keyword Arguement

def pizza1(**toppings):
    print(toppings)
pizza1 (dhiraj="a",dinesh="b",monisha="c")

