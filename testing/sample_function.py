#assume this is one of the functions that builds your app
def do_stuff(num):
    try:
        return int(num) * 5
    except (ValueError, TypeError) as err:
        return err
