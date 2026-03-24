AssholeDetected = ValueError

while True:
    try:
        age = int(input('what is your age?'))
        10/age
    except AssholeDetected as a:
        raise ValueError (f'{a}:  Age IS a Number!')
        print(f'{a}:  Age IS a Number!')
    else:
        print('thank you!')
        
    finally: # no matter what at the end of it all do something
        print('done!')





    