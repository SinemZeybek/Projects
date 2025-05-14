import time 
import random


def start():  # Yardımcı fonskiyonlar 
    print("\nDedektif oyunuma hoşgeldin!\n")
    name = input("Dedektif, lütfen adınızı giriniz: ")
    time.sleep(1)
    print(f"Tanıştığımıza memnun oldum Dedektif {name}.")
    print(f"\nBu kadar kısa zamanda gelebilmenize çok sevindim! \nNe yazık ki dün gece müzemizden çok değerli bir parça çalındı ve bunu bulmamız için sizin yardımınıza ihtiyacımız var.\n")
    time.sleep(3)
    return name 

def locations():  # Mekanlar ve Ipucları
    locations = ["Kafeterya", "Laboratuar", "Sanat Galerisi"]
    clue_list = [
        "Hımm... Bu kapının kilidi zorlanmış.",
        "Yerler çok tozlu.",
        "Ahh burnuma çok güçlü, kimyasal bir koku geldi.",
        "Köşede 1 adet kablosuz kulaklık teki bulundu. Kime ait henüz bilinmiyor.",
        "Yerde küçük kırık seramik parçaları var."
        ]
    print("\nMüzeyi yavaş yavaş gezmeye başlıyorsun...\n")
    time.sleep(1)
    for a_location in locations: 
        print(f"Şimdi {a_location} inceleniyor...") 
        time.sleep(3)
        clue = random.choice(clue_list) 
        clue_list.remove(clue)
        print(f"{clue}")
        time.sleep(2)

def talking_to_characters(): 
    characters = {
        "Güvenlik Görevlisi": "Gece laboratuarın ışığı açıktı ama herhangi bir giriş kaydı yok.",
        "Müze Sorumlusu": "Dün geceden hiçbir kamera kaydımız yok. Kameralar çalışmıyordu.",
        "Temizlikçi": "Bir yerlerde bir kulaklık gördüm, sanırım bizim güvenlik görevlisine ait.",
        "Bir Ziyaretçi": "Çocuklar koştururken birine çarptılar ve o kişinin elinden, değişik kimyasal kokulu bir şey düştü."
    }

    print("\nMüzede bulunan birkaç kişiyle konuşuyorsun... \n")
    time.sleep(2)
    for person, info in characters.items():
        print(f"{person} dedi ki: {info}")
        time.sleep(4)
    print()
    return characters


def guess_the_criminal(): 
    print("\nHerkesle konuştun ve bütün ipuçlarını topladın.")
    time.sleep(1)
    print("Şimdi suçlunun kim olduğunu ve ne çaldığını tahmin etme zamanı!\nUnutma, kazanmak için ikisini de doğru tahmin etmen gerekiyor.")
    time.sleep(2)
    
    possible_criminals = ["Güvenlik Görevlisi", "Müze Sorumlusu", "Temizlikçi", "Ziyaretçi"]

    the_criminal = random.choice(possible_criminals)
    the_object = "Vazo"

    guess_the_criminal = input("Suçlunun kim olduğunu düşünüyorsun?")
    guess_the_object = input("Suçlu ne çalmış olabilir?")

    if guess_the_criminal.lower() == the_criminal.lower() and guess_the_object.lower() == the_object.lower():
       print("\nTebrikler! Olayı çözdün ve suçluyu yakaladın!")

    elif guess_the_criminal.lower() == the_criminal.lower() and guess_the_object.lower() != the_object.lower():
       print(f"\nSuçluyu doğru tahmin ettin ama üzerinde {guess_the_object} bulunamadı. Çaldığı nesne: {the_object}. Olsun yiine de iyi denemeydi! Bir dahaki sefer daha dikkatli ol!")
    
    elif guess_the_criminal.lower() != the_criminal.lower() and guess_the_object.lower() == the_object.lower(): 
        print(f"\nÇalınan nesneyi buldun ama yanlış kişiyi tutuklamaya çalıştın! Asıl suçlu: {the_criminal} idi. Olsun yine de iyi denemeydi. Bir dahaki sefer daha dikkatli ol!")

    else: 
        print("\nMalesef yanlış tahminde bulundun ve suçlu kaçmayı başardı. Belki bir dahaki sefere... Seni arar mıyız bilmiyorum tabii.")
        print(f"Asıl suçlu: {the_criminal} ve Çalınan Nesne: {the_object}")
              

def game(): #main function
    name = start()
    locations()
    talking_to_characters()
    guess_the_criminal()

    

if __name__ == "__main__":
    game()