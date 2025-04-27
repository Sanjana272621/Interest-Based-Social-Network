from database import SessionMaker
from models import Languages, Movies

#connection to database
session = SessionMaker() 

english_language = session.query(Languages).filter_by(LANGUAGE = "English").first()

if not english_language:
    english_language = Languages(LANGUAGE = "English")
    session.add(english_language)
    session.commit()


lang = session.query(Languages).filter_by(LANGUAGE = "English").first()

new_movie = Movies(MOVIE = "Inception", LID = lang.LID)
session.add(new_movie)
session.commit()


movie = session.query(Movies).filter_by(LID = lang.LID).first()
print(movie.MOVIE)

session.close()
