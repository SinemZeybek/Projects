import time 
import random

lives = 3
the_criminal = "Temizlikçi" 

# Mekanlar ve Ipucları
locations = {
        "Kafeterya": {
            "characters": {
                "Güvenlik Görevlisi": "Gece laboratuarın ışığını açık gördüm ama malesef oradaki kameralar dün kayıt yapmamış."
            },
            "clue": "Çöp kutusunun yanında yerde bir adet siyah eldiven var."
        },
        "Laboratuar": {
            "characters": {
                "Temizlikçi": "Sabah galerideki vitrini silerken üzerinde çizikler fark ettim"
            },
            "clue": "Hımm... Bu kapının kilidi zorlanmış."
        },
        "Sanat Galerisi": {
            "characters": {
                "Ziyaretçi": "Ben sanatla ilgileniyorum, vazoların olduğu yere bakmadım bile."
            },
            "clue": "Yerler çok tozlu."
        },
    }


def start():  # Yardımcı fonskiyonlar 
    print("\nDedektif oyunuma hoşgeldin!\n")
    name = input("Dedektif, lütfen adınızı giriniz: ")
    time.sleep(1)
    print(f"Tanıştığımıza memnun oldum Dedektif {name}.")
    print(f"\nBu kadar kısa zamanda gelebilmenize çok sevindim! \nNe yazık ki dün gece müzemizden çok değerli bir parça çalındı ve bunu bulmamız için sizin yardımınıza ihtiyacımız var.\n")
    time.sleep(3)
    return name 


def pick_a_location(visited):
    remaining_locations = [location for location in locations if location not in visited]
    if not remaining_locations: 
        return None
    
    print("Ziyaret edebileceğin mekanlar:")
    for location in remaining_locations:
        print(f"- {location}")
    choice = input ("Hangi mekanı görmek istiyorsun?").strip().title()

    if choice in remaining_locations:
        return choice
    else: 
        print("Lütfen geçerli bir mekan ismi girin.")
        return pick_a_location(visited)
    
def visit_location(location):
    print(f"{location} incelenmeye başlanıyor...")
    time.sleep(2)

    clue = locations[location]["clue"]
    print(f"{clue}")
    time.sleep(1)

    talk = input(f"{location} içinde birini gördün. Konuşmak ister misin? (evet/hayır):").strip().lower()
    if talk == "evet":
        characters = locations[location]["characters"]
        print("\nKonuştuğun kişi:")
        time.sleep(1)
        for name, info in characters.items():
            print(f"{name}: {info}")
            time.sleep(2)
    else:
        print("Kimseyle konuşmadan devam ediyorsun.")
        time.sleep(1)


def make_guess():
    global lives
    guess = input("\nSuçlunun kim olduğunu düşünüyorsun? ").strip()

    if guess.lower() == the_criminal.lower():
        print("\nTebrikler! Olayı çözdün ve suçluyu yakaladın!")
        return True
    else:
        lives -= 1 
        print(f"\nMalesef yanlış tahmin! Kalan can: {lives}\n")
        if lives == 0:
            print("\nMalesef yanlış tahminde bulundun ve suçlu kaçmayı başardı. Belki bir dahaki sefere... Seni arar mıyız bilmiyorum tabii.")
            print(f"Asıl suçlu: {the_criminal}")
            exit()
        return False
    

def menu_after_visits():
    while True:
        print("Şimdi ne yapmak istiyorsun?")
        print("1. Müze Müdürü ile konuş (tahmin yap)")
        print("2. İncelemeye devam et.") 
        choice = input("Seçimin (1/2) :").strip()
        if choice == "1":
            if make_guess():
                exit()
            else:
                return
        elif choice == "2":
            return
        else:
            print("Geçersiz yanıt. Lütfen 1 veya 2 giriniz.")



def guess_the_criminal(): 
    print("\nHerkesle konuştun ve bütün ipuçlarını topladın.")
    time.sleep(1)
    print("Şimdi suçlunun kim olduğunu ve ne çaldığını tahmin etme zamanı!\nUnutma, kazanmak için ikisini de doğru tahmin etmen gerekiyor.")
    time.sleep(2)

    guess_the_criminal = input("Suçlunun kim olduğunu düşünüyorsun?").strip()


    if guess_the_criminal.lower() == the_criminal.lower():
       print("\nTebrikler! Olayı çözdün ve suçluyu yakaladın!")
    else: 
        print("\nMalesef yanlış tahminde bulundun ve suçlu kaçmayı başardı. Belki bir dahaki sefere... Seni arar mıyız bilmiyorum tabii.")
        print(f"Asıl suçlu: {the_criminal}")
              

def game(): #main function
    global lives
    name = start()
    visited = []

    while len(visited) < len(locations):
        selected = pick_a_location(visited)
        if selected:
            visit_location(selected)
            visited.append(selected)
            menu_after_visits()

    guess_the_criminal()



if __name__ == "__main__":
    game()