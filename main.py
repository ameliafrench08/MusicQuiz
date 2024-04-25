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
    question_genres = ["POP"]
    question_songs = []
    for i in range(4):
        genre_choose = random.randint(0, (len(basic_genres) - 1))
        question_genres.append(basic_genres[genre_choose])
    for a in range(len(question_genres)):
        pop_songs = []
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
        elif question_genres[a] == "CLASSICAL":
            f = open("Classical", "r")
        elif question_genres[a] == "RAP":
            f = open("Rap", "r")
        elif question_genres[a] == "HIP HOP":
            f = open("HipHop", "r")
        elif question_genres[a] == "SKA":
            f = open("Ska", "r")
        elif question_genres[a] == "ROCK":
            f = open("Rock", "r")
        elif question_genres[a] == "COUNTRY":
            f = open("Country", "r")
        elif question_genres[a] == "FOLK":
            f = open("Folk", "r")
        elif question_genres[a] == "RNB":
            f = open("RnB", "r")
