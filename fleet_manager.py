def init_database():
    n = ["Jean-luc Picard", "William Riker", "Data", "Beverly Crusher", "Geordi La Forge"]                       #a function with parallel lists with all information.
    r = ["Captain", "Commander", "Lt. Commander", "Commander", "Lieutenant"]
    d = ["Command", "Command", "Operations", "Sciences", "Operations"]
    ids = ["ID1", "ID2", "ID3", "ID4", "ID5"]
    
    return n, r, d, ids


def display_menu():
    student = input("What is your name?: ")

    print("----------------Menu----------------")                      #prints out the options to choose from and retruns the choice, as well as asking the students name.
    print("1. View crew members")
    print("2. Add a member")
    print("3. Remove a crew member")
    print("4. Analyse data")
    print("5. Shutdown System")

    print("Student currently logged in:", student)

    choice = input("select an option: ")

    return choice


def add_member(n, r, d, ids):
    name = input("What is the members name?: ")
    rank = input("What is their rank?:")
    division = input("What division are they in?: ")
    new_ids = input("What is their ID?: ")

    validation_list = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]                       #takes inputs for new member, validates it against created parameters and adds it to the existing lists.

    if new_ids in ids:
        print("ID already exists")
        return
    
    if rank not in validation_list:
        print("Invalid rank")
        return
    
    n.append(name)
    r.append(rank)
    d.append(division)
    ids.append(new_ids)

    print("Member added!")


def remove_member(n, r, d, ids):
    remove = input("Enter the ID to remove a member:")

    if remove in ids:
        idx = ids.index(remove)             #checks against the list in ids and if found is removed from that index, keeps lists synced
        n.pop(idx)
        r.pop(idx)
        d.pop(idx)
        ids.pop(idx)
        print("Member removed.")
    else:
        print("ID not found")


def update_rank(n, r, ids):
    update_id = input("Which ID would you like to update:")               #gets an ID

    if update_id not in ids:
        print("Invalid ID.")                #if the ID is not in list break
        return
    
    idx = ids.index(update_id)
    new_rank = input("Enter a new rank:")        #replaces the current rank with new rank 
    r[idx] = new_rank
    print("Rank has been updated")


def display_roster(n, r, d, ids):
    print("---------------Current Crew---------------")
    
    for i in range(len(n)):
        print(n[i] + " - " + r[i] +  " - " + d[i] + " - " + ids[i])          #prints the memebers in the lists with all attached details in the parallel lists 


def search_crew(n, r, d, ids):
    term = input("Enter a name to search:")

    for i in range(len(n)):
        if term in n[i]:                                                             #checks the term entered 
            print(n[i] + " - " + r[i] + " - " + d[i] + " - " + ids[i])  


def filter_by_division(n, d):
    select = input("Which division would you like Command, Operations, or Sciences?")

    for i in range(len(n)):             
        if d[i] == select:                          #if the selction is in that list it prints the matching memebers
            print(n[i])


def calculate_payroll(r):
    total = 0 

    for rank in r:                           #assigns a value to a rank
        if rank == "Captain":
            total += 1000
        elif rank == "Commander":
            total += 800
        elif rank == "Lt. Commander":
            total += 600
        elif rank == "Lieutenant":
            total += 400
        elif rank == "Ensign":
            total += 200
    
    return total


def count_officers(r):
    count = 0 

    for rank in r:
        if rank == "Captain" or rank == "Commander":           #
            count += 1

    return count


def main():
    n, r, d ,ids = init_database()

    while True:
        choice = display_menu()

        if choice == "1":                                                         #if and else statements for the options chosen and which functions to call.
            display_roster(n, r, d, ids)
        elif choice == "2":
            add_member(n, r, d, ids)
        elif choice == "3":
            remove_member(n, r, d, ids)
        elif choice =="4":
            print("Analysing...")
            print("Total Payroll:", calculate_payroll(r))
            print("High ranking officers:", count_officers(r))
        elif choice == "5":
            print("Shutting down.")
            break
        else:
            print("Invalid option")

main()
            


    
    








    
