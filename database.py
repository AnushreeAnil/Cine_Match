import sqlite3
from urllib.parse import quote_plus


def imdb_link(title, imdb_id=""):
    if imdb_id:
        return f"https://www.imdb.com/title/{imdb_id}/"
    return f"https://www.imdb.com/find/?q={quote_plus(title)}"


def movie(title, genre, language, director, cast, rating, year, imdb_id=""):
    description = (
        f"A curated {language} {genre.lower()} film selected for CineMatch's "
        "Indian movie discovery catalogue."
    )
    return {
        "title": title,
        "genre": genre,
        "language": language,
        "director": director,
        "cast": cast,
        "description": description,
        "rating": rating,
        "year": year,
        "imdb_link": imdb_link(title, imdb_id)
    }


# Curated Indian catalogue used to make the app feel like a real discovery
# platform. Each movie entry includes title, genre, language, cast, and review metadata.
CURATED_MOVIES = [
    movie("3 Idiots", "Comedy Drama", "Hindi", "Rajkumar Hirani", "Aamir Khan, R. Madhavan, Sharman Joshi", 8.4, 2009, "tt1187043"),
    movie("Dangal", "Biography Drama Sport", "Hindi", "Nitesh Tiwari", "Aamir Khan, Fatima Sana Shaikh, Sanya Malhotra", 8.3, 2016, "tt5074352"),
    movie("Taare Zameen Par", "Drama Family", "Hindi", "Aamir Khan", "Darsheel Safary, Aamir Khan, Tisca Chopra", 8.3, 2007, "tt0986264"),
    movie("Lagaan", "Drama Sport", "Hindi", "Ashutosh Gowariker", "Aamir Khan, Gracy Singh, Rachel Shelley", 8.1, 2001, "tt0169102"),
    movie("Dilwale Dulhania Le Jayenge", "Romance Drama", "Hindi", "Aditya Chopra", "Shah Rukh Khan, Kajol, Amrish Puri", 8.0, 1995, "tt0112870"),
    movie("Swades", "Drama", "Hindi", "Ashutosh Gowariker", "Shah Rukh Khan, Gayatri Joshi, Kishori Ballal", 8.2, 2004, "tt0367110"),
    movie("Chak De India", "Drama Sport", "Hindi", "Shimit Amin", "Shah Rukh Khan, Vidya Malvade, Sagarika Ghatge", 8.1, 2007, "tt0871510"),
    movie("Queen", "Adventure Comedy Drama", "Hindi", "Vikas Bahl", "Kangana Ranaut, Rajkummar Rao, Lisa Haydon", 8.1, 2013, "tt3322420"),
    movie("Andhadhun", "Crime Mystery Thriller", "Hindi", "Sriram Raghavan", "Ayushmann Khurrana, Tabu, Radhika Apte", 8.2, 2018, "tt8108198"),
    movie("Kahaani", "Mystery Thriller", "Hindi", "Sujoy Ghosh", "Vidya Balan, Parambrata Chatterjee, Nawazuddin Siddiqui", 8.1, 2012, "tt1821480"),
    movie("Gangs of Wasseypur", "Action Crime Drama", "Hindi", "Anurag Kashyap", "Manoj Bajpayee, Nawazuddin Siddiqui, Richa Chadha", 8.2, 2012, "tt1954470"),
    movie("Zindagi Na Milegi Dobara", "Adventure Comedy Drama", "Hindi", "Zoya Akhtar", "Hrithik Roshan, Farhan Akhtar, Abhay Deol", 8.2, 2011, "tt1562872"),
    movie("Bajrangi Bhaijaan", "Adventure Drama Family", "Hindi", "Kabir Khan", "Salman Khan, Harshaali Malhotra, Kareena Kapoor", 8.1, 2015, "tt3863552"),
    movie("Tumbbad", "Horror Thriller", "Hindi", "Rahi Anil Barve", "Sohum Shah, Jyoti Malshe, Anita Date", 8.2, 2018, "tt8239946"),
    movie("Article 15", "Crime Drama Thriller", "Hindi", "Anubhav Sinha", "Ayushmann Khurrana, Nassar, Manoj Pahwa", 8.1, 2019, "tt10324144"),

    movie("Drishyam", "Crime Drama Thriller", "Malayalam", "Jeethu Joseph", "Mohanlal, Meena, Ansiba Hassan", 8.3, 2013, "tt3417422"),
    movie("Premam", "Drama Romance", "Malayalam", "Alphonse Puthren", "Nivin Pauly, Sai Pallavi, Madonna Sebastian", 8.3, 2015, "tt4679210"),
    movie("Bangalore Days", "Comedy Drama Romance", "Malayalam", "Anjali Menon", "Dulquer Salmaan, Nivin Pauly, Nazriya Nazim", 8.3, 2014, "tt3668162"),
    movie("Charlie", "Adventure Drama Romance", "Malayalam", "Martin Prakkat", "Dulquer Salmaan, Parvathy Thiruvothu, Aparna Gopinath", 8.0, 2015, "tt5082014"),
    movie("Kumbalangi Nights", "Drama", "Malayalam", "Madhu C. Narayanan", "Shane Nigam, Fahadh Faasil, Soubin Shahir", 8.5, 2019, "tt8413338"),
    movie("Maheshinte Prathikaaram", "Comedy Drama", "Malayalam", "Dileesh Pothan", "Fahadh Faasil, Anusree, Soubin Shahir", 8.3, 2016, "tt4851630"),
    movie("Lucifer", "Action Drama Thriller", "Malayalam", "Prithviraj Sukumaran", "Mohanlal, Vivek Oberoi, Manju Warrier", 7.5, 2019, "tt6067752"),
    movie("Virus", "Drama Thriller", "Malayalam", "Aashiq Abu", "Kunchacko Boban, Parvathy Thiruvothu, Tovino Thomas", 7.8, 2019, "tt8941440"),
    movie("Joseph", "Crime Drama Mystery", "Malayalam", "M. Padmakumar", "Joju George, Athmiya Rajan, Dileesh Pothan", 8.0, 2018),
    movie("Manichitrathazhu", "Comedy Horror Mystery", "Malayalam", "Fazil", "Mohanlal, Shobana, Suresh Gopi", 8.7, 1993, "tt0214915"),
    movie("Ayyappanum Koshiyum", "Action Drama Thriller", "Malayalam", "Sachy", "Biju Menon, Prithviraj Sukumaran, Ranjith", 8.0, 2020, "tt11322920"),
    movie("Minnal Murali", "Action Adventure Comedy", "Malayalam", "Basil Joseph", "Tovino Thomas, Guru Somasundaram, Aju Varghese", 7.8, 2021, "tt7268738"),
    movie("Home", "Drama Family", "Malayalam", "Rojin Thomas", "Indrans, Sreenath Bhasi, Vijay Babu", 8.1, 2021),
    movie("2018", "Drama Thriller", "Malayalam", "Jude Anthany Joseph", "Tovino Thomas, Kunchacko Boban, Asif Ali", 8.4, 2023),
    movie("The Great Indian Kitchen", "Drama", "Malayalam", "Jeo Baby", "Nimisha Sajayan, Suraj Venjaramoodu, Ajitha V.M.", 8.1, 2021),

    movie("Kantara", "Action Drama Mystery", "Kannada", "Rishab Shetty", "Rishab Shetty, Sapthami Gowda, Kishore", 8.2, 2022, "tt15327088"),
    movie("KGF Chapter 1", "Action Drama", "Kannada", "Prashanth Neel", "Yash, Srinidhi Shetty, Ramachandra Raju", 8.2, 2018, "tt7838252"),
    movie("KGF Chapter 2", "Action Drama Thriller", "Kannada", "Prashanth Neel", "Yash, Sanjay Dutt, Raveena Tandon", 8.3, 2022, "tt10698680"),
    movie("777 Charlie", "Adventure Comedy Drama", "Kannada", "Kiranraj K", "Rakshit Shetty, Charlie, Sangeetha Sringeri", 8.7, 2022, "tt7466810"),
    movie("Ulidavaru Kandanthe", "Crime Drama Mystery", "Kannada", "Rakshit Shetty", "Rakshit Shetty, Kishore, Tara", 8.3, 2014, "tt3394420"),
    movie("Lucia", "Drama Mystery Sci-Fi", "Kannada", "Pawan Kumar", "Sathish Ninasam, Sruthi Hariharan, Achyuth Kumar", 8.2, 2013, "tt2358592"),
    movie("Godhi Banna Sadharana Mykattu", "Drama Thriller", "Kannada", "Hemanth M. Rao", "Anant Nag, Rakshit Shetty, Sruthi Hariharan", 8.6, 2016),
    movie("Mungaru Male", "Drama Romance", "Kannada", "Yogaraj Bhat", "Ganesh, Pooja Gandhi, Anant Nag", 8.1, 2006),
    movie("U Turn", "Mystery Thriller", "Kannada", "Pawan Kumar", "Shraddha Srinath, Dileep Raj, Roger Narayan", 7.4, 2016),
    movie("Garuda Gamana Vrishabha Vahana", "Crime Drama Thriller", "Kannada", "Raj B. Shetty", "Raj B. Shetty, Rishab Shetty, Gopalkrishna Deshpande", 8.3, 2021),
    movie("Kirik Party", "Comedy Drama Romance", "Kannada", "Rishab Shetty", "Rakshit Shetty, Rashmika Mandanna, Samyuktha Hegde", 8.2, 2016),
    movie("Dia", "Drama Romance", "Kannada", "K.S. Ashoka", "Pruthvi Ambaar, Dheekshith Shetty, Kushee Ravi", 8.0, 2020),
    movie("Bell Bottom", "Crime Thriller", "Kannada", "Jayatheertha", "Rishab Shetty, Hariprriya, Yogaraj Bhat", 8.1, 2019),

    movie("Vikram", "Action Crime Thriller", "Tamil", "Lokesh Kanagaraj", "Kamal Haasan, Vijay Sethupathi, Fahadh Faasil", 8.3, 2022, "tt9179430"),
    movie("Jai Bhim", "Crime Drama", "Tamil", "T.J. Gnanavel", "Suriya, Lijomol Jose, Manikandan", 8.7, 2021, "tt15097216"),
    movie("Soorarai Pottru", "Biography Drama", "Tamil", "Sudha Kongara", "Suriya, Aparna Balamurali, Paresh Rawal", 8.7, 2020, "tt10189514"),
    movie("Kaithi", "Action Thriller", "Tamil", "Lokesh Kanagaraj", "Karthi, Narain, Arjun Das", 8.4, 2019, "tt9900782"),
    movie("96", "Drama Romance", "Tamil", "C. Prem Kumar", "Vijay Sethupathi, Trisha Krishnan, Varsha Bollamma", 8.5, 2018, "tt7019842"),
    movie("Pariyerum Perumal", "Drama", "Tamil", "Mari Selvaraj", "Kathir, Anandhi, Yogi Babu", 8.7, 2018),
    movie("Anbe Sivam", "Adventure Comedy Drama", "Tamil", "Sundar C.", "Kamal Haasan, Madhavan, Kiran Rathod", 8.6, 2003, "tt0367495"),
    movie("Super Deluxe", "Comedy Crime Drama", "Tamil", "Thiagarajan Kumararaja", "Vijay Sethupathi, Fahadh Faasil, Samantha Ruth Prabhu", 8.2, 2019, "tt7019942"),
    movie("Asuran", "Action Drama", "Tamil", "Vetrimaaran", "Dhanush, Manju Warrier, Prakash Raj", 8.4, 2019, "tt9477520"),
    movie("Vada Chennai", "Action Crime Drama", "Tamil", "Vetrimaaran", "Dhanush, Ameer Sultan, Andrea Jeremiah", 8.4, 2018, "tt5959980"),
    movie("Master", "Action Thriller", "Tamil", "Lokesh Kanagaraj", "Vijay, Vijay Sethupathi, Malavika Mohanan", 7.7, 2021, "tt10579952"),
    movie("Enthiran", "Action Romance Sci-Fi", "Tamil", "S. Shankar", "Rajinikanth, Aishwarya Rai Bachchan, Danny Denzongpa", 7.1, 2010, "tt1305797"),
    movie("Vinnaithaandi Varuvaayaa", "Drama Music Romance", "Tamil", "Gautham Vasudev Menon", "Silambarasan, Trisha Krishnan, Prabhu", 7.9, 2010),

    movie("RRR", "Action Adventure Drama", "Telugu", "S.S. Rajamouli", "N.T. Rama Rao Jr., Ram Charan, Alia Bhatt", 7.8, 2022, "tt8178634"),
    movie("Baahubali: The Beginning", "Action Adventure Drama", "Telugu", "S.S. Rajamouli", "Prabhas, Rana Daggubati, Tamannaah Bhatia", 8.0, 2015, "tt2631186"),
    movie("Baahubali: The Conclusion", "Action Adventure Drama", "Telugu", "S.S. Rajamouli", "Prabhas, Rana Daggubati, Anushka Shetty", 8.2, 2017, "tt4849438"),
    movie("Pushpa: The Rise", "Action Crime Drama", "Telugu", "Sukumar", "Allu Arjun, Rashmika Mandanna, Fahadh Faasil", 7.6, 2021, "tt9389998"),
    movie("Mahanati", "Biography Drama", "Telugu", "Nag Ashwin", "Keerthy Suresh, Dulquer Salmaan, Samantha Ruth Prabhu", 8.4, 2018, "tt7465992"),
    movie("Jersey", "Drama Sport", "Telugu", "Gowtam Tinnanuri", "Nani, Shraddha Srinath, Sathyaraj", 8.5, 2019, "tt8948790"),
    movie("Arjun Reddy", "Drama Romance", "Telugu", "Sandeep Reddy Vanga", "Vijay Deverakonda, Shalini Pandey, Jia Sharma", 8.0, 2017, "tt7294534"),
    movie("Eega", "Action Comedy Fantasy", "Telugu", "S.S. Rajamouli", "Nani, Samantha Ruth Prabhu, Sudeep", 7.7, 2012, "tt2258337"),
    movie("Magadheera", "Action Drama Fantasy", "Telugu", "S.S. Rajamouli", "Ram Charan, Kajal Aggarwal, Dev Gill", 7.7, 2009, "tt1447500"),
    movie("Sita Ramam", "Drama Romance", "Telugu", "Hanu Raghavapudi", "Dulquer Salmaan, Mrunal Thakur, Rashmika Mandanna", 8.5, 2022),
    movie("Agent Sai Srinivasa Athreya", "Comedy Crime Mystery", "Telugu", "Swaroop Rsj", "Naveen Polishetty, Shruti Sharma, Shredha Rajagopalan", 8.3, 2019),
    movie("C/o Kancharapalem", "Drama Romance", "Telugu", "Venkatesh Maha", "Radha Bessy, Subba Rao Vepada, Praneeta Patnaik", 8.4, 2018),
    movie("Athadu", "Action Thriller", "Telugu", "Trivikram Srinivas", "Mahesh Babu, Trisha Krishnan, Sonu Sood", 8.2, 2005),

    movie("Pather Panchali", "Drama Family", "Bengali", "Satyajit Ray", "Kanu Bannerjee, Karuna Bannerjee, Subir Banerjee", 8.2, 1955, "tt0048473"),
    movie("Aparajito", "Drama", "Bengali", "Satyajit Ray", "Pinaki Sengupta, Smaran Ghosal, Kanu Bannerjee", 8.2, 1956, "tt0048956"),
    movie("Apur Sansar", "Drama", "Bengali", "Satyajit Ray", "Soumitra Chatterjee, Sharmila Tagore, Alok Chakravarty", 8.4, 1959, "tt0052572"),
    movie("Charulata", "Drama Romance", "Bengali", "Satyajit Ray", "Madhabi Mukherjee, Soumitra Chatterjee, Sailen Mukherjee", 8.1, 1964, "tt0057935"),
    movie("Nayak", "Drama", "Bengali", "Satyajit Ray", "Uttam Kumar, Sharmila Tagore, Bireswar Sen", 8.3, 1966),
    movie("Meghe Dhaka Tara", "Drama", "Bengali", "Ritwik Ghatak", "Supriya Choudhury, Anil Chatterjee, Gyanesh Mukherjee", 8.0, 1960),
    movie("Baishe Srabon", "Crime Mystery Thriller", "Bengali", "Srijit Mukherji", "Prosenjit Chatterjee, Parambrata Chatterjee, Raima Sen", 8.1, 2011),
    movie("Autograph", "Drama", "Bengali", "Srijit Mukherji", "Prosenjit Chatterjee, Nandana Sen, Indraneil Sengupta", 7.6, 2010),
    movie("Chotushkone", "Drama Mystery Thriller", "Bengali", "Srijit Mukherji", "Aparna Sen, Chiranjit, Goutam Ghose", 8.1, 2014),
    movie("Cinemawala", "Drama Family", "Bengali", "Kaushik Ganguly", "Paran Banerjee, Parambrata Chatterjee, Arun Guhathakurta", 7.7, 2016),
    movie("Asha Jaoar Majhe", "Drama Romance", "Bengali", "Aditya Vikram Sengupta", "Ritwick Chakraborty, Basabdatta Chatterjee", 7.8, 2014),
    movie("Belashuru", "Drama Family", "Bengali", "Shiboprosad Mukherjee", "Soumitra Chatterjee, Swatilekha Sengupta, Rituparna Sengupta", 7.5, 2022),
    movie("Praktan", "Drama Romance", "Bengali", "Shiboprosad Mukherjee", "Prosenjit Chatterjee, Rituparna Sengupta, Aparajita Adhya", 7.7, 2016),

    movie("Sairat", "Drama Romance", "Marathi", "Nagraj Manjule", "Rinku Rajguru, Akash Thosar, Arbaz Shaikh", 8.3, 2016, "tt5312232"),
    movie("Court", "Drama", "Marathi", "Chaitanya Tamhane", "Vira Sathidar, Vivek Gomber, Geetanjali Kulkarni", 7.6, 2014, "tt3717068"),
    movie("Natsamrat", "Drama Family", "Marathi", "Mahesh Manjrekar", "Nana Patekar, Medha Manjrekar, Vikram Gokhale", 8.8, 2016),
    movie("Harishchandrachi Factory", "Biography Comedy Drama", "Marathi", "Paresh Mokashi", "Nandu Madhav, Vibhawari Deshpande, Atharva Karve", 8.4, 2009),
    movie("Fandry", "Drama Romance", "Marathi", "Nagraj Manjule", "Somnath Awghade, Suraj Pawar, Chhaya Kadam", 8.2, 2013),
    movie("Killa", "Drama Family", "Marathi", "Avinash Arun", "Amruta Subhash, Archit Deodhar, Parshva Dhariwal", 7.8, 2014),
    movie("Elizabeth Ekadashi", "Drama Family", "Marathi", "Paresh Mokashi", "Shrirang Mahajan, Sayali Bhandarkavathekar, Pushkar Lonarkar", 7.6, 2014),
    movie("Ventilator", "Drama Family", "Marathi", "Rajesh Mapuskar", "Ashutosh Gowariker, Jitendra Joshi, Sulabha Arya", 7.8, 2016),
    movie("Katyar Kaljat Ghusali", "Drama Musical", "Marathi", "Subodh Bhave", "Sachin Pilgaonkar, Shankar Mahadevan, Subodh Bhave", 8.7, 2015),
    movie("Anandi Gopal", "Biography Drama", "Marathi", "Sameer Vidwans", "Bhagyashree Milind, Lalit Prabhakar, Geetanjali Kulkarni", 8.7, 2019),
    movie("Mulshi Pattern", "Crime Drama", "Marathi", "Pravin Tarde", "Om Bhutkar, Pravin Tarde, Mohan Joshi", 8.0, 2018),
    movie("Deool", "Drama", "Marathi", "Umesh Vinayak Kulkarni", "Nana Patekar, Dilip Prabhavalkar, Girish Kulkarni", 8.1, 2011),
    movie("Balak Palak", "Comedy Drama Family", "Marathi", "Ravi Jadhav", "Shashwati Pimplikar, Madan Deodhar, Bhagyashree Shankpal", 7.8, 2012),

    movie("Carry On Jatta", "Comedy Romance", "Punjabi", "Smeep Kang", "Gippy Grewal, Mahie Gill, Gurpreet Ghuggi", 8.3, 2012),
    movie("Angrej", "Comedy Drama Romance", "Punjabi", "Simerjit Singh", "Amrinder Gill, Sargun Mehta, Aditi Sharma", 8.5, 2015),
    movie("Punjab 1984", "Drama History", "Punjabi", "Anurag Singh", "Diljit Dosanjh, Kirron Kher, Sonam Bajwa", 8.3, 2014),
    movie("Qismat", "Drama Romance", "Punjabi", "Jagdeep Sidhu", "Ammy Virk, Sargun Mehta, Guggu Gill", 8.1, 2018),
    movie("Sufna", "Drama Romance", "Punjabi", "Jagdeep Sidhu", "Ammy Virk, Tania, Jagjeet Sandhu", 8.0, 2020),
    movie("Chal Mera Putt", "Comedy Drama", "Punjabi", "Janjot Singh", "Amrinder Gill, Simi Chahal, Iftikhar Thakur", 7.6, 2019),
    movie("Lahoriye", "Drama Romance", "Punjabi", "Amberdeep Singh", "Amrinder Gill, Sargun Mehta, Yuvraj Hans", 7.7, 2017),
    movie("Rabb Da Radio", "Drama Family", "Punjabi", "Tarnvir Singh Jagpal", "Tarsem Jassar, Simi Chahal, Mandy Takhar", 7.8, 2017),
    movie("Ardaas", "Drama Family", "Punjabi", "Gippy Grewal", "Gurpreet Ghuggi, Ammy Virk, Rana Ranbir", 8.2, 2016),
    movie("Bambukat", "Comedy Drama", "Punjabi", "Pankaj Batra", "Ammy Virk, Binnu Dhillon, Simi Chahal", 7.8, 2016),
    movie("Nikka Zaildar", "Comedy Drama Romance", "Punjabi", "Simerjit Singh", "Ammy Virk, Sonam Bajwa, Nirmal Rishi", 7.3, 2016),
    movie("Jatt & Juliet", "Comedy Romance", "Punjabi", "Anurag Singh", "Diljit Dosanjh, Neeru Bajwa, Jaswinder Bhalla", 7.5, 2012),
    movie("Sajjan Singh Rangroot", "Action Drama War", "Punjabi", "Pankaj Batra", "Diljit Dosanjh, Yograj Singh, Sunanda Sharma", 7.3, 2018),

    movie("Hellaro", "Drama", "Gujarati", "Abhishek Shah", "Shraddha Dangar, Jayesh More, Tejal Panchasara", 8.6, 2019),
    movie("Chaal Jeevi Laiye", "Adventure Drama Family", "Gujarati", "Vipul Mehta", "Siddharth Randeria, Yash Soni, Aarohi Patel", 8.5, 2019),
    movie("Wrong Side Raju", "Drama Thriller", "Gujarati", "Mikhil Musale", "Pratik Gandhi, Kimberley Louisa McBeath, Asif Basra", 7.8, 2016),
    movie("Bey Yaar", "Comedy Drama Family", "Gujarati", "Abhishek Jain", "Darshan Jariwala, Manoj Joshi, Aarti Patel", 8.5, 2014),
    movie("Kevi Rite Jaish", "Comedy Drama", "Gujarati", "Abhishek Jain", "Divyang Thakkar, Veronica Kalpana Gautam, Tom Alter", 8.1, 2012),
    movie("Love Ni Bhavai", "Comedy Drama Romance", "Gujarati", "Sandeep Patel", "Malhar Thakar, Aarohi Patel, Pratik Gandhi", 8.3, 2017),
    movie("Reva", "Drama", "Gujarati", "Rahul Bhole", "Chetan Dhanani, Monal Gajjar, Yatin Karyekar", 8.4, 2018),
    movie("Dhh", "Drama Family", "Gujarati", "Manish Saini", "Naseeruddin Shah, Kahaan, Karan Patel", 8.3, 2017),
    movie("Ventilator", "Drama Family", "Gujarati", "Umang Vyas", "Jackie Shroff, Pratik Gandhi, Sanjay Goradia", 7.5, 2018),
    movie("Gujjubhai the Great", "Comedy Drama", "Gujarati", "Ishaan Randeria", "Siddharth Randeria, Jimit Trivedi, Swati Shah", 8.0, 2015),
    movie("Naadi Dosh", "Comedy Romance", "Gujarati", "Krishnadev Yagnik", "Yash Soni, Janki Bodiwala, Raunaq Kamdar", 7.8, 2022),
    movie("Nayika Devi", "Action Drama History", "Gujarati", "Nitin G.", "Khushi Shah, Manoj Joshi, Chunky Panday", 7.1, 2022),
    movie("Karsandas Pay & Use", "Comedy Drama Romance", "Gujarati", "Krishnadev Yagnik", "Mayur Chauhan, Deeksha Joshi, Hemang Shah", 7.5, 2017),

    movie("Village Rockstars", "Drama Family", "Assamese", "Rima Das", "Bhanita Das, Basanti Das, Boloram Das", 7.2, 2017, "tt7297966"),
    movie("Bulbul Can Sing", "Drama", "Assamese", "Rima Das", "Arnita Barua, Bonita Thakuriya, Manabendra Das", 6.8, 2018),
    movie("Aamis", "Drama Horror Romance", "Assamese", "Bhaskar Hazarika", "Lima Das, Arghadeep Baruah, Neetali Das", 8.0, 2019),
    movie("Kothanodi", "Drama Fantasy Horror", "Assamese", "Bhaskar Hazarika", "Seema Biswas, Adil Hussain, Zerifa Wahid", 7.7, 2015),
    movie("Local Kung Fu", "Action Comedy", "Assamese", "Kenny Basumatary", "Kenny Basumatary, Sangeeta Nair, Utkal Hazowary", 7.4, 2013),
    movie("Ishu", "Drama Family", "Assamese", "Utpal Borpujari", "Kapil Garo, Tonthoingambi Leishangthem, Bishnu Kharghoria", 7.8, 2017),
    movie("Bornodi Bhotiai", "Drama", "Assamese", "Anupam Kaushik Borah", "Himanshu Gogoi, Kaushik Nath, Dorothi Bhardwaj", 8.0, 2019),
    movie("Calendar", "Drama Family", "Assamese", "Himjyoti Talukdar", "Moloya Goswami, Arun Nath, Gunjan Bhardwaj", 7.6, 2018),
    movie("Ratnakar", "Action Drama", "Assamese", "Jatin Bora", "Jatin Bora, Barsha Rani Bishaya, Nishita Goswami", 7.2, 2019),
    movie("Mission China", "Action Thriller", "Assamese", "Zubeen Garg", "Zubeen Garg, Deeplina Deka, Siddhartha Nipon Goswami", 6.9, 2017),
    movie("Kanchenjunga", "Drama Thriller", "Assamese", "Zubeen Garg", "Zubeen Garg, Pabitra Margherita, Sasanka Samir", 7.1, 2019),
    movie("Antareen", "Drama", "Assamese", "Monjul Baruah", "Urmila Mahanta, Pranjal Saikia, Baharul Islam", 7.4, 2017),
    movie("Xhoixobote Dhemalite", "Drama", "Assamese", "Bidyut Kotoky", "Victor Banerjee, Nakul Vaid, Dipannita Sharma", 7.9, 2017),

    movie("Daman", "Drama", "Odia", "Vishal Mourya", "Babushaan Mohanty, Dipanwit Dashmohapatra, Vaibhav Gohil", 8.8, 2022),
    movie("Sala Budha", "Drama Family", "Odia", "Sabyasachi Mohapatra", "Atal Bihari Panda, Sabyasachi Mohapatra, Puspa Panda", 8.1, 2012),
    movie("Adieu Godard", "Comedy Drama", "Odia", "Amartya Bhattacharyya", "Choudhury Bikash Das, Sudhasri Madhusmita, Dipanwit Dashmohapatra", 7.6, 2021),
    movie("Hello Arsi", "Drama", "Odia", "Sambit Mohanty", "Prakruti Mishra, Partha Sarathi Ray, Priyambada Ray", 8.0, 2018),
    movie("Kalika", "Drama Thriller", "Odia", "Nila Madhab Panda", "Sabyasachi Mishra, Gargi Mohanty, Prakruti Mishra", 7.0, 2020),
    movie("Pratikshya", "Drama Family", "Odia", "Anupam Patnaik", "Dipanwit Dashmohapatra, Barsha Patnaik, Choudhury Bikash Das", 8.1, 2022),
    movie("Phalguna Chaitra", "Drama", "Odia", "Sisira Kumar Sahu", "Parthasarathi Ray, Choudhury Jayaprakash Das, BM Baisali", 7.4, 2023),
    movie("Delivery Boy", "Drama", "Odia", "Ashwin Tripathy", "Babushaan Mohanty, Buddhaditya Mohanty, Sailendra Samantray", 7.2, 2023),
    movie("Malajanha", "Drama Romance", "Odia", "Nilamani Sahu", "Akshaya Mohanty, Prashant Nanda, Sujata Anand", 7.5, 1965),
    movie("Maya Miriga", "Drama Family", "Odia", "Nirad N. Mohapatra", "Manimala, Bansidhar Satpathy, Samuel Sahu", 7.9, 1984),
    movie("Pahada Ra Luha", "Drama", "Odia", "Sabyasachi Mohapatra", "Atal Bihari Panda, Lochani Bag, Sabyasachi Mohapatra", 8.0, 2015),
    movie("Kathantara", "Drama", "Odia", "Himanshu Khatua", "Anu Choudhury, Anubhav Mohanty, Sritam Das", 7.2, 2005),
    movie("Tulasi Apa", "Biography Drama", "Odia", "Amiya Patnaik", "Madhusmita Mohanty, Lochani Bag, Mamata Panda", 8.1, 2017),

    movie("Pingara", "Drama", "Tulu", "Preetham Shetty", "Neema Ray, Usha Bhandary, Sharath Shetty", 8.5, 2019),
    movie("Suddha", "Drama Family", "Tulu", "Ramchandra P.N.", "Mohan Sheni, Vaman Nandavara, Balakrishna Shetty", 8.1, 2005),
    movie("September 8", "Drama Thriller", "Tulu", "Ranjith Bajpe", "Ranjan Shetty, Shruthi, Naveen D. Padil", 7.8, 2016),
    movie("Oriyardori Asal", "Comedy Drama", "Tulu", "H.S. Rajashekar", "Naveen D. Padil, Aravind Bolar, Bhojaraj Vamanjoor", 7.6, 2011),
    movie("Chaali Polilu", "Comedy Drama", "Tulu", "Virendra Shetty", "Naveen D. Padil, Aravind Bolar, Bhojaraj Vamanjoor", 8.0, 2014),
    movie("Rang", "Comedy Drama", "Tulu", "Suhail Shetty", "Arjun Kapikad, Deekshitha Achrappa, Naveen D. Padil", 7.8, 2014),
    movie("Eregla Panodchi", "Comedy Drama", "Tulu", "Kodlu Ramakrishna", "Naveen D. Padil, Aravind Bolar, Bhojaraj Vamanjoor", 7.2, 2015),
    movie("Madime", "Comedy Romance", "Tulu", "Vijaykumar Kodialbail", "Arjun Kapikad, Akshatha Shetty, Naveen D. Padil", 7.4, 2014),
    movie("Dabak Daba Aisa", "Comedy Family", "Tulu", "Prakash Pandeshwar", "Devdas Kapikad, Aravind Bolar, Naveen D. Padil", 7.3, 2016),
    movie("Pilibail Yamunakka", "Comedy Drama", "Tulu", "Sooraj Shetty", "Pruthvi Ambar, Sonal Monteiro, Naveen D. Padil", 7.6, 2016),
    movie("Ammer Polisa", "Comedy Drama", "Tulu", "K. Sooraj Shetty", "Roopesh Shetty, Pooja Shetty, Aravind Bolar", 7.4, 2018),
    movie("Girgit", "Comedy Thriller", "Tulu", "Roopesh Shetty", "Roopesh Shetty, Shilpa Shetty, Naveen D. Padil", 7.5, 2019),
    movie("Raj Sounds and Lights", "Comedy Drama", "Tulu", "Rahul Amin", "Vineeth Kumar, Yashaswini Devadiga, Naveen D. Padil", 8.0, 2022),
]


