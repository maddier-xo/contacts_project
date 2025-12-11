# Person class
# Class represents a single contact
class Person:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"{self.name} | {self.phone} | {self.email}"


# ContactsApp class
# ContactsApp class stores all contacts in the dictionary
class ContactsApp:
    def __init__(self):
        self.contacts = {}


 # All the methods to add and remove contacts 
 # add_person returns False if contact already exists 
    def add_person(self, name, phone, email):
        if name in self.contacts:
            return False
        self.contacts[name] = Person(name, phone, email)
        return True

 # remove_person returns False if contact not found  
    def remove_person(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return True
        return False


 # Retrieval methods 
 # get_person returns a single contact or none if not founds
    def get_person(self, name):
        return self.contacts.get(name)


 # get_all  returns a list of all contacts 
    def get_all(self):
        return list(self.contacts.values())

    def find_contacts(self, keyword):
        keyword = keyword.lower()
        return [c for c in self.contacts.values() if keyword in c.name.lower() or keyword in c.email.lower()]

    def sort_by_name(self):
        return sorted(self.contacts.values(), key=lambda c: c.name)





# Main Menu
# main() provides an interactive menu for all the functions 
def main():
    app = ContactsApp()  
    while True:
        print("\nMenu:")
        print("1. Add Contact  2. Remove Contact  3. Exact Search")
        print("4. Partial Search  5. List All  6. List Sorted  0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            if app.add_person(name, phone, email):
                print(f"Added: {name}")
            else:
                print(f"{name} already exists.")

        elif choice == "2":
            name = input("Name to remove: ")
            print("Removed" if app.remove_person(name) else "Not found")

        elif choice == "3":
            name = input("Exact name: ")
            print(app.get_person(name) or "Not found")

        elif choice == "4":
            keyword = input("Keyword: ")
            results = app.find_contacts(keyword)
            print("\n".join(str(c) for c in results) or "No matches")

        elif choice == "5":
            contacts = app.get_all()
            print("\n".join(str(c) for c in contacts) or "No contacts")

        elif choice == "6":
            contacts = app.sort_by_name()
            print("\n".join(str(c) for c in contacts) or "No contacts")

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
