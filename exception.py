def exceptionsEx():
    try:
        a=int(input('Enter The Value'))
        b=int(input('Enter The Value'))
        c=a/b
        print(c)
    except ZeroDivisionError:
        print('Dude Divison by Zero not permitted')
    finally:
        print('This Code Will Be Executed No Matter What!')

exceptionsEx()