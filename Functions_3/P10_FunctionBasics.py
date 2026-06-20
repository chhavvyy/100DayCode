'''Create a function called format_name() that takes two inputs: f_name and `l_name ,
Use the title() function to modify the f_name and l_name parameters into Title Case.'''



def format_name(f_name , l_name):
    print(f_name.title())
    print(l_name.title())

format_name("chhaviie" , "vyas")



#another way to write this is
#---------------------------------------------------------------------------------------------------------------|


def format_name(f_name , l_name):
    x=f_name.title()
    y=l_name.title()
    print(f"{x} , {y}")


format_name("chhaviie" , "vyas")