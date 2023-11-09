input_name = input()     #movies_exp.txt
output_name = input()      #movieoutput.txt

input_file = open(input_name, "rt")
output_file = open(output_name, "wt")

movie_dict = dict()

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

for item in movie_dict:
    output_file.write(f"{item} {str(movie_dict[item])}\n")

input_file.close()
output_file.close()