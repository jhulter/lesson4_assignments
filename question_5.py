# Task 1:
print("*********Task 1*********")
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
tracks = ['Track 1', 'Track 2', 'Track 3', 'Track 4']
print("We have plenty of genres of music you can listen to...")
for genre in genres:
    for track in tracks:
        if genre == 'Jazz':
            print(f"You're listening to smooth {genre} {track}")
        elif genre == 'Rock':
            print(f"You're listening to hard {genre} {track}")
        elif genre == 'Hip-hop':
            print(f"You're listening to funky {genre} {track}")
        else:
            print(f"You're listening to calming {genre} {track}")

# Task 2:
print("*********Task 2*********")
i = 0
x = genres[0]

while x != 'Hip-hop' and i < len(genres):
    print(genres[i])
    i += 1
    x = genres[i]


# Task 3:
print("*********Task 3*********")
for index in range(len(genres)):
    for t in range(len(tracks)):
        if genres[index] == 'Classical':
            print("Classical is not great for a light show")
            continue
        else:
            print(f"You're listening to{tracks[t]} of {genres[index]} genre")

