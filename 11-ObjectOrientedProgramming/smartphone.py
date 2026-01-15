from contact import Contact
from contact_list import ContactList

def main():
    my_contacts = ContactList()

    p1 = Contact("John Brown","brown@onet.pl","555234000")
    p2 = Contact("Anna May","am@o2.pl","232000199")
    p3 = Contact("George Small","smallg@google.pl","222999100")
    p4 = Contact("Paola Big","bigpaola@poczta.pl","100200300")

    my_contacts.add_contact(p1)
    my_contacts.add_contact(p2)
    my_contacts.add_contact(p3)
    my_contacts.add_contact(p4)

    my_contacts.display_contacts()

if __name__ == '__main__':
    main()