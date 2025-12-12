# tv.py file
# class definition
class TV:
   def __init__(self):
      self.is_on = False
   def turn_off(self):
      self.is_on = False
   def turn_on(self):
      self.is_on = True
   def show_status(self):
      if self.is_on == True:
         return 'TV is on'
      if self.is_on == False:
         return 'TV is off'