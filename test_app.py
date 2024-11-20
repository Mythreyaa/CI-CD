from app import add, subtract

def test_add():
       if add(5, 9) == 10:
              print("Sum: ",add(5,5))
              print("SUCESS")
       else:
              print(AssertionError())
  
def test_subtract():
       assert subtract(10, 5) == 5
       assert subtract(0, 5) == -5
