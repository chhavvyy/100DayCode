def format_name(f_name, l_name):
    if f_name=="" or l_name=="":
       return
       formated_f_name = f_name.title()
       formated_l_name = l_name.title()
       return f"{formated_f_name} {formated_l_name}"


print(format_name("",""))

#return tells us that its the end of the function , it simply store the result nd return it where as print only display it
# if there's no value it will return None


# and if we tell to print the empty value it will still return, eg
def format_name(f_name, l_name):

       formated_f_name = f_name.title()
       formated_l_name = l_name.title()
       return f"result: {formated_f_name} {formated_l_name}"


print(format_name("", ""))
