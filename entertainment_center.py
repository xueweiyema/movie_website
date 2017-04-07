import media
import fresh_tomatoes

pirate_radio = media.Movie("Pirate Radio", 'A band of rogue DJs that captivated Britain, playing the music that defined a generation and standing up to a government that wanted classical music, and nothing else, on the airwaves.',
                           "https://upload.wikimedia.org/wikipedia/en/e/e3/The_boat_that_rocked_poster.jpg", "https://youtu.be/qX1SSiFWF-s", '7.4')

the_social_network = media.Movie("The Social Network", "Harvard student Mark Zuckerberg creates the social networking site that would become known as Facebook, but is later sued by two brothers who claimed he stole their idea, and the co-founder who was later squeezed out of the business.",
                                 "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg", "https://youtu.be/lB95KLmpLR4", '7.7')

hidden_figures = media.Movie('Hidden Figures', 'The story of a team of African-American women mathematicians who served a vital role in NASA during the early years of the US space program.',
                             'https://upload.wikimedia.org/wikipedia/en/4/4f/The_official_poster_for_the_film_Hidden_Figures%2C_2016.jpg', 'https://www.youtube.com/watch?v=RK8xHq6dfAo', '7.9')

the_martian = media.Movie('The Martian', 'An astronaut becomes stranded on Mars after his team assume him dead, and must rely on his ingenuity to find a way to signal to Earth that he is alive.',
                          'https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/The_Martian_film_poster.jpg/220px-The_Martian_film_poster.jpg', 'https://youtu.be/ej3ioOneTy8', '8')

good_will_hunting = media.Movie('Good Will Hunting', 'Will Hunting, a janitor at M.I.T., has a gift for mathematics, but needs help from a psychologist to find direction in his life.',
                                'https://upload.wikimedia.org/wikipedia/en/thumb/b/b8/Good_Will_Hunting_theatrical_poster.jpg/220px-Good_Will_Hunting_theatrical_poster.jpg', 'https://youtu.be/PaZVjZEFkRs', '8.3')

the_lives_of_others = media.Movie('The Lives of Others', 'In 1984 East Berlin, an agent of the secret police, conducting surveillance on a writer and his lover, finds himself becoming increasingly absorbed by their lives.',
                                  'https://upload.wikimedia.org/wikipedia/en/9/9f/Leben_der_anderen.jpg', 'https://youtu.be/FppW5ml4vdw', '8.5')

movies = [pirate_radio, the_social_network, hidden_figures,
          the_martian, good_will_hunting, the_lives_of_others]


fresh_tomatoes.open_movies_page(movies)
