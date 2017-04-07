import media
import fresh_tomatoes

titles = [
    "Pirate Radio", "The Social Network", "Hidden Figures", "The Martian",
    "Good Will Hunting", "The Lives of Others"
]
storylines = [
    '''A band of rogue DJs that captivated Britain, playing the music that defined a generation and
     standing up to a government that wanted classical music, and nothing else, on the airwaves.''',
    '''Harvard student Mark Zuckerberg creates the social networking site that would become known as
     Facebook, but is later sued by two brothers who claimed he stole their idea, and the co-founder
      who was later squeezed out of the business.''',
    '''The story of a team of African-American women mathematicians who served a vital role in NASA 
    during the early years of the US space program.''',
    '''An astronaut becomes stranded on Mars after his team assume him dead, and must rely on his 
    ingenuity to find a way to signal to Earth that he is alive.''',
    '''Will Hunting, a janitor at M.I.T., has a gift for mathematics, but needs help from a psychologist
     to find direction in his life.''',
    '''In 1984 East Berlin, an agent of the secret police, conducting surveillance on a writer and his 
    lover, finds himself becoming increasingly absorbed by their lives.''',
]

wiki_head = "https://upload.wikimedia.org/wikipedia/en/"
youtube_head = "https://youtu.be/"

wiki_suffixes = [
    "e/e3/The_boat_that_rocked_poster.jpg",
    "7/7a/Social_network_film_poster.jpg",
    '4/4f/The_official_poster_for_the_film_Hidden_Figures%2C_2016.jpg',
    'thumb/c/cd/The_Martian_film_poster.jpg/220px-The_Martian_film_poster.jpg',
    'thumb/b/b8/Good_Will_Hunting_theatrical_poster.jpg/220px-Good_Will_Hunting_theatrical_poster.jpg',
    '9/9f/Leben_der_anderen.jpg'
]
youtube_suffixes = [
    "qX1SSiFWF-s", "lB95KLmpLR4", 'RK8xHq6dfAo', 'ej3ioOneTy8', 'PaZVjZEFkRs',
    'FppW5ml4vdw'
]

imdbs = ["7.4", "7.7", "7.9", "8", "8.3", "8.5"]

posters = [wiki_head + wiki_suffix for wiki_suffix in wiki_suffixes]
trailers = [
    youtube_head + youtube_suffix for youtube_suffix in youtube_suffixes
]
movies = []
for n in range(len(titles)):
    movies.append(
        media.Movie(titles[n], storylines[n], posters[n], trailers[n], imdbs[
            n]))
print media.Movie.__doc__
fresh_tomatoes.open_movies_page(movies)
