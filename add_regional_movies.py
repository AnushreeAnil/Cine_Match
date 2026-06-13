import sqlite3

def add_regional_movies():
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    regional_movies = [

        # ─────────────────────────────────────────
        # HINDI MOVIES (additional)
        # ─────────────────────────────────────────
        ("Sholay", "Action Adventure Drama Hindi", "Ramesh Sippy", "Amitabh Bachchan Dharmendra Hema Malini", "Two criminals are hired by a retired police officer to capture a ruthless bandit", 8.2, 1975),
        ("Mughal-E-Azam", "Drama History Romance Hindi", "K. Asif", "Dilip Kumar Madhubala Prithviraj Kapoor", "A Mughal prince falls in love with a court dancer against his father's wishes", 8.1, 1960),
        ("Dil Dhadakne Do", "Comedy Drama Hindi", "Zoya Akhtar", "Priyanka Chopra Ranveer Singh Anil Kapoor", "A dysfunctional family takes a cruise trip and confronts its secrets", 7.2, 2015),
        ("Tumbbad", "Horror Thriller Hindi", "Rahi Anil Barve", "Sohum Shah", "A man seeks treasure from a cursed ancestor and faces terrifying consequences", 8.2, 2018),
        ("Article 15", "Crime Drama Hindi", "Anubhav Sinha", "Ayushmann Khurrana", "A police officer investigates a case of caste discrimination in rural India", 8.1, 2019),
        ("Masaan", "Drama Romance Hindi", "Neeraj Ghaywan", "Vicky Kaushal Richa Chadha", "Two stories of love and loss set against the backdrop of the ghats of Varanasi", 8.2, 2015),
        ("Neerja", "Biography Drama Thriller Hindi", "Ram Madhvani", "Sonam Kapoor", "The story of Neerja Bhanot who saved passengers during a hijack at the cost of her own life", 7.9, 2016),
        ("Kahaani", "Mystery Thriller Hindi", "Sujoy Ghosh", "Vidya Balan", "A pregnant woman arrives in Kolkata to search for her missing husband", 8.1, 2012),
        ("Paan Singh Tomar", "Biography Crime Drama Hindi", "Tigmanshu Dhulia", "Irrfan Khan", "A national champion athlete becomes a wanted rebel after injustice forces his hand", 8.2, 2012),
        ("Super 30", "Biography Drama Hindi", "Vikas Bahl", "Hrithik Roshan", "Mathematician Anand Kumar coaches 30 underprivileged students for the IIT entrance exam", 7.4, 2019),

        # ─────────────────────────────────────────
        # MALAYALAM MOVIES
        # ─────────────────────────────────────────
        ("Drishyam", "Crime Drama Thriller Malayalam", "Jeethu Joseph", "Mohanlal Meena", "A cable operator protects his family from the law after a tragic incident", 8.3, 2013),
        ("Premam", "Drama Romance Malayalam", "Alphonse Puthren", "Nivin Pauly Madonna Sebastian", "A man goes through three phases of love across different stages of his life", 8.3, 2015),
        ("Bangalore Days", "Drama Romance Comedy Malayalam", "Anjali Menon", "Dulquer Salmaan Nazriya Nazim Nivin Pauly", "Three cousins move to Bangalore and experience love and life", 8.3, 2014),
        ("Kumbalangi Nights", "Drama Malayalam", "Madhu C. Narayanan", "Fahadh Faasil Shane Nigam", "Four brothers in a coastal village struggle with family and relationships", 8.4, 2019),
        ("Lucifer", "Action Drama Malayalam", "Prithviraj Sukumaran", "Mohanlal Vivek Oberoi Manju Warrier", "A mysterious outsider gets involved in the power struggle after a chief ministers death", 7.6, 2019),
        ("Joseph", "Crime Drama Mystery Malayalam", "M. Padmakumar", "Joju George", "A retired police officer investigates the mysterious death of a young woman", 8.3, 2018),
        ("Virus", "Drama Thriller Malayalam", "Aashiq Abu", "Parvathy Thiruvothu Kunchako Boban Revathy", "A medical team races against time to contain a deadly Nipah virus outbreak in Kerala", 8.3, 2019),
        ("Charlie", "Adventure Drama Romance Malayalam", "Martin Prakkat", "Dulquer Salmaan Parvathy Thiruvothu", "A free spirited wanderer leaves an impression on everyone he meets including a young woman chasing his footsteps", 8.0, 2015),
        ("Maheshinte Prathikaaram", "Comedy Drama Malayalam", "Dileesh Pothan", "Fahadh Faasil Anusree", "A photo studio owner vows not to wear his slippers until he takes revenge for his humiliation", 8.4, 2016),
        ("Manjadikuru", "Drama Family Malayalam", "Anjali Menon", "Master Dhruvan Sanusha", "A young boy spends his summer at his grandparents house in Kerala and discovers the magic of childhood", 8.1, 2007),

        # ─────────────────────────────────────────
        # KANNADA MOVIES
        # ─────────────────────────────────────────
        ("KGF Chapter 1", "Action Drama Kannada", "Prashanth Neel", "Yash Srinidhi Shetty", "A young man from Mumbai slums rises to become the most feared person in Kolar Gold Fields", 8.2, 2018),
        ("KGF Chapter 2", "Action Drama Kannada", "Prashanth Neel", "Yash Sanjay Dutt Raveena Tandon", "Rocky faces powerful enemies as he takes full control of the gold mines", 8.3, 2022),
        ("Mungaru Male", "Drama Romance Kannada", "Yogaraj Bhat", "Ganesh Pooja Gandhi", "A young man falls in love with a girl who is already engaged to another man", 7.8, 2006),
        ("Ulidavaru Kandante", "Crime Drama Kannada", "Rakshit Shetty", "Rakshit Shetty Kishore", "The story of a fisherman told from five different perspectives", 8.2, 2014),
        ("Lucia", "Drama Mystery Sci-Fi Kannada", "Pawan Kumar", "Sathish Ninasam Rakshit Shetty", "A theatre usher takes an experimental drug that allows him to live in two realities", 7.9, 2013),
        ("Simple Agi Ondh Love Story", "Comedy Drama Romance Kannada", "Yogaraj Bhat", "Rakshit Shetty Bhavana Rao", "A cheerful young man falls in love with his neighbor", 7.5, 2011),
        ("Godhi Banna Sadharana Mykattu", "Drama Kannada", "Hemanth M Rao", "Anant Nag Rakshit Shetty", "A son searches for his father who has Alzheimers and disappeared from home", 8.6, 2016),
        ("Bell Bottom", "Crime Thriller Kannada", "Jayatheertha", "Rishab Shetty Hariprriya", "A detective unravels a web of crime involving a ruthless gang", 8.1, 2019),
        ("777 Charlie", "Adventure Drama Kannada", "Kiranraj K", "Rakshit Shetty Sangeetha Sringeri", "A lonely and reclusive man forms an unexpected bond with a stray dog named Charlie", 8.8, 2022),
        ("Kantara", "Action Drama Mystery Kannada", "Rishab Shetty", "Rishab Shetty Sapthami Gowda", "A conflict arises in a forest village between a spirit worshipping tribe and a forest officer", 8.5, 2022),

        # ─────────────────────────────────────────
        # TAMIL MOVIES
        # ─────────────────────────────────────────
        ("Vikram", "Action Crime Thriller Tamil", "Lokesh Kanagaraj", "Kamal Haasan Vijay Sethupathi Fahadh Faasil", "A special agent investigates a series of murders committed by masked men", 8.4, 2022),
        ("Master", "Action Thriller Tamil", "Lokesh Kanagaraj", "Vijay Vijay Sethupathi Malavika Mohanan", "An alcoholic professor is sent to a juvenile school where he faces a dangerous gangster", 7.7, 2021),
        ("Enthiran", "Action Romance Sci-Fi Tamil", "S Shankar", "Rajinikanth Aishwarya Rai", "A scientist creates a robot that develops feelings and becomes dangerous", 7.1, 2010),
        ("Mersal", "Action Drama Tamil", "Atlee", "Vijay S J Suryah Kajal Aggarwal", "A magician unravels the truth behind a series of killings linked to his past", 7.5, 2017),
        ("96", "Drama Romance Tamil", "C. Prem Kumar", "Vijay Sethupathi Trisha Krishnan", "Two school sweethearts meet after 22 years and reminisce about their past", 8.5, 2018),
        ("Kaithi", "Action Thriller Tamil", "Lokesh Kanagaraj", "Karthi Narain", "A released prisoner gets caught up in a drug bust operation on the same night he plans to meet his daughter", 8.5, 2019),
        ("Soorarai Pottru", "Biography Drama Tamil", "Sudha Kongara", "Suriya Aparna Balamurali", "Based on the life of Air Deccan founder who fights to bring affordable aviation to ordinary people", 8.7, 2020),
        ("Jai Bhim", "Crime Drama Tamil", "T.J. Gnanavel", "Suriya Lijomol Jose", "A lawyer fights for justice after a tribal man dies in police custody", 8.8, 2021),
        ("Pariyerum Perumal", "Drama Tamil", "Mari Selvaraj", "Kathir Anandhi", "A first generation law student faces caste discrimination in college", 8.5, 2018),
        ("Vinnaithaandi Varuvaayaa", "Drama Music Romance Tamil", "Gautham Vasudev Menon", "Silambarasan Trisha Krishnan", "A young man falls deeply in love with a Christian girl and faces religious differences", 7.9, 2010),

        # ─────────────────────────────────────────
        # TELUGU MOVIES
        # ─────────────────────────────────────────
        ("Baahubali: The Beginning", "Action Adventure Drama Telugu", "S S Rajamouli", "Prabhas Rana Daggubati Tamannaah", "A young man discovers his true identity and fights to reclaim the throne of Mahishmati", 8.1, 2015),
        ("Baahubali: The Conclusion", "Action Adventure Drama Telugu", "S S Rajamouli", "Prabhas Rana Daggubati Anushka Shetty", "Shiva wages a great war to avenge his father and reclaim the kingdom", 8.2, 2017),
        ("RRR", "Action Adventure Drama Telugu", "S S Rajamouli", "Ram Charan Jr NTR Alia Bhatt Ajay Devgn", "Two Indian revolutionaries fight against British colonialism in a fictional tale", 7.9, 2022),
        ("Pushpa: The Rise", "Action Crime Drama Telugu", "Sukumar", "Allu Arjun Rashmika Mandanna Fahadh Faasil", "A laborer rises through the red sandalwood smuggling network in the forests of Andhra Pradesh", 7.6, 2021),
        ("Arjun Reddy", "Drama Romance Telugu", "Sandeep Reddy Vanga", "Vijay Deverakonda Shalini Pandey", "A short tempered doctor spirals into self destruction after his girlfriend is forced to marry someone else", 8.0, 2017),
        ("Magadheera", "Action Adventure Fantasy Telugu", "S S Rajamouli", "Ram Charan Kajal Aggarwal Dev Gill", "A warrior from the past is reincarnated in the present and fights for his love", 7.7, 2009),
        ("Jersey", "Drama Sport Telugu", "Gowtam Tinnanuri", "Nani Shraddha Srinath", "A failed cricketer makes a comeback to fulfil his sons wish for a jersey", 8.6, 2019),
        ("Mahanati", "Biography Drama Telugu", "Nag Ashwin", "Keerthy Suresh Dulquer Salmaan", "The life story of legendary actress Savitri and her rise and fall in South Indian cinema", 8.4, 2018),
        ("Eega", "Action Fantasy Telugu", "S S Rajamouli", "Nani Samantha Sudeep", "A man is reincarnated as a housefly and takes revenge on his murderer", 7.7, 2012),
        ("Pellichoopulu", "Comedy Drama Romance Telugu", "Tharun Bhascker", "Vijay Deverakonda Ritu Varma", "Two young people with different dreams end up on an unexpected journey together", 8.2, 2016),
    ]

    count = 0
    for movie in regional_movies:
        cursor.execute("SELECT id FROM movies WHERE title = ? AND genre = ?", (movie[0], movie[1]))
        existing = cursor.fetchone()
        if not existing:
            cursor.execute("""
                INSERT INTO movies (title, genre, director, cast, description, rating, year)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, movie)
            count += 1

    conn.commit()
    conn.close()
    print(f"Successfully added {count} regional language movies!")
    print("Languages added: Hindi, Malayalam, Kannada, Tamil, Telugu")

if __name__ == "__main__":
    add_regional_movies()
