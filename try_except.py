# 1st example
print("Exception 1")
from sys import exit

def SysEx():
    try:
        exit(11)
    except SystemExit as e:
        print('Exit code is: %s' % e.code)
        raise

print(SysEx())


#2nd example
print("Exception 2")
def File_error():
    try:
       fh = open("test", "w")
       try:
          fh.write("Test file!!")
       finally:
          print ("Closing the file")
          fh.close()
    except IOError:
       print ("Error: File not found or is read-only" )

print(File_error())


#3rd example
print("Exception 3")
def Filter_Name(name):
    try:
        name = name.encode('ascii')
    except UnicodeError as e:
        if name == 'Салауат':
            print('OK, Салауат')
        else:
            raise e
    return name

print(Filter_Name("Салауат"))