# tv_show.py file
# main program
from tv import TV

def main():
   # object creation
    my_tv = TV()

   # object usage
    my_tv.show_status()
    my_tv.turn_on()
    my_tv.volume_increase()
    my_tv.volume_increase()

    channels_data = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery","Animal Planet"]
    my_tv.set_channels(channels_data)
    my_tv.set_channel(2)
    my_tv.show_status()
    my_tv.volume_increase()
    my_tv.volume_increase()
    my_tv.volume_increase()

    my_tv.set_channel(5)
    my_tv.show_status()

    my_tv.set_channel(7)
    my_tv.show_status()
    my_tv.volume_decrease()
    my_tv.volume_decrease()

    my_tv.set_channel(8)
    my_tv.show_status()

if __name__ == "__main__":
   main() 