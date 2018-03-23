Entity type: Movies
Sources :
    imdb.com: imdb.csv, imdb_movies.json
    the-numbers.com/movies: thenumbers.csv, the_numbers_movies.json
Table size:
    imdb: 4,291 tuples
    the-numbers: 31,006 tuples
Schema:
    title:            The movie title
    year:             The movie's release year
    mpaa:             MPAA rating assigned to the movie
    runtime:          Movie runtime in years
    genres:           Listed genres separated by commas
    star_rating:      IMDB star rating given to movie, between 1 to 10
    metascore_rating: Metascore rating given to move between 1 to 100
    description:      Synopsis of the movie provided by production house
    director:         Names of directors of the movie, separated by commas
    stars:            Names of few of the main cast of the movie, separated by commas
    gross:            The combined total amount earned by the movie, including domestic and international sales