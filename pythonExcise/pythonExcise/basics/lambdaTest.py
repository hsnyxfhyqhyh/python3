#lamda is the key word to tell the system we are going to create anonymous function, 
#for parameter x we want to calculate 3*x +1

g = lambda x: 3*x +1
print(g(2))

#lamda to handle multiple parameters: 
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

print(full_name(" Yinghui ", "HU"))

#lambda is used for one line of function definition 
# for example if having a list authors, we want to sort all authors in the list with last name only

scifi_authors = ["Isaac Asimove", "Ray Bradbury", "Rober Heinlein", "Arts C. Clark", "Frank Erbert", "Orson Scott Card"]

# we are going to create a lambda function and use it directly into the sort function. 
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower() )
print (scifi_authors)

# the output is like this: ['Isaac Asimove', 'Ray Bradbury', 'Orson Scott Card', 'Arts C. Clark', 'Frank Erbert', 'Rober Heinlein']

#if you go deeper, you can have nested lambda function. 
def build_quadratic_function(a, b, c):
    """returns the function f(x) = ax^2 + bx + c"""
    return lambda x: a*x**2 + b*x + c

f = build_quadratic_function(2, 3, -5) 
print (f(0))        # -5
print (f(1))        # 0 
print (f(2))        # 9