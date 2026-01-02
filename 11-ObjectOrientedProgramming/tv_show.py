# tv_show.py file
# main program
from tv import TV

def main():
   # object creation
    my_tv = TV()

   # object usage
    my_tv.show_status()

    my_tv.turn_on()
    my_tv.show_status()

    channels_data = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery","Animal Planet"]
    my_tv.set_channels(channels_data)
    my_tv.show_channels()

    my_tv.turn_off()
    my_tv.show_status()

if __name__ == "__main__":
   main() 