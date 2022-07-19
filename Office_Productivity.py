from tabnanny import check
from Offices import Location, Retail, Repair, Admin
from Office_Custom_Error import CommaError, DivisibleBy4Error, TooLargeError
import re
import logging

def main():
    logging.basicConfig(filename="Office_Productivity.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')

    print("*** Welcome to the Office Productivity Log ***")

    fname = "regional_offices.csv"
    lst_offices = []
    lst_offices = load_offices(fname)
    logging.info("loaded historic data...")

    while(True):
        print("\nPlease select which operation you want to perform:")
        print("\t1) Veiw Current Information")
        print("\t2) Update Office Data")
        print("\t3) Examine Productivity Ratings")
        print("\t4) Add New Location")
        print("\t5) Exit Productivity Log")
        action_type = input(">>> ")

        if action_type == "1":
            print("\n\n***** All Offices *****")
            for elem in lst_offices:
                print(elem)
        elif action_type == "2":
            lst_offices = edit_offices(lst_offices)
        elif action_type == "3":
            print("\n\n***** OPERATION UNDER DEVELPOMENT *****")
        elif action_type == "4":
            office = insert_office()
            if office == None:
                print("*** DATA INPUT ABORTED. NO OFFICE ADDED ***")
            else:
                lst_offices.append(office)
                logging.info("Added a new Location")
        elif action_type == "5":
            print("\n\nThank you for using the Productivity Log!")
            break
        else:
            print("\n\n***** INVALID INPUT: Please enter 1-5 *****")
        print("\n\nDirecting back to operation menu....")

    

    save_offices(fname,lst_offices)
    logging.info("Saved office data to " + fname)
    print("\n\n")

def save_offices(fname, lst_offices):
    '''
    save_offices

    This function will take in a list of offices and save them to a csv file

    Returns None
    '''
    with open(fname, "w") as f:
        for office in lst_offices:
            if type(office) == Retail:
                f.write("Retail," + office._name + "," + office._manager + "," + str(office._employees) + "," + str(office._hours) + "," + str(office._customers) + "\n")
            elif type(office) == Repair:
                f.write("Repair," + office._name + "," + office._manager + "," + str(office._employees) + "," + str(office._hours) + "," + str(office._customers) + "\n")
            elif type(office) == Admin:
                f.write("Admin," + office._name + "," + office._manager + "," + str(office._employees) + "," + str(office._hours) + "," + str(office._customers) + "\n")
            else:
                pass
    
def load_offices(fname) -> list:
    '''
    load_offices

    This function will take in a file name representing a csv file of offices
    to load into an office list.

    Returns list of offices
    '''
    lst_offices = []
    with open(fname, "r") as f:
        for line in f:
            info = line.split(',')
            if info[0] == "Retail":
                office = Retail(info[1], info[2], info[3], info[4], info[5].strip())
            elif info[0] == "Repair":
                office = Repair(info[1], info[2], info[3], info[4], info[5].strip())
            elif info[0] == "Admin":
                office = Admin(info[1], info[2], info[3], info[4], info[5].strip())
            else:
                office = None
            
            if office != None:
                lst_offices.append(office)
    return lst_offices

def insert_office() -> Location:
    '''
    insert_office

    This function prompts the user for information about what office
    to insert into the journal

    Returns office
    Returns None if user wants to quit
    '''
    print("\nPlease select which type of location is being added:")
    print("\t1) Retail")
    print("\t2) Repair")
    print("\t3) Admin")
    print("\t4) Abort Location Addition")
    office_type = input(">>> ")

    if office_type not in ["1", "2", "3"]:
        return None

    while True:
        try:
            name = input("\nEnter the office name(city):\n>>>")
            check = re.search(",", name)

            if check != None:
                raise CommaError
        except CommaError:
            print("CANNOT HAVE COMMAS IN INPUT!\n")
        else:
             break

    while True:
        try:
            manager = input("\nEnter the manager name:\n>>>")
            check = re.search(",", manager)

            if check != None:
                raise CommaError
        except CommaError:
            print("CANNOT HAVE COMMAS IN INPUT!\n")
        else:
             break


    while True:
        try:
            employees = int(input("\nEnter employee count:\n>>>"))

        except ValueError as ve:
            print("\nCANNOT ENTER A STRING FOR EMPLOYEES! PLEASE ENTER AN INTEGER!\n")
        else:
            break

    while True:
        try:
            hours = int(input("\nEnter hours worked(week):\n>>>"))

        except ValueError as ve:
            print("\nCANNOT ENTER A STRING FOR HOURS! PLEASE ENTER AN INTEGER!\n")
        else:
            break

    if office_type == "1":
            
        while True:
            try:
                customers = int(input("\nEnter tires sold(week):\n>>>"))

                if customers%4 != 0:
                    raise DivisibleBy4Error

            except ValueError as ve:
                print("\nCANNOT ENTER A STRING FOR TIRES! PLEASE ENTER AN INTEGER!\n")
            except DivisibleBy4Error as ve:
                print("\nTIRES MUST BE SOLD IN UNITS OF 4!\n")
                logging.error("Tried to enter an invalid value for tires sold for" + name + " " + manager)
            else:
                break

    elif office_type == "2":
            
        while True:
            try:
                customers = int(input("\nEnter vehicles repaired(week):\n>>>"))
            except ValueError as ve:
                print("\nCANNOT ENTER A STRING FOR VEHICLES! PLEASE ENTER AN INTEGER!\n")
            else:
                break
    
    elif office_type == "3":
        customers = 0
    


    if office_type == "1":
        return Retail(name, manager, employees, hours, customers)
    elif office_type == "2":
        return Repair(name, manager, employees, hours, customers)
    elif office_type == "3":
        print("**** AUTHORIZATION ERROR: New Admin Offices cannot be added through the Productivity Log ****")
        return None
    else:
        return None



def edit_offices(lst) -> Location:
    '''
    edit_offices

    This function allows the user to change the descriptive data for the offices each week or as neccesary

    Takes in a list of offices
    Returns a list of offices
    '''
    while True:
        print("\nPlease select the type of edits you are making:")
        print("\t1) Weekly Update (Edit All Locations)")
        print("\t2) Value Correction (Single Office)")
        print("\t3) Admin Details")
        print("\t4) Done Editing")
        Edit_type = input(">>> ")

    
        if Edit_type == "1":
            
            for office in lst:
                print("\nEditing:", end= " " )
                print(office)
                print(type(office))
                while True:
                    try:
                        office._hours = int(input("\nEnter hours worked(week):\n>>>"))

                    except ValueError as ve:
                        print("\nCANNOT ENTER A STRING FOR HOURS! PLEASE ENTER AN INTEGER!\n")
                    else:
                        break

                if type(office) == Retail:
                        
                    while True:
                        try:
                            office._customers = int(input("\nEnter tires sold(week):\n>>>"))

                            if office._customers%4 != 0:
                                raise DivisibleBy4Error

                        except ValueError as ve:
                            print("\nCANNOT ENTER A STRING FOR TIRES! PLEASE ENTER AN INTEGER!\n")
                        except DivisibleBy4Error as ve:
                            print("\nTIRES MUST BE SOLD IN UNITS OF 4!\n")
                            logging.error("Tried to enter an invalid value for tires sold for" + office._name + " " + office._manager)
                        else:
                            break

                elif type(office) == Repair:
                        
                    while True:
                        try:
                            office._customers = int(input("\nEnter vehicles repaired(week):\n>>>"))
                        except ValueError as ve:
                            print("\nCANNOT ENTER A STRING FOR VEHICLES! PLEASE ENTER AN INTEGER!\n")
                        else:
                            break
        
                elif type(office) == Admin:
                    office._customers = 0
            
        elif Edit_type == "2":
            print("\n\n***** Office Indexes *****")
            i = 0
            for elem in lst:
                print("Index: " + str(i), end= " ")
                print(elem)
                i = i + 1
            
            while True:
                try:
                    selected_index = int(input("\nEnter the Index of the Office you wish to edit:\n>>>"))

                    if selected_index  >= i:
                        raise TooLargeError
                except TooLargeError:
                    print("\nSPECIFIED INDEX NOT IN LIST!\n")
                except ValueError as ve:
                    print("\nCANNOT ENTER A STRING FOR VEHICLES! PLEASE ENTER AN INTEGER!\n")
                else:
                    break

            while True:
                try:
                    manager = input("\nEnter the manager name:\n>>>")
                    check = re.search(",", manager)
                    
                    if check != None:
                        raise CommaError
                except CommaError:
                    print("CANNOT HAVE COMMAS IN INPUT!\n")
                else:
                    lst[selected_index]._manager = manager
                    break


            while True:
                try:
                    employees = int(input("\nEnter employee count:\n>>>"))

                except ValueError as ve:
                    print("\nCANNOT ENTER A STRING FOR EMPLOYEES! PLEASE ENTER AN INTEGER!\n")
                else:
                    lst[selected_index]._employees = employees
                    break

        elif Edit_type == "3":
            print("\n\n***** OPERATION UNDER DEVELPOMENT *****")
        elif Edit_type == "4":
            print("\n\nExiting Editor!")
            return lst
        else:
            print("\n\n***** INVALID INPUT: Please enter 1-5 *****")
        print("\n\nDirecting back to editor menu....")

    

if __name__ == "__main__":
    main()
