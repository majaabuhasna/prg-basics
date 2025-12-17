import queue

tickets = queue.Queue()
ticket_number = 1

while True:

    print('1. Print a new ticket')
    print('2. Customer being served')
    menu = input('Select an option: ')

    if menu == '1':
        tickets.put(ticket_number)
        print(f'Ticket number: {ticket_number}')
        print()
        ticket_number += 1


    elif menu == '2':
        if tickets.empty():
            print('No customers are being served right now')
            break

        else:
            ticket_number_right_now = tickets.get()
            print(f'Number {ticket_number_right_now} is being served right now')
            print()
        