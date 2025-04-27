from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from database import Base, engine
from sqlalchemy.orm import relationship 


class User(Base):
    __tablename__ = "user" #table name

    uid = Column(Integer, primary_key = True, autoincrement = True, index = True) 
    name = Column(String(100), nullable = False)
    email = Column(String(100), nullable = False, index = True) 
    password = Column(String(100), nullable = False) #hashing needs to be added


class Follow(Base):
    __tablename__ = "follow"  
    
    XID = Column(Integer, ForeignKey("user.uid"), nullable=False, primary_key = True)
    YID = Column(Integer, ForeignKey("user.uid"), nullable=False, primary_key = True)
    
    #check constraint to ensure XID and YID are not the same
    __table_args__ = (
        CheckConstraint('XID <> YID', name='chk_XID_YID_diff'), 
    )


class Languages(Base):
    __tablename__ = 'languages'

    LID = Column(Integer, primary_key=True, autoincrement=True)
    LANGUAGE = Column(String(50), unique=True, nullable=False)

    tvshows = relationship('TVShows', back_populates='language')
    movies = relationship('Movies', back_populates='language')
    books = relationship('Books', back_populates='language')


class Genres(Base):
    __tablename__ = 'genres'

    GID = Column(Integer, primary_key=True, autoincrement=True)
    GENRE = Column(String(50), unique=True, nullable=False)


class Movies(Base):
    __tablename__ = 'movies'

    MID = Column(Integer, primary_key=True, autoincrement=True)
    MOVIE = Column(String(255), unique=True, nullable=False)
    LID = Column(Integer, ForeignKey('languages.LID'), nullable=True)

    language = relationship('Languages', back_populates='movies') #settign up foreign key

class Books(Base):
    __tablename__ = 'books'

    BID = Column(Integer, primary_key=True, autoincrement=True)
    BOOK = Column(String(255), unique=True, nullable=False)
    LID = Column(Integer, ForeignKey('languages.LID'), nullable=True)

    language = relationship('Languages', back_populates='books')


class TVShows(Base):
    __tablename__ = 'tvshows'

    TVID = Column(Integer, primary_key=True, autoincrement=True)
    TVSHOW = Column(String(255), unique=True, nullable=False)
    LID = Column(Integer, ForeignKey('languages.LID'), nullable=True)

    language = relationship('Languages', back_populates='tvshows')


class MoviesGenres(Base):
    __tablename__ = 'movies_genres'

    MID = Column(Integer, ForeignKey('movies.MID'), primary_key=True)
    GID = Column(Integer, ForeignKey('genres.GID'), primary_key=True)


class BooksGenres(Base):
    __tablename__ = 'books_genres'

    BID = Column(Integer, ForeignKey('books.BID'), primary_key=True)
    GID = Column(Integer, ForeignKey('genres.GID'), primary_key=True)


class TVShowsGenres(Base):
    __tablename__ = 'tvshows_genres'

    TVID = Column(Integer, ForeignKey('tvshows.TVID'), primary_key=True)
    GID = Column(Integer, ForeignKey('genres.GID'), primary_key=True)


class UserMovieLangPref(Base):
    __tablename__ = 'user_movie_lang_pref'

    UID = Column(Integer, ForeignKey('user.uid'), primary_key=True)
    LID = Column(Integer, ForeignKey('languages.LID'), primary_key=True)


class UserBookLangPref(Base):
    __tablename__ = 'user_book_lang_pref'

    UID = Column(Integer, ForeignKey('user.uid'), primary_key=True)
    LID = Column(Integer, ForeignKey('languages.LID'), primary_key=True)


class UserTVShowLangPref(Base):
    __tablename__ = 'user_tvshow_lang_pref'

    UID = Column(Integer, ForeignKey('user.uid'), primary_key=True)
    LID = Column(Integer, ForeignKey('languages.LID'), primary_key=True)


class UserMovieGenPref(Base):
    __tablename__ = 'user_movie_gen_pref'

    UID = Column(Integer, ForeignKey('user.uid'), primary_key=True)
    GID = Column(Integer, ForeignKey('genres.GID'), primary_key=True)


class UserBookGenPref(Base):
    __tablename__ = 'user_book_gen_pref'

    UID = Column(Integer, ForeignKey('user.uid'), primary_key=True)
    GID = Column(Integer, ForeignKey('genres.GID'), primary_key=True)


class UserTVShowGenPref(Base):
    __tablename__ = 'user_tvshow_gen_pref'

    UID = Column(Integer, ForeignKey('user.uid'), primary_key=True)
    GID = Column(Integer, ForeignKey('genres.GID'), primary_key=True)


class UserTVShowWatched(Base):
    __tablename__ = 'user_tvshow_watched'

    UID = Column(Integer, ForeignKey('user.uid'), primary_key=True)
    TVID = Column(Integer, ForeignKey('tvshows.TVID'), primary_key=True)


class UserMovieWatched(Base):
    __tablename__ = 'user_movie_watched'

    UID = Column(Integer, ForeignKey('user.uid'), primary_key=True)
    MID = Column(Integer, ForeignKey('movies.MID'), primary_key=True)


class UserBookRead(Base):
    __tablename__ = 'user_book_read'

    UID = Column(Integer, ForeignKey('user.uid'), primary_key=True)
    BID = Column(Integer, ForeignKey('books.BID'), primary_key=True)

Base.metadata.create_all(engine)