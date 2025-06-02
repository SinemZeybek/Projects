def log_action(func):                   #func dekore ettigimiz fonk. ses degistirme kapatip acma gibi.
    """Decorator to log the TV actions"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  #orijinal fonksiyonu cagiriyoruz, herhangi bir argumani alabilir.
        print(f"[LOG] Action performed: {func.__name__}")   #func yerine gecen fonksiyonun adini yazdirir. 
        return result #orijinal fonksiyonu donduruyoruz.
    return wrapper  #sarmaladigimiz fonksiyonu donduruyoruz.

class TV:
    def __init__(self):
        self.is_on = False
        self.volume = 20
        self.channels = ["ATV", "KANALD", "TV8", "Netflix"]
        self.current_channel_index = 0  #su anda kangi kanalda oldugu: 0.

    @log_action       #sonda power = log_action(power) yazmak yerine @log_action diyoruz.
    def power(self):
        self.is_on = not self.is_on     #toggle; acik ya da kapali olmasi.
        state = "ON" if self.is_on else "OFF"
        print(f"TV is {state} right now.")

    @log_action
    def increase_volume(self):
        if self.is_on:                  #tvnin acik olmasi lazim bunlar icin.
            self.volume += 1
            print(f"Volume: {self.volume}")
        else:
            print("TV is OFF.")

    @log_action
    def decrease_volume(self):
        if self.is_on:
            self.volume = max(0, self.volume - 1)  #0 ile ikinci arasindaki en yuksek sayiyi verecek. 0dan asagi dusemiyor. 
            print(f"Volume: {self.volume}")
        else:
            print("TV is OFF.")

    @log_action
    def next_channel(self):
        if self.is_on:
            self.current_channel_index = (self.current_channel_index + 1) % len(self.channels)
            print(f"Channel: {self.channels[self.current_channel_index]}")
        else:
            print("TV is OFF.")

    @log_action
    def previous_channel(self):
        if self.is_on:
            self.current_channel_index = (self.current_channel_index - 1) % len(self.channels)  #sonuncuya gelince basa 0a gondermis oluyor.
            print(f"Channel: {self.channels[self.current_channel_index]}")
        else:
            print("TV is OFF.")

    @log_action
    def show_status(self):
        if self.is_on:
            print(f"TV is ON | On the channel: {self.channels[self.current_channel_index]} | Volume: {self.volume}")
        else:
            print("TV is OFF.")



def main():
    tv = TV()
    print("Welcome!")
    print("Commands: power, vol+, vol-, next, previous, status, exit")

    while True:
        command = input("Enter command: ").strip().lower()

        if command == "power":
            tv.power()
        elif command == "vol+":
            tv.increase_volume()
        elif command == "vol-":
            tv.decrease_volume()
        elif command == "next":
            tv.next_channel()
        elif command == "previous":
            tv.previous_channel()
        elif command == "status":
            tv.show_status()
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command. Put a valid command.")

if __name__ == "__main__":
    main()
