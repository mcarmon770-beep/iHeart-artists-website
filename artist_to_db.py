from app import app
from app import Artists
from app import db
from models_app import Review
from flask import jsonify
from datetime import datetime

def add_artist_to_db(artist_name, genres, origin, band_members, years_active, awards, top_3_albums,\
    top_3_songs, biography, image_path):
    with app.app_context():
        new_artist = Artists(artist_name=artist_name, genres=genres, biography=biography,\
        origin=origin, band_members=band_members, years_active=years_active, awards=awards\
        ,top_3_albums=top_3_albums, top_3_songs=top_3_songs, image_file_path=image_path)
        db.session.add(new_artist)
        db.session.commit()


'''@app.route("/get_artist_ids", methods=["GET"])
def get_artist_ids():
    # Fetch all artist IDs from the database
    artist_ids = [artist.id for artist in Artists.query.all()]
    return jsonify(artist_ids)


add_artist_to_db("The Beatles", "Rock, pop, beat,psychedelia", "Liverpool, England",\
"John Lennon, Paul McCartney, Ringo Starr and George Harrison", "1960–1970", "A star on the Hollywood Walk of Fame\
 Grammy Lifetime Achievement Award (2014), Board of Trustees Grammy Award (1988), Rock and Roll Hall of Fame (1986), Grammy Award for Album of the Year (1968)",\
"“A Hard Day's Night” (1964), “Help!” ( 1965), “Rubber Soul” (1965)",\
"“I Want to Hold Your Hand”, “Yesterday”, “Hey Jude”", "The Beatles were an English rock band formed in Liverpool in 1960, comprising John Lennon, Paul McCartney,\
 George Harrison and Ringo Starr. They are regarded as the most influential band of all time and were integral to the development of\
 1960s counterculture and the recognition of popular music as an art form.","/media/the beatles logo.png")

add_artist_to_db("Queen", "Rock, pop", "London, England",\
"Freddie Mercury, Brian May, Roger Taylor and John Deacon", "1970-Present", "A star on the Hollywood Walk of Fame,\
 Songwriters Hall of Fame (2003), Grammy Lifetime Achievement Award (2018), Rock and Roll Hall of Fame (2001)",\
"“Queen” (1973), “A Night At The Opera” (1975), “The Works” (1965)",\
"“Bohemian Rhaphsody”, “Killer Queen”, “We Are The Champions”", "Queen is a British band that\
 is considered one of the greatest rock bands in history. It was founded in 1970 in London. Its original members were\
  Freddie Mercury, Brian May, Roger Taylor, and John Deacon. Freddie Mercury was the lead singer and was famous because of his \
  theatrical presentations and great voice.","/media/queen_logo.png")

add_artist_to_db("David Bowie", "Art rock, glam rock, pop, electronic", "London, England",\
"None", "1947-2016", "A star on the Hollywood Walk of Fame, The 100 Greatest Artists of All Time (2004),\
 Grammy Hall of Fame (1998), Grammy Lifetime Achievement Award (2006), Rock and Roll Hall of Fame (1996)",\
"“Hunky Dory. David Bowie.” (1971), “Aladdin Sane. David Bowie.” (1973), “Low. David Bowie.” (1977)",\
"“Heroes”, “Space Oddity”, “Let's Dance”", "David Bowie (born January 8, 1947, London, England—died January 10, 2016,\
 New York, New York, U.S.) British singer, songwriter, and actor who was most prominent in the 1970s and best known for his\
  shifting personae and musical genre hopping.","/media/david_bowie.png")

add_artist_to_db("Jimi Hendrix", "Rock, psychedelia, blues, R&B", "Bay City, Michigan, US",\
"None", "1979–Present", "A star on the Hollywood Walk of Fame, UK Music Hall of Fame,\
 Grammy Lifetime Achievement Award (1992), and more.",\
"“Axis: Bold as Love” (1967), “Voodoo Chile” (1968), “Are You Experienced” (1967)",\
"“Hey Joe”, “Voodoo Child (Slight Return)”, “Little Wing”", "James Marshall ”Jimi” Hendrix\
 (November 27, 1942 – September 18, 1970) was an American musician, guitarist and singer. The most\
  prominent blues rock artists of the 1960s. had a great influence on the “flower children” generation.\
   Hendrix was known for a wild and different performance style, when he used to riot on stage and sometimes even play the\
    guitar with his teeth. Hendrix was a groundbreaking musician, he was known as one of the best electric guitar\
     players of all time and is recognized as a guitarist who reshaped the concept of using the guitar.","/media/jimi_hendrix_logo.png")

add_artist_to_db("Eminem", "Hip hop, Rap", "St. Joseph, Missouri, U.S.",\
"None", "1988–Present", "Rock and Roll Hall of Fame (2022), Grammy Award for Best Rap Album (2015),\
 Academy Award for Best Original Song (2003), Grammy Award for Best Rap/Singing Performance (2015).",\
"“The Marshall Mathers LP” (2000), “Recovery” (2010), “Relapse” (2009)",\
"“Without Me”, “The Real Slim Shady”, “Lose Yourself”", "Marshall Bruce Mathers III (born October 17, 1972),\
 known professionally as Eminem, is an American rapper. He is credited with popularizing hip hop in Middle America and\
 is regarded as one of the greatest rappers of all time.[3] His global success is regarded as having broken racial barriers\
 for the acceptance of white rappers in popular music. While much of his transgressive work during the late 1990s and early\
 2000s made him a controversial figure, he came to be a representation of popular angst of the American underclass and\
 has been cited as an influence by and upon many artists working in various genres..","/media/mnm_logo.png")

add_artist_to_db("Madonna", "Pop, electronica, dance", "Bay City, Michigan, US",\
"None", "1979–Present", "Maddona was nominated to 820 awards throught her music career, and won 430 of them. By that\
, she became the first woman in the music history to win this many awards.",\
"'Ray Of Light' (1998), 'Music' (2000), 'Like A Prayer' (1989)",\
"'Borderline', 'Hung Up', 'Like A Prayer'", "Madonna Louise Ciccone (born August 16, 1958) is\
 an American singer, songwriter, and actress. Known as the 'Queen of Pop', she has been widely\
 recognized for her continual reinvention and versatility in music production, songwriting and\
 visual presentation. Madonna's works, which incorporate social, political and religious\
 themes, have generated both controversy and critical acclaim. A prominent cultural pop icon\
 spanning both the 20th and 21st centuries, she remains one of the most 'well-documented figures\
 of the modern age',[2] with a broad array of scholarly reviews, literature, and art works about\
 her, as well as an academic mini subdiscipline devoted to her called Madonna studies.","/media/maddona_logo.png")


add_artist_to_db("Elton John", "Rock, pop rock, glam rock, soft rock, blues", "Pinner, Middlesex, England",\
"None", "1962–Present", "A star on the Hollywood Walk of Fame, Grammy Living Legend Award (1999),\
 Academy Award for Best Original Song (1995), Tony Award for Best Original Score (2000), Rock and Roll Hall of Fame (1994), and more.",\
"“Madman Across the Water” (1971), “Goodbye Yellow Brick Road” (1973), “Blue Moves” (1976)",\
"“Heroes”, “Space Oddity”, “Let's Dance”", "Sir Elton Hercules John CH CBE (birth name Reginald\
 Kenneth Dwight, born 25 March 1947) is an English singer, songwriter, pianist and composer. He started his music career immediately\
  after leaving school. Elton John was the biggest music star of the 1970s.","/media/elton_john.png")

add_artist_to_db("The Rolling Stones", "Rock, pop, blues", "London, England",\
"Charlie Watts, Ronnie Wood, Mick Jagger and Keith Richards.", "1962–present",\
"Grammy Hall of Fame (2013), Rock and Roll Hall of Fame (1989),\
 Grammy Hall of Fame (1998), Grammy Lifetime Achievement Award (1986), Grammy Award for Rock Album (1994), and more.",\
"“Exile on Main St. (1972)”, “Some Girls (1978)”, “Aftermath (1966)”",\
"“Honky Tonk Women”, “Beast Of Burden”, “Paint It, Black”", "The Rolling Stones are an\
 English rock band formed in London in 1962. Active across seven decades, they are one of the most popular\
  and enduring bands of the rock era. In the early 1960s, the band pioneered the gritty, rhythmically\
   driven sound that came to define hard rock.","/media/the_rs.png")

add_artist_to_db("Michael Jackson", "Pop, soul, rhythm and blues ,funk, rock, disco, dance-pop", "Gary, Indiana, US",\
"None", "1958-2009", "A star on the Hollywood Walk of Fame, 7 British Music Awards,\
 28 MTV Video Music Awards, 19 Billboard Music Awards, 26 American Music Awards, 15 Grammy Awards, and more.",\
"“Thriller · 1982”, “Off The Wall · 1979”, “Bad · 1987”",\
"“Beat It”, “Thriller”, “Billie Jean”", "Michael Jackson was once one of the world’s\
 most popular entertainers. He became a star as a child in the jackson 5, later became so well known as a singer, songwriter,\
 and dancer that he became known as the King of Pop.","/media/mj_logo.png")'''













with app.app_context():
        artist = db.session.query(Artists).get(25)
        if artist:
            db.session.delete(artist)
            db.session.commit()



'''with app.app_context():
    artist_to_update = db.session.query(Artists).get(9)

    if artist_to_update:
        # Update the attributes
        artist_to_update.image_file_path = "/media/mj_logo.png"
        db.session.commit()'''

