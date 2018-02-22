import media
import fresh_tomatoes

"""Creates Objects for the Class Movie"""

# Details of Pari movie
pari = media.Movie("Pari",
                   "Pari is Supernatural horror film starring Anushka",
                   "https://upload.wikimedia.org/wikipedia/en/c/c2/"
                   "Pari_-_Poster.jpg",
                   "https://www.youtube.com/watch?v=iTomHDVLl4E")

# Details of Avatar movie
avatar = media.Movie("Avatar",
                     "Marine on Alien Planet",
                     "https://upload.wikimedia.org/wikipedia/sco/b/b0/"
                     "Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Details of naachiyar movie
naachiyar = media.Movie("Naachiyar",
                        "Naachiyar is action drama film starring GV,Jyothika",
                        "https://upload.wikimedia.org/wikipedia/en/f/fb/"
                        "Naachiyaar_poster.jpg",
                        "https://www.youtube.com/watch?v=DTtnh86GnTY")

# Details of awe movie
awe = media.Movie("Awe",
                  "Awe is a thriller starring Kajal",
                  "https://upload.wikimedia.org/wikipedia/en/8/81/"
                  "Awe_film_poster.jpg",
                  "https://www.youtube.com/watch?v=xOEscQChX7M")

# Details of oru adaar love movie
oru_adaar_love = media.Movie("Oru Adaar Love",
                             "Oru Adaar Love is a Malayalam rom-com starring Priya",
                             "https://upload.wikimedia.org/wikipedia/en/f/f9/"
                             "Oru_Adaar_Love_%282018%29_Poster.jpg",
                             "https://www.youtube.com/watch?v=pC2yUlN2kMU")

# Details of tagaru movie
tagaru = media.Movie("Tagaru",
                     "Tagaru is a Kannada action film starring ShivRajkumar",
                     "https://upload.wikimedia.org/wikipedia/en/6/66/"
                     "Tagaru.jpg",
                     "https://www.youtube.com/watch?v=scekni9K2Mg")

# Adding the list of movies in the array to pass in open_movies_page method
movies = [pari, avatar, naachiyar, awe, oru_adaar_love, tagaru]
fresh_tomatoes.open_movies_page(movies)
