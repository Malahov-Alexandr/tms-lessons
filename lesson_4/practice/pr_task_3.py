does_it_move = input('Does it move? (y/n): ')
should_it_move = input('Should it move? (y/n): ')

if does_it_move == 'n' and should_it_move == 'y':
    print('Add oil')
elif does_it_move == 'y' and should_it_move == 'n':
    print('Add some glue')
else:
    print('Leave it')