# provide numbers from 1 to 100, if yes - stop the app, else- continue

for i in range(1,101):
    print(i)
    if input('Should we break ').lower() == 'yes':
        print('The program was stopped')
        break
    else:
        continue

