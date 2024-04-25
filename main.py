import random

basic_genres = ["POP", "JAZZ", "CLASSICAL", "RAP", "HIP HOP", "SKA", "ROCK", "COUNTRY", "FOLK", "RNB"]
not_chosen_one = []
not_chosen_two = []
pop_sub = ["DANCE", "ELECTRONIC", "INDIE", "TEEN"]
classical_sub = ["ANCIENT", "OPERA"]
rock_sub = ["HEAVY METAL", "INDIE", "PSYCHEDELIC", "PUNK", "SOFT"]
country_sub = ["BLUEGRASS"]
pop_not = 0
jazz_not = 0
classical_not = 0
rap_not = 0
hiphop_not = 0
ska_not = 0
rock_not = 0
country_not = 0
folk_not = 0
rnb_not = 0

def choose_songs():
    question_genres = []
    question_songs = []
    for i in range(4):
        genre_options = ["POP", "JAZZ", "CLASSICAL", "RAP", "HIP HOP", "SKA", "ROCK", "COUNTRY", "FOLK", "RNB"]
        genre_choose = random.randint(0, (len(genre_options) - 1))
        question_genres.append(basic_genres[genre_choose])
        genre_options.pop(genre_choose)
    for a in range(len(question_genres)):
        pop_songs = []
        jazz_songs = []
        classical_songs = []
        rock_songs = []
        ska_songs = []
        rap_songs = []
        hiphop_songs = []
        country_songs = []
        folk_songs = []
        rnb_songs = []
        if question_genres[a] == "POP":
            f = open("Pop", "r")
            for w in f:
                pop_songs.append(w)
            r = random.randint(0, len(pop_songs) - 1)
            f.close()
            random_pop = pop_songs[r]
            question_songs.append(random_pop)
        elif question_genres[a] == "JAZZ":
            f = open("Jazz", "r")
            for w in f:
                jazz_songs.append(w)
            r = random.randint(0, len(jazz_songs) - 1)
            f.close()
            random_jazz = jazz_songs[r]
            question_songs.append(random_jazz)
        elif question_genres[a] == "CLASSICAL":
            f = open("Classical", "r")
            for w in f:
                classical_songs.append(w)
            r = random.randint(0, len(classical_songs) - 1)
            f.close()
            random_classical = classical_songs[r]
            question_songs.append(random_classical)
        elif question_genres[a] == "RAP":
            f = open("Rap", "r")
            for w in f:
                rap_songs.append(w)
            r = random.randint(0, len(rap_songs) - 1)
            f.close()
            random_rap = rap_songs[r]
            question_songs.append(random_rap)
        elif question_genres[a] == "HIP HOP":
            f = open("HipHop", "r")
            for w in f:
                hiphop_songs.append(w)
            r = random.randint(0, len(hiphop_songs) - 1)
            f.close()
            random_hiphop = hiphop_songs[r]
            question_songs.append(random_hiphop)
        elif question_genres[a] == "SKA":
            f = open("Ska", "r")
            for w in f:
                ska_songs.append(w)
            r = random.randint(0, len(ska_songs) - 1)
            f.close()
            random_ska = ska_songs[r]
            question_songs.append(random_ska)
        elif question_genres[a] == "ROCK":
            f = open("Rock", "r")
            for w in f:
                rock_songs.append(w)
            r = random.randint(0, len(rock_songs) - 1)
            f.close()
            random_rock = rock_songs[r]
            question_songs.append(random_rock)
        elif question_genres[a] == "COUNTRY":
            f = open("Country", "r")
            for w in f:
                country_songs.append(w)
            r = random.randint(0, len(country_songs) - 1)
            f.close()
            random_country = country_songs[r]
            question_songs.append(random_country)
        elif question_genres[a] == "FOLK":
            f = open("Folk", "r")
            for w in f:
                folk_songs.append(w)
            r = random.randint(0, len(folk_songs) - 1)
            f.close()
            random_folk = folk_songs[r]
            question_songs.append(random_folk)
        elif question_genres[a] == "RNB":
            f = open("RnB", "r")
            for w in f:
                rnb_songs.append(w)
            r = random.randint(0, len(rnb_songs) - 1)
            f.close()
            random_rnb = rnb_songs[r]
            question_songs.append(random_rnb)
    print(question_genres)
    print(question_songs)

choose_songs()
