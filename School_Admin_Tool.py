
import csv

def write_csv(info_list):
    with open('stud_info.csv', 'a', newline='\n') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name", "Age", "Contact Number", "Email ID"])
        writer.writerow(info_list)
        
if __name__=='__main__':      
    a=True
    stud_num=1
    while a:
        stud_info = input("\n\n  Enter student information for student #{}(format: Name Age Contact_No. Email_ID): ".format(stud_num))
        
        stud_split_list = stud_info.split(' ')
        
        print("  The entered information is - \n\tName: {}\n\tAge: {}\n\tContact Number: {}\n\tEmail ID: {} ".format(stud_split_list[0],stud_split_list[1],stud_split_list[2],stud_split_list[3]))
        
        final=input("\n\t\t  Is the entered information correct? (yes/no): ")

        if final=="yes":
            write_csv(stud_split_list)

            add = input("\n  Do you want to add another student information (yes/no): ")
            if add == "yes" or add == "Yes":
                a = True
                stud_num+=1
            elif add == "no" or add == "No":
                a = False
        elif final=="no":
            print("\t\t  Please re-enter the values --")
