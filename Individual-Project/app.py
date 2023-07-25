from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase



Config = {
  "apiKey": "AIzaSyCs6k0XhtrNjyECIsubgq0itGfSZhzWn8g",
  "authDomain": "individual-project-7bc5e.firebaseapp.com",
  "projectId": "individual-project-7bc5e",
  "storageBucket": "individual-project-7bc5e.appspot.com",
  "messagingSenderId": "305217233371",
  "appId": "1:305217233371:web:2beb79ec73ea43130687fe",
  "measurementId": "G-30QPYFQRYP",
  "databaseURL": "https://individual-project-7bc5e-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here


@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        try: 
            
            login_session['user'] = auth.sign_in_with_email_and_password(email,password)
            

            
            return redirect(url_for('home'))
        except:
            error = "SIGN IN Authenticitoinsaoinsa / database afaiedkeedlead"
    
    return render_template("sign_in.html", msg_error = error)



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
    #try:
        
        login_session['user'] = auth.create_user_with_email_and_password(email,password)
        UID = login_session['user']['localId']
        user = {"username":request.form['username'],
        "email":request.form['email'],
        }
        db.child("Users").child(UID).set(user)
        add_data()
        return redirect(url_for('home'))
    #except:
        error = "SIGN UP Authenticitoinsaoinsa / database afaiedkeedlead"
    return render_template("signup.html", msg_error = error)


europe_countries_dict = {
    "Spain": {
        "attraction_1": {
            "attraction_name": "Sagrada Família",
            "description": "The Sagrada Família is an iconic basilica in Barcelona, Spain. Designed by Antoni Gaudí, its unique architecture and intricate facades make it a must-visit landmark. Despite being under construction for over a century, it remains an awe-inspiring masterpiece."
        },
        "attraction_2": {
            "attraction_name": "Alhambra",
            "description": "The Alhambra is a stunning palace and fortress complex in Granada, Spain. Known for its Islamic architecture, intricate tilework, and beautiful gardens, it offers visitors a glimpse into Spain's Moorish history and culture."
        }
    },
    "France": {
        "attraction_1": {
            "attraction_name": "Eiffel Tower",
            "description": "The Eiffel Tower is an iconic iron tower in Paris, France. It is one of the most recognizable structures in the world and offers panoramic views of the city from its observation decks."
        },
        "attraction_2": {
            "attraction_name": "Louvre Museum",
            "description": "The Louvre Museum in Paris is the world's largest art museum and a historic monument in France. It houses a vast collection of art and historical artifacts, including Leonardo da Vinci's Mona Lisa."
        }
    },
    "Italy": {
        "attraction_1": {
            "attraction_name": "Colosseum",
            "description": "The Colosseum, located in Rome, Italy, is an ancient amphitheater and one of the most iconic symbols of ancient Roman engineering and architecture. It was used for gladiatorial contests and public spectacles."
        },
        "attraction_2": {
            "attraction_name": "Venice Canals",
            "description": "Venice, Italy, is famous for its intricate network of canals and iconic gondolas. Visitors can explore the charming waterways, historic buildings, and landmarks like St. Mark's Square."
        }
    },
    "United Kingdom": {
        "attraction_1": {
            "attraction_name": "Big Ben and Houses of Parliament",
            "description": "Big Ben is the nickname for the Great Bell of the clock at the north end of the Palace of Westminster in London, England. It is an iconic symbol of London and the United Kingdom."
        },
        "attraction_2": {
            "attraction_name": "Stonehenge",
            "description": "Stonehenge is a prehistoric monument in Wiltshire, England. Its origins and purpose continue to be a subject of debate, but it remains a fascinating and mysterious landmark."
        }
    },
    "Germany": {
        "attraction_1": {
            "attraction_name": "Brandenburg Gate",
            "description": "The Brandenburg Gate is an 18th-century neoclassical monument in Berlin, Germany. It is a symbol of peace and unity and has played a significant role in German history."
        },
        "attraction_2": {
            "attraction_name": "Neuschwanstein Castle",
            "description": "Neuschwanstein Castle is a fairytale-like castle in Bavaria, Germany. Built by King Ludwig II, it is a popular tourist destination known for its picturesque setting and romantic architecture."
        }
    },
    "Greece": {
        "attraction_1": {
            "attraction_name": "Acropolis of Athens",
            "description": "The Acropolis of Athens is an ancient citadel located on a rocky outcrop above the city of Athens, Greece. It contains the remains of several ancient buildings, including the iconic Parthenon."
        },
        "attraction_2": {
            "attraction_name": "Santorini",
            "description": "Santorini is a stunning island in the Aegean Sea known for its white-washed buildings, blue-domed churches, and breathtaking sunsets. It is a popular destination for honeymooners and travelers seeking picturesque views."
        }
    },
    "Netherlands": {
        "attraction_1": {
            "attraction_name": "Keukenhof",
            "description": "Keukenhof is one of the world's largest flower gardens, located in Lisse, Netherlands. It is famous for its stunning displays of tulips and other spring flowers, attracting millions of visitors each year."
        },
        "attraction_2": {
            "attraction_name": "Rijksmuseum",
            "description": "The Rijksmuseum in Amsterdam is the national museum of the Netherlands. It houses an extensive collection of Dutch Golden Age paintings, including works by Rembrandt and Vermeer."
        }
    },
    "Switzerland": {
        "attraction_1": {
            "attraction_name": "The Matterhorn",
            "description": "The Matterhorn is one of the most famous mountains in the Swiss Alps, located on the border between Switzerland and Italy. It is a challenging peak for mountaineers and a popular destination for hikers and skiers."
        },
        "attraction_2": {
            "attraction_name": "Lake Geneva",
            "description": "Lake Geneva is a stunning lake shared by Switzerland and France. The lake is surrounded by picturesque towns and offers a range of outdoor activities, from boating to lakeside strolls."
        }
    },
    "Austria": {
        "attraction_1": {
            "attraction_name": "Schönbrunn Palace",
            "description": "Schönbrunn Palace is a magnificent Baroque palace in Vienna, Austria. It was the former imperial summer residence and is known for its opulent interiors and beautiful gardens."
        },
        "attraction_2": {
            "attraction_name": "Hallstatt",
            "description": "Hallstatt is a charming village in the Salzkammergut region of Austria. It is renowned for its picturesque setting on the Hallstätter See and its well-preserved historic buildings."
        }
    },
    "Sweden": {
        "attraction_1": {
            "attraction_name": "Vasa Museum",
            "description": "The Vasa Museum in Stockholm, Sweden, houses the Vasa ship, which sank in 1628 and was salvaged in 1961. It is the only almost fully intact 17th-century ship in the world and offers a unique insight into maritime history."
        },
        "attraction_2": {
            "attraction_name": "Gamla Stan",
            "description": "Gamla Stan, the old town of Stockholm, is one of the best-preserved medieval city centers in Europe. It offers charming narrow streets, historic buildings, and the Royal Palace."
        }
    },
    "Czech Republic": {
        "attraction_1": {
            "attraction_name": "Prague Castle",
            "description": "Prague Castle is a massive castle complex in Prague, Czech Republic. It is the largest ancient castle in the world and serves as the official residence of the President of the Czech Republic."
        },
        "attraction_2": {
            "attraction_name": "Charles Bridge",
            "description": "The Charles Bridge is a historic bridge in Prague, Czech Republic, connecting the Old Town with the Lesser Town. It is adorned with statues and offers beautiful views of the city and the Vltava River."
        }
    },
    "Norway": {
        "attraction_1": {
            "attraction_name": "Fjords of Norway",
            "description": "Norway's fjords, such as the Geirangerfjord and Nærøyfjord, offer breathtaking natural beauty. These deep, glacially-carved inlets are surrounded by majestic mountains and are a popular destination for cruises and hiking."
        },
        "attraction_2": {
            "attraction_name": "Vigeland Sculpture Park",
            "description": "Vigeland Sculpture Park in Oslo, Norway, is the world's largest sculpture park created by a single artist, Gustav Vigeland. It features a vast collection of sculptures depicting the human experience and is a unique and artistic attraction."
        }
    },
    "Belarus": {
        "attraction_1": {
            "attraction_name": "Mir Castle",
            "description": "Mir Castle is a stunning medieval fortress in Belarus. It is a UNESCO World Heritage Site and showcases a mix of architectural styles, including Gothic, Renaissance, and Baroque."
        },
        "attraction_2": {
            "attraction_name": "Brest Fortress",
            "description": "Brest Fortress is a 19th-century fortress in Belarus, known for its role in the defense against the German invasion during World War II. It now serves as a memorial complex and museum."
        }
    },
    "Iceland": {
        "attraction_1": {
            "attraction_name": "Blue Lagoon",
            "description": "The Blue Lagoon is a geothermal spa in Iceland known for its milky-blue waters and rejuvenating properties. It is located in a lava field on the Reykjanes Peninsula and is a popular destination for relaxation."
        },
        "attraction_2": {
            "attraction_name": "Gullfoss",
            "description": "Gullfoss, meaning 'Golden Falls,' is a powerful waterfall located in southwest Iceland. It is one of the country's most iconic waterfalls and is part of the popular Golden Circle tourist route."
        }
    },
    "Ireland": {
        "attraction_1": {
            "attraction_name": "Cliffs of Moher",
            "description": "The Cliffs of Moher are stunning sea cliffs located on the west coast of Ireland. Rising up to 214 meters, they offer breathtaking views of the Atlantic Ocean and the surrounding coastal landscapes."
        },
        "attraction_2": {
            "attraction_name": "Dublin's Temple Bar",
            "description": "Temple Bar is a lively cultural quarter in Dublin, Ireland. It is known for its vibrant nightlife, cultural events, and artistic atmosphere, making it a popular spot for locals and visitors alike."
        }
    },
    "Liechtenstein": {
        "attraction_1": {
            "attraction_name": "Vaduz Castle",
            "description": "Vaduz Castle is the official residence of the Prince of Liechtenstein. It is located on a hill overlooking the capital, Vaduz. While the castle itself is not open to the public, it is a prominent symbol of the country."
        },
        "attraction_2": {
            "attraction_name": "Malbun",
            "description": "Malbun is a ski resort village in the Alps of Liechtenstein. In addition to winter sports, it offers opportunities for hiking and enjoying the Alpine scenery."
        }
    },
    "Moldova": {
        "attraction_1": {
            "attraction_name": "Old Orhei",
            "description": "Old Orhei is an archaeological and historical complex in Moldova, featuring ancient cave monasteries, fortifications, and traditional villages. It provides a glimpse into the country's rich history and rural heritage."
        },
        "attraction_2": {
            "attraction_name": "Cricova Winery",
            "description": "Cricova Winery is one of the largest underground wine cellars in the world, located in Moldova. It offers guided tours through its vast network of underground tunnels and cellars, showcasing a wide variety of wines."
        }
    },
    "Russia": {
        "attraction_1": {
            "attraction_name": "Red Square and Kremlin",
            "description": "Red Square and the Kremlin are iconic landmarks in Moscow, Russia. The Red Square is a historic square and a UNESCO World Heritage Site, while the Kremlin is a fortified complex that houses several historic buildings, including the residence of the President of Russia."
        },
        "attraction_2": {
            "attraction_name": "Hermitage Museum",
            "description": "The Hermitage Museum in St. Petersburg is one of the largest and oldest museums in the world. It houses an extensive collection of art and cultural artifacts, including works by famous artists such as Leonardo da Vinci, Michelangelo, and Rembrandt."
        }
    },
    "Slovenia": {
        "attraction_1": {
            "attraction_name": "Lake Bled",
            "description": "Lake Bled is a glacial lake in Slovenia, known for its emerald-green waters and a picturesque island with a church in the middle. Visitors can enjoy rowing to the island and exploring the Bled Castle overlooking the lake."
        },
        "attraction_2": {
            "attraction_name": "Postojna Cave",
            "description": "Postojna Cave is a karst cave system in Slovenia, featuring a series of caverns, halls, and passages adorned with stunning stalactites and stalagmites. It is one of the most famous cave systems in the world and offers guided tours for visitors."
        }
    },
    "Croatia": {
        "attraction_1": {
            "attraction_name": "Dubrovnik Old Town",
            "description": "Dubrovnik Old Town is a historic city located on the Adriatic coast of Croatia. It is surrounded by impressive stone walls and offers charming streets, historical buildings, and stunning views of the sea."
        },
        "attraction_2": {
            "attraction_name": "Plitvice Lakes National Park",
            "description": "Plitvice Lakes National Park is a UNESCO World Heritage Site in Croatia, known for its breathtaking lakes and waterfalls. Visitors can explore the park through a network of wooden walkways and hiking trails."
        }
    },
    "Bosnia and Herzegovina": {
        "attraction_1": {
            "attraction_name": "Stari Most",
            "description": "Stari Most, meaning 'Old Bridge,' is a historic Ottoman-style bridge in Mostar, Bosnia and Herzegovina. It spans the Neretva River and is a symbol of the city's unity and resilience after its reconstruction following the war."
        },
        "attraction_2": {
            "attraction_name": "Sarajevo's Bascarsija",
            "description": "Bascarsija is the old bazaar and historical center of Sarajevo, Bosnia and Herzegovina. It offers traditional crafts, Ottoman architecture, and a rich cultural atmosphere."
        }
    },
    "Kosovo": {
        "attraction_1": {
            "attraction_name": "Gračanica Monastery",
            "description": "Gračanica Monastery is a Serbian Orthodox monastery located in Kosovo. It is a UNESCO World Heritage Site and an outstanding example of medieval Serbian architecture and frescoes."
        },
        "attraction_2": {
            "attraction_name": "Rugova Canyon",
            "description": "Rugova Canyon is a scenic canyon in western Kosovo, offering beautiful landscapes and opportunities for outdoor activities such as hiking and rock climbing."
        }
    },
    "Albania": {
        "attraction_1": {
            "attraction_name": "Gjirokastër Old Town",
            "description": "Gjirokastër Old Town is a well-preserved Ottoman-era town in southern Albania. It is known for its historic houses, cobblestone streets, and Gjirokastër Fortress."
        },
        "attraction_2": {
            "attraction_name": "Butrint National Park",
            "description": "Butrint is an ancient city and UNESCO World Heritage Site in Albania. The national park encompasses ancient ruins, a hilltop castle, a freshwater lake, and diverse flora and fauna."
        }
    },
    "North Macedonia": {
        "attraction_1": {
            "attraction_name": "Skopje Old Bazaar",
            "description": "The Skopje Old Bazaar is one of the oldest and largest bazaars in the Balkans, located in the capital city of North Macedonia. It offers a mix of Ottoman and Byzantine architecture, along with bustling markets and historical sites."
        },
        "attraction_2": {
            "attraction_name": "Ohrid Lake",
            "description": "Lake Ohrid, shared by North Macedonia and Albania, is one of Europe's oldest and deepest lakes. The town of Ohrid, located on its shores, is a UNESCO World Heritage Site and offers visitors a wealth of historical and natural attractions."
        }
    },
    "Serbia": {
        "attraction_1": {
            "attraction_name": "Belgrade Fortress",
            "description": "Belgrade Fortress, located at the confluence of the Sava and Danube rivers in Belgrade, Serbia, is a historic fortification that dates back to ancient times. The fortress complex includes museums, galleries, and offers spectacular views of the city."
        },
        "attraction_2": {
            "attraction_name": "St. Sava Temple",
            "description": "St. Sava Temple is one of the largest Orthodox churches in the world, located in Belgrade, Serbia. Its grand architecture and impressive dome make it a significant religious and cultural landmark in the country."
        }
    },
    "Montenegro": {
        "attraction_1": {
            "attraction_name": "Kotor Old Town",
            "description": "Kotor Old Town is a well-preserved medieval town located in the Bay of Kotor, Montenegro. It is surrounded by impressive city walls and offers narrow streets, historic buildings, and beautiful squares."
        },
        "attraction_2": {
            "attraction_name": "Sveti Stefan",
            "description": "Sveti Stefan is a small islet and luxury resort in Montenegro, known for its picturesque architecture and scenic views. The island is connected to the mainland by a causeway and is a popular destination for visitors seeking tranquility and natural beauty."
        }
    },
    "Slovakia": {
        "attraction_1": {
            "attraction_name": "Bratislava Castle",
            "description": "Bratislava Castle is an iconic landmark in the capital city of Slovakia. Perched on a hill overlooking the Danube River, the castle offers panoramic views of the city and surrounding countryside."
        },
        "attraction_2": {
            "attraction_name": "Spiš Castle",
            "description": "Spiš Castle is one of the largest castle complexes in Central Europe, located in eastern Slovakia. It is a UNESCO World Heritage Site and attracts visitors with its historical significance and stunning hilltop location."
        }
    },
    "Svalbard and Jan Mayen": {
        "attraction_1": {
            "attraction_name": "Arctic Wildlife",
            "description": "Svalbard and Jan Mayen, located in the Arctic Ocean, offer unique opportunities to observe polar bears, Arctic foxes, walruses, and various bird species in their natural habitat."
        },
        "attraction_2": {
            "attraction_name": "Glacier Exploration",
            "description": "The archipelago of Svalbard is home to numerous glaciers, providing visitors with the chance to explore these majestic ice formations and witness the beauty of the Arctic landscape."
        }
    },
    "Ukraine": {
        "attraction_1": {
            "attraction_name": "Chernobyl Exclusion Zone",
            "description": "The Chernobyl Exclusion Zone, near the city of Pripyat in Ukraine, is a unique and haunting destination where visitors can explore the abandoned remains of the Chernobyl Nuclear Power Plant and learn about the world's worst nuclear disaster."
        },
        "attraction_2": {
            "attraction_name": "Saint Sophia's Cathedral",
            "description": "Saint Sophia's Cathedral, located in Kyiv, Ukraine, is a UNESCO World Heritage Site and a beautiful example of Byzantine architecture. The cathedral is adorned with mosaics and frescoes dating back to the 11th century."
        }
    },
    "Faroe Islands": {
        "attraction_1": {
            "attraction_name": "Sørvágsvatn",
            "description": "Sørvágsvatn, also known as Leitisvatn, is the largest lake in the Faroe Islands. It is famous for its optical illusion that makes it appear as if the lake sits higher than the ocean, although it is only a few meters above sea level."
        },
        "attraction_2": {
            "attraction_name": "Gásadalur",
            "description": "Gásadalur is a picturesque village in the Faroe Islands known for its stunning waterfall, Múlafossur. The waterfall cascades from a cliff into the ocean, creating a breathtaking sight against the backdrop of rugged landscapes."
        }
    },
    "Andorra": {
        "attraction_1": {
            "attraction_name": "Vallnord",
            "description": "Vallnord is a ski resort located in the Pyrenees mountains of Andorra. During the winter months, it offers excellent skiing and snowboarding opportunities, while in the summer, visitors can enjoy outdoor activities and stunning mountain views."
        },
        "attraction_2": {
            "attraction_name": "Casa de la Vall",
            "description": "Casa de la Vall is a historic house and former parliament building in Andorra la Vella, Andorra. It is one of the oldest buildings in the city and provides insights into the country's political history."
        }
    }
}

def add_data():{
    
db.child("Countries").set(europe_countries_dict)
}


@app.route('/profile')
def profile():
    return render_template("profile.html")



@app.route('/homepage')
def home():
    return render_template("home.html")

#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)