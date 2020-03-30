filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        content = f_obj.read()
except FileNotFoundError:
    msg = 'sorry,the file ' + filename + 'does not exit!'
    print(msg)