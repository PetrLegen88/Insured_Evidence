from insured import Insured


class InsuredEvidence:
    """
    The InsuredEvidence class represents evidence of insured persons and works with them.

    Parameters:
    - user_collection: A list to which new users are added

    Methods:
    - add_insured: Adds a new insured person to the user collection
    - display_all_insured: Displays all stored insured persons in the user collection
    - search_insured: Searches for an insured person by their name and surname
    - start: Starts the application
    """

    def __init__(self):
        self.user_collection = []

    def add_insured(self):
        """
        The method creates an insured person and adds them to the user collection.
        """
        name = input("Enter the name of the insured person: ")
        surname = input("Enter the surname of the insured person: ")
        phone_number = input("Enter the phone number (9 digits): ")
        while not phone_number.isnumeric() or len(phone_number) != 9:
            print("Invalid phone number format!")
            phone_number = input("Enter the phone number (9 digits): ")
        age = input("Enter the age (1-119): ")
        while not age.isnumeric() or int(age) < 1 or int(age) > 119:
            print("Invalid age format!")
            age = input("Enter the age (1-119): ")

        insured_person = Insured(name, surname, phone_number, age)

        self.user_collection.append(insured_person)

        print(f"\nData has been saved. Press any key to continue...\n")
        input()

    def display_all_insured(self):
        """
        The method displays all insured persons stored in the user collection.
        """
        for insured_person in self.user_collection:
            print(
                f"{insured_person.name}   {insured_person.surname}   {insured_person.age}   {insured_person.phone_number}")
        print(f"\nData has been saved. Press any key to continue...\n")
        input()

    def search_insured(self):
        """
        The method searches for an insured person in the user collection by their name and surname.
        """
        name = input("Enter the name of the insured person: ").lower()
        surname = input("Enter the surname of the insured person: ").lower()

        for insured_person in self.user_collection:
            if insured_person.name == name and insured_person.surname == surname \
                    or insured_person.name.lower() == name and insured_person.surname.lower() == surname:
                print(
                    f"\n{insured_person.name}   {insured_person.surname}   {insured_person.age}   {insured_person.phone_number}")
                break
        print(f"\nData has been saved. Press any key to continue...\n")
        input()

    def start(self):
        """
        The method that starts the application and verifies the input entered.
        """
        action = ""
        while action != "4":
            print("--------------------------------\nInsured Evidence\n--------------------------------\n")
            print("Choose an action")
            print("1 - Add a new insured person")
            print("2 - Display all insured persons")
            print("3 - Search for an insured person")
            print("4 - Exit")

            action = input()

            if action == "1":
                self.add_insured()

            elif action == "2":
                self.display_all_insured()

            elif action == "3":
                self.search_insured()

            elif action == "4":
                print("Exiting the program")
            else:
                print("Invalid choice")
