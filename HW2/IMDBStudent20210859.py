import sys

movie_dict = dict()

with open(sys.argv[1], "r") as input_file:
    for line in input_file:
        line = line.strip()

        colon = line.split("::")
        genre = colon[2]
        detail_genre = genre.split("|")
        
        for item in detail_genre:
            if item in movie_dict:
                movie_dict[item] += 1
            else:
                movie_dict[item] = 1

with open(sys.argv[2], "w") as output_file:
    for item in movie_dict:
        output_file.write(f"{item} {movie_dict[item]}\n")