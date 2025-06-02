import os 


class UnderageError(Exception):            #Özel hata yaratacağımız için exception sınıfı.
    pass


def user_sign_up():

    current_folder = os.path.dirname(os.path.abspath(__file__))
    print(current_folder)
    users_path = os.path.join(current_folder, "logs/users.txt")
    logs_path = os.path.join(current_folder, "logs/logs.txt")

    while True:
        name = input("Your Name: ").capitalize()
        age = input("Your Age: ")

        try:
            age_int = int(age)     #Value error verir

            #Eğer yaş 18'den küçükse özel hata
            if age_int < 18:
                raise UnderageError("Age doesn`t match the requirements. (Under 18)")

            #Yaş uygunsa users.txt dosyasına yaz
            try:
                with open(users_path, "a") as file:
                    file.write(name + ", " + str(age_int) + "\n")
                print("Sign up successful!")
            except IOError:
                print("Error during sign up.")
            
            break 

        except ValueError:
            print("Please put your age in numbers.")
        except UnderageError as error:
            print("Error: ", error)
        
        finally:
            try:
                with open(logs_path, "a") as log:
                    log.write("User: " + name + ", Age: " + str(age_int) + "\n")    #str ve int toplanmiyor.
            except IOError:
                print("Error writing in logs file.")

user_sign_up()
