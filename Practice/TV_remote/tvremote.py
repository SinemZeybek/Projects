def log_action(func):                   #func dekore ettigimiz fonk. ses degistirme kapatip acma gibi.
    """Decorator to log the TV actions"""    #dekoratorun ne yaptigini aciklayan docstring
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  #orijinal fonksiyonu cagiriyoruz, herhangi bir argumani alabilir.
        print(f"[LOG] Action performed: {func.__name__}")   #func yerine gecen fonksiyonun adini yazdirir. 
        return result #orijinal fonksiyonu donduruyoruz.
    return wrapper  #sarmaladigimiz fonksiyonu donduruyoruz.

def requires_power_on(func):
    """If tv is not on, gives error and func doesn`t work."""
    def wrapper(self, *args, **kwargs):
        if not self.is_on:
            print("TV is OFF.")
            return
        return func(self, *args, **kwargs)
    return wrapper


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
    @requires_power_on               #Altta yaziyoruz ki once acik olup olmadigini kontrol etsin.
    def increase_volume(self):
        self.volume += 1
        print(f"Volume: {self.volume}")

    @log_action
    @requires_power_on
    def decrease_volume(self):
        self.volume = max(0, self.volume - 1)  #0 ile ikinci arasindaki en yuksek sayiyi verecek. 0dan asagi dusemiyor. 
        print(f"Volume: {self.volume}")

    @log_action
    @requires_power_on
    def next_channel(self):
        self.current_channel_index = (self.current_channel_index + 1) % len(self.channels)
        print(f"Channel: {self.channels[self.current_channel_index]}")

    @log_action
    @requires_power_on
    def previous_channel(self):
        self.current_channel_index = (self.current_channel_index - 1) % len(self.channels)  #sonuncuya gelince basa 0a gondermis oluyor.
        print(f"Channel: {self.channels[self.current_channel_index]}")

    @log_action
    @requires_power_on
    def show_status(self):
        print(f"TV is ON | On the channel: {self.channels[self.current_channel_index]} | Volume: {self.volume}")


def main():
    tv = TV()
    print(dir(tv))
    print(hasattr(tv, "decrease_volume"))
    print(tv.volume)
    setattr(tv, "volume", 60)
    print(tv.volume)
    delattr(tv, "volume")
    print(hasattr(tv, "volume"))
    print(dir(tv))
    print("Welcome!")
    print("Commands: power, vol+, vol-, next, previous, status, exit")

    command_map = {
        "power": "power",
        "vol+": "increase_volume",
        "vol-": "decrease_volume",
        "next": "next_channel",
        "previous": "previous_channel",
        "status": "show_status"
    }
    while True:
        command = input("Enter command: ").strip().lower()

        if command == "exit":
            print("Bye!")
            break
        elif command in command_map:
            method_name = command_map[command]         
            method = getattr(tv, method_name, None)    # getattr ile fonksiyonu al (boyle bir method yoksa none doner, hata vermez.)
            if method:
                method()                               # ve çağır
            else:
                print("This function does not exist.")
        else:
            print("Invalid command. Put a valid command.")


if __name__ == "__main__":
    main() 