def ensure_column(cursor, table, column, definition):
    cursor.execute(f"PRAGMA table_info({table})")
    columns = [row[1] for row in cursor.fetchall()]
    if column not in columns:
        cursor.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")


def infer_language(genre):
    for language in [
        "Hindi", "Malayalam", "Kannada", "Tamil", "Telugu", "Bengali",
        "Marathi", "Punjabi", "Gujarati", "Assamese", "Odia", "Tulu"
    ]:
        if language.lower() in (genre or "").lower():
            return language
    return "International"


def create_database():
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre TEXT NOT NULL,
            director TEXT,
            "cast" TEXT,
            description TEXT,
            rating REAL,
            year INTEGER
        )
    """)

    ensure_column(cursor, "movies", "language", "TEXT DEFAULT ''")
    ensure_column(cursor, "movies", "imdb_link", "TEXT DEFAULT ''")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS favorites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            movie_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (movie_id) REFERENCES movies(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS watchlist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            movie_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (movie_id) REFERENCES movies(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_preferences (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            personality_type TEXT,
            favorite_genre TEXT,
            favorite_language TEXT,
            updated_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_ratings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            movie_id INTEGER NOT NULL,
            rating REAL NOT NULL,
            FOREIGN KEY (movie_id) REFERENCES movies(id)
        )
    """)

    cursor.execute("SELECT id, title, genre FROM movies")
    for movie_id, title, genre in cursor.fetchall():
        cursor.execute("""
            UPDATE movies
            SET language = COALESCE(NULLIF(language, ''), ?),
                imdb_link = COALESCE(NULLIF(imdb_link, ''), ?)
            WHERE id = ?
        """, (
            infer_language(genre),
            imdb_link(title),
            movie_id
        ))

    inserted = 0
    for item in CURATED_MOVIES:
        cursor.execute("""
            SELECT id FROM movies
            WHERE title = ? AND language = ?
        """, (item["title"], item["language"]))
        existing = cursor.fetchone()

        if existing:
            cursor.execute("""
                UPDATE movies
                SET genre = ?, director = ?, "cast" = ?, description = ?,
                    rating = ?, year = ?, imdb_link = ?
                WHERE id = ?
            """, (
                item["genre"],
                item["director"],
                item["cast"],
                item["description"],
                item["rating"],
                item["year"],
                item["imdb_link"],
                existing[0]
            ))
        else:
            cursor.execute("""
                INSERT INTO movies (
                    title, genre, language, director, "cast",
                    description, rating, year, imdb_link
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                item["title"],
                item["genre"],
                item["language"],
                item["director"],
                item["cast"],
                item["description"],
                item["rating"],
                item["year"],
                item["imdb_link"]
            ))
            inserted += 1

    conn.commit()
    conn.close()
    print(f"Database ready. Curated movies inserted: {inserted}")


if __name__ == "__main__":
    create_database()
