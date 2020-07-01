
num=input("\n\tEnter some numbers(separated with a space): ")
new_list=num.split(' ')
print("\tEntered list:",new_list)
size=len(new_list)

new_list2=[]

i=0
while i<size:
    try:
        if float(new_list[i])>=0:
            new_list2.append(new_list[i])
        elif float(new_list[i])<0:
            pass
    except ValueError:
        print("\n\tPlease enter numbers only!! -----")
        new_list2.clear()
        break
    i+=1

if len(new_list2)==0:
    pass
else:
    print("\n\tList of positive numbers:",new_list2)
