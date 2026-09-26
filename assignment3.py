import random
def hangman_game():
    print("Welcome to Hangman Game!")
    name = input("Please enter your name: ")
    print(f"Hello {name},Lets begin the guessing game!")
    print("You need to guess the Malayalam Movie!!")
    print("You can only make 5 mistakes while guessing the movie!")
    movies = ["Manichitrathazhu", "Drishyam", "Premalu", "Aavesham", "Manjummel Boys", "Kumbalangi Nights",
              "Bangalore Days", "Maheshinte Prathikaaram", "Kireedam", "Devasuram", "Sandesham", "Nadodikkattu",
              "Chithram",
              "Spadikam", "Oru Vadakkan Veeragatha", "Thoovanathumbikal", "Kilukkam", "Godfather", "In Harihar Nagar",
              "Ramji Rao Speaking",
              "Yoddha", "Bharatham", "Panchavadi Palam", "Kaalapani", "Pattanapravesam",
              "Namukku Parkkan Munthiri Thoppukal",
              "Thanmathra", "Guru", "Take Off", "Thaniyavartanam", "Vadakkunokkiyantram", "Amaram", "Vatsalyam",
              "Thondimuthalum Driksakshiyum", "Traffic", "Memories", "Kaazhcha", "Kammatti Paadam", "Dasharatham",
              "Punjabi House", "Pavithram", "Thalavattam", "Thenmavin Kombath", "Innale", "Moonnam Pakkam",
              "Njan Gandharvan", "Oru CBI Diary Kurippu"
                                 "Virus", "Aparan", "Aaram Thamburan", "Irupatham Noottandu", "Rajavinte Makan",
              "Yavanika",
              "Classmates", "Ponthan Mada", "Chemmeen", "Ustad Hotel", "22 Female Kottayam", "Angamaly Diaries",
              "Paleri Manikyam: Oru Pathirakolapathakathinte Katha", "Jallikattu", "Sudani from Nigeria",
              "Bhoothakaalam", "Nayattu", "Thallumaala", "C.I.D. Moosa", "Chronic Bachelor", "Meesa Madhavan",
              "Narasimham", "Ravanaprabhu", "Pranchiyettan & the Saint", "Indian Rupee", "Mumbai Police",
              "Drishyam 2", "Jaya Jaya Jaya Jaya Hai", "Bheeshma Parvam", "Malayankunju", "C U Soon", "Malik",
              "Helen", "Kaathal – The Core", "Bramayugam", "Aadujeevitham (The Goat Life)", "Neru", "Garudan",
              "Romancham", "RDX: Robert Dony Xavier", "Kannur Squad", "Neru", "Ayalum Njanum Thammil",
              "Left Right Left", "Annayum Rasoolum", "North 24 Kaatham", "Ohm Shanthi Oshaana", "1983",
              "Premam", "Oru Vadakkan Selfie", "Charlie", "Maheshinte Prathikaaram", "Jacobinte Swargarajyam"]
    word=random.choice(movies).upper()
    chance = 5
    guessed_letters = set()
    while chance > 0:
        display_word = ""
        for i in word:
            if i == " ":
                display_word = display_word + " "
            elif i in guessed_letters:
                display_word = display_word + i
            else:
                display_word = display_word + "_"
        if "_" not in display_word:
            print(f"Congratulations! You have successfully guessed the movie {word}!! You Win!!")
            break
        print('Movie: ', display_word)
        print("Do you want to try guessing the whole movie?")
        whole = input("If Yes type Yes else No: ").upper().strip()
        if whole == "YES":
            whole_movie = input("Guess the whole movie: ").upper().strip()
            if whole_movie == word:
                print(f"Congratulations! You have successfully guessed the movie{word}! You Win!!")
                break
            else:
                print(f"Try Again! {whole_movie} is not the movie!")
        print(f"You have {chance} chance(s) left.")
        if guessed_letters:
            print(f"You have guessed the letter(s): {sorted(guessed_letters)}")
        else:
            print("")
        guess=input("Guess a letter: ").upper().strip()
        if len(guess)!=1:
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You have already guessed the word!")
            continue
        if guess in word:
            print(f"Congratulations! {guess} is in the word.!")
            guessed_letters.add(guess)
        else:
            print(f"Try Again! {guess} is not in the word.!")
            chance -= 1
    else:
        print(f"Better Luck Next Time {name}! {word} is the movie!")
hangman_game()