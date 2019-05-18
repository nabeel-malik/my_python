user_input = ''
car_started = False

while True:
    user_input = input('> ').lower()
    if user_input == 'start':
        if car_started == True:
            print('Car is already started!')
        else:
            print('Car started... Ready to go!')
            car_started = True
    elif user_input == 'stop':
        if car_started == False:
            print('Car is already stopped!')
        else:
            print('Car stopped.')
            car_started = False
    elif user_input == 'help':
        print('''
        start - to start the car
        stop - to stop the car
        quit - to exit''')
    elif user_input == 'quit':
        break
    else:
        print("I don't understand that.")







