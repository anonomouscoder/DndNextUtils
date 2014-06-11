class UnitTestException(Exception):
   def __init__(self,string=""):
      self.string = string
   def __str__(self):
      return repr(self.string)
class UnitTest():
   name = ""
   def run(self):
      return
   def passTest(self):
      return
   def failTest(self,string=""):
      raise UnitTestException(string)
#