# tv.py file
# class definition
class TV:
   def __init__(self):
      self.is_on = False
      self.channel_no = 1
      self.channels = []

   def turn_off(self):
      self.is_on = False

   def turn_on(self):
      self.is_on = True

   def show_status(self):
      if self.is_on:
         if self.channel_no <= len(self.channels):
            channel_name = self.channels[self.channel_no - 1]
            print(f'TV is on, channel {self.channel_no} ({channel_name})')
         else:
            print(f'TV is on, channel {self.channel_no}')
      else:
         print('TV is off')

   def set_channels(self, channels_list):
      self.channels = channels_list

   def show_channels(self):
      print("Channels list:")
      index = 1
      for channel in self.channels:
         print(f"{index}. {channel}")

   def set_channel(self,new_channel_no):
      if self.is_on:
         self.channel_no = new_channel_no
