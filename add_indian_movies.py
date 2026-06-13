import sqlite3

def add_indian_movies():
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    indian_movies = [
        # Bollywood - Shah Rukh Khan
        ("Dilwale Dulhania Le Jayenge", "Romance Drama", "Aditya Chopra", "Shah Rukh Khan Kajol", "A young man follows a girl to Europe to win her love", 8.1, 1995),
        ("Kabhi Khushi Kabhie Gham", "Drama Romance Family", "Karan Johar", "Shah Rukh Khan Kajol Amitabh Bachchan Hrithik Roshan", "A wealthy son searches for his adopted brother who was disowned", 7.4, 2001),
        ("My Name Is Khan", "Drama", "Karan Johar", "Shah Rukh Khan Kajol", "A Muslim man with Aspergers syndrome sets out to meet the US president", 8.0, 2010),
        ("Chennai Express", "Action Comedy Romance", "Rohit Shetty", "Shah Rukh Khan Deepika Padukone", "A man on a train to immerse his grandfather ashes gets caught up in South India", 6.2, 2013),
        ("Raees", "Action Crime Drama", "Rahul Dholakia", "Shah Rukh Khan Mahira Khan", "A bootlegger rises to power in Gujarat in the 1980s", 6.7, 2017),

        # Bollywood - Aamir Khan
        ("Dangal", "Biography Drama Sport", "Nitesh Tiwari", "Aamir Khan Fatima Sana Shaikh", "A former wrestler trains his daughters to become world class wrestlers", 8.4, 2016),
        ("3 Idiots", "Comedy Drama", "Rajkumar Hirani", "Aamir Khan Madhavan Sharman Joshi", "Two friends search for their lost companion and reminisce about their college days", 8.4, 2009),
        ("PK", "Comedy Drama", "Rajkumar Hirani", "Aamir Khan Anushka Sharma", "An alien stranded on Earth questions the concept of religion", 8.1, 2014),
        ("Lagaan", "Drama Sport", "Ashutosh Gowariker", "Aamir Khan Gracy Singh", "Villagers in colonial India challenge British officers to a game of cricket", 8.1, 2001),
        ("Taare Zameen Par", "Drama Family", "Aamir Khan", "Darsheel Safary Aamir Khan", "An eight year old dyslexic child is sent to a boarding school where a new teacher recognises his talents", 8.4, 2007),

        # Bollywood - Salman Khan
        ("Sultan", "Action Drama Sport", "Ali Abbas Zafar", "Salman Khan Anushka Sharma", "A wrestler attempts to reclaim his lost glory", 7.0, 2016),
        ("Bajrangi Bhaijaan", "Adventure Drama", "Kabir Khan", "Salman Khan Kareena Kapoor Harshaali Malhotra", "A man takes a mute Pakistani girl back to her homeland to reunite with her family", 8.0, 2015),
        ("Dabangg", "Action Comedy", "Abhinav Kashyap", "Salman Khan Sonakshi Sinha", "A fearless police officer fights crime in a small town", 6.9, 2010),

        # Bollywood - Other
        ("Zindagi Na Milegi Dobara", "Adventure Comedy Drama", "Zoya Akhtar", "Hrithik Roshan Farhan Akhtar Abhay Deol", "Three friends go on a bachelor trip to Spain and face their fears", 8.1, 2011),
        ("Dil Chahta Hai", "Comedy Drama Romance", "Farhan Akhtar", "Aamir Khan Saif Ali Khan Akshaye Khanna", "Three best friends have very different attitudes toward love and life", 8.1, 2001),
        ("Queen", "Adventure Drama", "Vikas Bahl", "Kangana Ranaut", "A Delhi girl goes on her honeymoon alone after her fiance cancels the wedding", 8.2, 2014),
        ("Andhadhun", "Crime Mystery Thriller", "Sriram Raghavan", "Ayushmann Khurrana Tabu Radhika Apte", "A series of events unfold after a blind pianist becomes witness to a murder", 8.3, 2018),
        ("Gully Boy", "Drama Music", "Zoya Akhtar", "Ranveer Singh Alia Bhatt", "A street rapper from the Dharavi slums rises to fame", 7.9, 2019),
        ("Gangs of Wasseypur", "Action Crime Drama", "Anurag Kashyap", "Manoj Bajpayee Nawazuddin Siddiqui", "A saga of revenge spanning three generations of coal mafia in Jharkhand", 8.2, 2012),
        ("Drishyam", "Crime Drama Thriller", "Nishikant Kamat", "Ajay Devgn Tabu Shriya Saran", "A family man goes to great lengths to protect his family from a police investigation", 8.3, 2015),
        ("Uri: The Surgical Strike", "Action Thriller", "Aditya Dhar", "Vicky Kaushal Paresh Rawal", "Indian army conducts a surgical strike on terrorist camps across the border", 8.2, 2019),
        ("Kabir Singh", "Drama Romance", "Sandeep Reddy Vanga", "Shahid Kapoor Kiara Advani", "A medical student with a short temper falls into self destruction after his girlfriend is forced to marry another", 7.1, 2019),

        # South Indian movies
        ("Baahubali: The Conclusion", "Action Adventure Drama", "S S Rajamouli", "Prabhas Rana Daggubati Anushka Shetty", "When Shiva learns about his heritage he wages war to reclaim the throne of Mahishmati", 8.2, 2017),
        ("KGF Chapter 1", "Action Drama", "Prashanth Neel", "Yash Srinidhi Shetty", "A young man from the slums of Mumbai rises to become the most feared person in the Kolar Gold Fields", 8.2, 2018),
        ("KGF Chapter 2", "Action Drama", "Prashanth Neel", "Yash Sanjay Dutt Raveena Tandon", "Rocky takes control of the gold mines and faces powerful enemies from across the country", 8.3, 2022),
        ("RRR", "Action Adventure Drama", "S S Rajamouli", "Ram Charan Jr NTR Alia Bhatt Ajay Devgn", "A fictional story about two Indian revolutionaries who fight against British rule", 7.9, 2022),
        ("Vikram", "Action Crime Thriller", "Lokesh Kanagaraj", "Kamal Haasan Vijay Sethupathi Fahadh Faasil", "A special agent investigates a series of murders committed by masked men", 8.4, 2022),
        ("Pushpa: The Rise", "Action Crime Drama", "Sukumar", "Allu Arjun Rashmika Mandanna Fahadh Faasil", "A laborer rises through the ranks of a red sandalwood smuggling syndicate", 7.6, 2021),
        ("2.0", "Action Sci-Fi", "S Shankar", "Rajinikanth Akshay Kumar Amy Jackson", "A scientist creates a super robot to fight a powerful enemy who threatens mobile phone users", 6.9, 2018),
        ("Master", "Action Thriller", "Lokesh Kanagaraj", "Vijay Vijay Sethupathi Malavika Mohanan", "An alcoholic professor is sent to a juvenile school where he faces a dangerous gangster", 7.7, 2021),
    ]

    count = 0
    for movie in indian_movies:
        # Check if movie already exists
        cursor.execute("SELECT id FROM movies WHERE title = ?", (movie[0],))
        existing = cursor.fetchone()
        if not existing:
            cursor.execute("""
                INSERT INTO movies (title, genre, director, cast, description, rating, year)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, movie)
            count += 1

    conn.commit()
    conn.close()
    print(f"Added {count} Indian movies to the database!")

if __name__ == "__main__":
    add_indian_movies()
