def init_database():
    n = ["Jean-luc Picard", "William Riker", "Data", "Beverly Crusher", "Geordi La Forge"]                       #a function with parallel lists with all information
    r = ["Captain", "Commander", "Lt. Commander", "Commander", "Lieutenant"]
    d = ["Command", "Command", "Operations", "Sciences", "Operations"]
    i = ["ID1", "ID2", "ID3", "ID4", "ID5"]
    
    return n, r, d, i

def display_menu():
    student = input("What is your name?: ")

    print("----------------Menu----------------")
    print("1. View crew members")
    print("2. Add a member")
    print("3. Remove a crew member")
    print("4. Analyse data")
    print("5. Shutdown System")

    print("Student currently logged in:", student)

    choice = input("select an option: ")

    return choice






    
