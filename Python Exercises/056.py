from distutils.log import error


def throws():
    return 5 / 0

try:
    throws()
except ZeroDivisionError:
    print("Divison by zero!")
except Exception:
    print("Caught an exception")
finally:
    print("In finally block for cleanup")