# the same as in 1.2, but if yes - stop the app, no-continue, else- print ' do not understad'
# provide numbers from 1 to 100, if yes - stop the app, else- continue

for i in range(1,101):
    print(i)
    text = input('Should we break ').lower()
    if text == 'yes':
        print('The program was stopped')
        break
    elif text == 'no':
        continue

    else:
        print("Don't understand you")
        continue