player_to_id_map = {
"ATL": {'Larry Nance Jr.': 385, 'Caris LeVert': 317, 'Georges Niang': 391, 'Trae Young': 1046, 'Terance Mann': 1877, "DeAndre Hunter": 1868,
         'Garrison Mathews': 2327, 'Onyeka Okongwu': 2629, 'Vit Krejci': 2608, 'Kevon Harris': 2677, 'Jalen Johnson': 2819,
         'Dyson Daniels': 3406, 'David Roddy': 3483, 'Dominick Barlow': 3415, 'Daeqwon Plowden': 3478, 'Kobe Bufkin': 3938,
         'Mouhamed Gueye': 3939, 'Seth Lundy': 3941, 'Zaccharie Risacher': 4090, 'Clint Capela': 92, 'Bogdan Bogdanovic': 743, 'Keaton Wallace': 3259},

"BOS": {'Jaylen Brown': 75, 'Jayson Tatum': 882, 'Derrick White': 897, 'Luke Kornet': 819, 'Torrey Craig': 765, 'Lonnie Walker IV': 1038,
           'Neemias Queta': 2844, 'Payton Pritchard': 2635, 'Xavier Tillman': 2656, 'Jaden Springer': 2851, 'Sam Hauser': 2812, 'JD Davison': 3429,
           'Ron Harper Jr.': 3447, 'Jordan Walsh': 3943, 'Drew Peterson': 3995, 'D. Skapintsev': 4083, 'Baylor Scheierman': 4092, 'Anton Watson': 4093,
           'Al Horford': 248, 'Jrue Holiday': 242, 'Kristaps Porzingis': 432},

"BKN": {"D'Angelo Russell": 462, 'Ben Simmons': 481, 'Dorian Finney-Smith': 175, 'Dennis Smith Jr.': 876, 'Shake Milton': 1001, 'Nic Claxton': 1854,
        'Cameron Johnson': 1871, 'Ziaire Williams': 2864, "Day'Ron Sharpe": 2848, 'Keon Johnson': 2820, 'Cam Thomas': 2855, 'Trendon Watford': 2861,
        'Tyrese Martin': 3465, 'Noah Clowney': 3944, 'Dariq Whitehead': 3945, 'Jalen Wilson': 3946, 'Amari Bailey': 3947, 'Tosan Evbuomwan': 3969,
        'Maxwell Lewis': 3991, 'Jaylen Martin': 4006, 'Reece Beekman': 4114, 'Yongxi Cui': 4212, 'Dennis Schroder': 472},

"CHA": {'Miles Bridges': 941, 'Cody Martin': 1879, 'Josh Okogie': 1010, 'DaQuan Jeffries': 1948, 'Grant Williams': 1901, 'Charlie Brown Jr.': 2111,
           'LaMelo Ball': 2566, 'Josh Green': 2593, 'Nick Richards': 2639, 'Tre Mann': 2831, 'Duane Washington Jr.': 2860, 'Mark Williams': 3506,
           'Jared Rhoden': 3481, 'Moussa Diabate': 3431, 'Brandon Miller': 3950, 'Isaiah Wong': 3982, 'Damion Baugh': 3986, 'Keyontae Johnson': 4008,
           'Harry III Giles': 4041, 'Nick Jr. Smith': 4042, 'Tidjane Salaun': 4095, 'K.J. Simpson': 4096, 'Taj Gibson': 190, 'Seth Curry': 123,
           'Elfrid Payton': 418, 'Jusuf Nurkic': 398, 'Vasilije Micic': 2739},

"CHI": {'Lonzo Ball': 735, 'Zach Collins': 762, 'Torrey Craig': 765, 'Jevon Carter': 949, 'Kevin Huerter': 980, 'Coby White': 1900, 
         'Talen Horton-Tucker': 1867, 'Patrick Williams': 2664, 'Jalen Smith': 2644, 'Tre Jones': 2606, 'Ayo Dosunmu': 2802, 'Chris Duarte': 2803, 
         'DJ Steward': 2921, 'Josh Giddey': 2808, 'E.J. Liddell': 3462, 'Dalen Terry': 3494, 'Kenneth Lofton Jr.': 3463, 'Onuralp Bitim': 3951, 
         'Julian Phillips': 3954, 'Adama Sanogo': 3955, 'Matas Buzelis': 4098, 'Nikola Vucevic': 534, 'Zach LaVine': 308},

"CLE": {'Caris LeVert': 317, 'Georges Niang': 391, 'Donovan Mitchell': 840, 'Jarrett Allen': 727, 'Zhaire Smith': 1025, 'Max Strus': 2051, 
        "DeAndre Hunter": 1868, 'Darius Garland': 1860, 'Ty Jerome': 1870, 'Dean Wade': 2392, 'Isaac Okoro': 2630, 'Sam Merrill': 2623, 
        'JT Thor': 2856, 'Evan Mobley': 2835, 'Jules Bernard': 3576, 'Jacob Gilyard': 3892, 'Emoni Bates': 3956, 'Pete Nance': 3957, 
        'Craig Jr. Porter': 4043, 'Luke Travers': 4101, 'Jaylon Tyson': 4102, 'Tristan Thompson': 515},

"DAL": {'Maxi Kleber': 817, 'P.J. Washington': 1897, 'Luka Doncic': 963, 'Daniel Gafford': 1859, 'Quentin Grimes': 2811, 'Naji Marshall': 2668, 
        'Kylor Kelley': 2670, 'Brandon Williams': 3398, 'Kessler Edwards': 2805, 'A.J. Lawson': 2890, 'Jaden Hardy': 3407, 'Max Christie': 3427, 
        'OlivierMaxence Prosper': 3960, 'Jazian Gortman': 3996, 'Dereck II Lively': 4044, 'Emanuel Miller': 4103, 'Jamarion Sharp': 4104, 
        'Kyrie Irving': 261, 'Klay Thompson': 514, 'Markieff Morris': 374, 'Anthony Davis': 126, 'Spencer Dinwiddie': 142, 'Dwight Powell': 433, 
        'Dante Exum': 164},

"DEN": {'Jamal Murray': 383, 'Vlatko Cancar': 1312, 'Michael Porter Jr.': 1014, 'Zeke Nnaji': 2627, 'Christian Braun': 3420, 'Peyton Watson': 3498, 
           'Andrew Funk': 3964, 'Jalen Pickett': 3965, 'Julian Strawther': 3966, 'Hunter Tyson': 3967, 'Charles Bediako': 4023, 'Trey Alexander': 4105, 
           'PJ Hall': 4106, 'Spencer Jones': 4108, 'Gabe McGlothan': 4109, 'Jahmir Young': 4110, 'W. Richardson': 4205, 'Russell Westbrook': 544, 
           'DeAndre Jordan': 286, 'Aaron Gordon': 195, 'Dario Saric': 468, 'Nikola Jokic': 279},

"DET": {'Malik Beasley': 46, 'Isaiah Stewart': 2648, 'Jalen Duren': 3433, 'Simone Fontecchio': 3438, 'Cade Cunningham': 2801, 'Marcus Sasser': 3970, 
           'Ausar Thompson': 3971, 'Ron II Holland': 4111, 'Tobias Harris': 222, 'Dennis Schröder': 472, 'Tim Hardaway Jr.': 215},

"GSW": {'Kevon Looney': 322, 'Buddy Hield': 236, 'Gary Payton II': 593, 'Kevin Knox II': 987, "DeAnthony Melton": 998, 'Jonathan Kuminga': 2827, 
            'Pat Spencer': 3492, 'Lindy Waters III': 3404, 'Moses Moody': 2836, 'Gui Santos': 3485, 'Trayce JacksonDavis': 3973, 
            'Brandin Podziemski': 3975, 'Reece Beekman': 4114, 'Jackson Rowe': 4115, 'Q. Post': 4207, 'B. Hinson': 4209, 'Stephen Curry': 124, 
            'Jimmy Butler': 86, 'Draymond Green': 204, 'Dennis Schroder': 472, 'Kyle Anderson': 18, 'Andrew Wiggins': 548},

"HOU": {'Fred VanVleet': 527, 'Dillon Brooks': 749, 'Aaron Holiday': 979, 'Jack McVeigh': 1060, 'Jock Landale': 1485, 'Nate Hinton': 2672, 
           'Jalen Green': 2810, "Jae'Sean Tate": 2650, 'Alperen Sengun': 2847, 'Jabari Smith Jr.': 3489, 'Tari Eason': 3435, 
           'Jeenathan Williams': 3931, 'Amen Thompson': 3977, 'Cam Whitmore': 3978, 'Markquis Nowell': 4028, "N'Faly Dante": 4116, 
           'Reed Sheppard': 4117, 'Jeff Green': 207, 'Samardo Samuels': 869, 'Steven Adams': 4},

"IND": {'Myles Turner': 522, 'Pascal Siakam': 479, 'Thomas Bryant': 753, 'Andrew Nembhard': 3476, 'Moses Brown': 2160, 'James Wiseman': 2666, 
          'Obi Toppin': 2658, 'Tyrese Haliburton': 2595, 'Aaron Nesmith': 2626, 'Isaiah Jackson': 2817, 'Bennedict Mathurin': 3466, 
          'Kendall Brown': 3423, 'Quenton Jackson': 3452, 'Cole Swider': 3493, 'Ben Sheppard': 3979, 'Jarace Walker': 3981, 
          'Enrique Freeman': 4118, 'Johnny Furphy': 4119, 'Tristen Newton': 4120, 'RayJ Dennis': 4122, 'James Johnson': 274, 'T.J. McConnell': 348},

"LAC": {'Norman Powell': 434, 'Ben Simmons': 481, 'Kris Dunn': 152, 'Ivica Zubac': 575, 'Derrick Jones Jr.': 283, 'Mo Bamba': 932, 
            'Drew Eubanks': 966, 'Amir Coffey': 2115, 'Terance Mann': 1877, 'Kevin Porter Jr.': 1888, 'Nate Darling': 2578, 'Braxton Key': 3091, 
            'Bones Hyland': 2816, 'Kai Jones': 2823, 'MarJon Beauchamp': 3405, 'Alondes Williams': 3503, 'Kobe Brown': 3983, 'Jordan Miller': 3984, 
            'Cam Christie': 4121, 'RayJ Dennis': 4122, 'Trentyn Flowers': 4123, 'EJ Harkless': 4124, 'E. Harkless': 4238, 'Nicolas Batum': 40, 
            'James Harden': 216, 'Patty Mills': 365, 'Kawhi Leonard': 314, 'Bogdan Bogdanovic': 743},

"LAL": {"D'Angelo Russell": 462, 'Dorian Finney-Smith': 175, 'Shake Milton': 1001, 'Jarred Vanderbilt': 1036, 'Luka Doncic': 963, 
          'Rui Hachimura': 1862, 'Gabe Vincent': 1775, 'Cam Reddish': 1889, 'Jaxson Hayes': 1864, 'Kylor Kelley': 2670, 'Austin Reaves': 2845, 
          'Jordan Goodwin': 3341, 'Max Christie': 3427, 'Christian Koloko': 3458, 'Colin Castleton': 3987, 'Jalen HoodSchifino': 3990, 
          'Maxwell Lewis': 3991, 'Trey Jemison': 4003, 'Bronny James': 4125, 'Dalton Knecht': 4126, 'Quincy Olivari': 4127, 'Armel Traore': 4128, 
          'Markieff Morris': 374, 'Anthony Davis': 126, 'Alex Len': 313, 'LeBron James': 265},

"MEM": {'Luke Kennard': 814, 'Jaren Jackson Jr.': 982, 'Ja Morant': 1881, 'Brandon Clarke': 1853, 'Miye Oni': 1885, 'John Konchar': 2177, 
             'Desmond Bane': 2568, 'Santi Aldama': 2786, 'Scotty Pippen Jr.': 3477, 'Jay Huff': 2814, 'Jake LaRavia': 3460, 'Vince Williams Jr.': 3508, 
             'Miles Norris': 3942, 'Colin Castleton': 3987, 'GG Jackson': 3994, 'M. Pereira': 4086, 'Armando Bacot': 4129, 'Zach Edey': 4130, 
             'Yuki Kawamura': 4131, 'Cam Spencer': 4132, 'Jaylen Wells': 4133, 'Zyon Pullin': 4136, 'Marcus Smart': 486},

"MIA": {'Terry Rozier': 458, 'Josh Richardson': 446, 'Bam Adebayo': 724, 'Thomas Bryant': 753, 'Duncan Robinson': 1018, 'Haywood Highsmith': 1815, 
 'Tyler Herro': 1866, 'Nassir Little': 1875, 'Josh Christopher': 2799, 'Davion Mitchell': 2834, 'Dru Smith': 3360, 'Nikola Jovic': 3453, 
 'Jamie Jr. Jaquez': 4085, 'Keshad Johnson': 4134, 'Pelle Larsson': 4135, 'Zyon Pullin': 4136, 'Isaiah Stevens': 4137, "Kel'el Ware": 4138, 
 'Caleb Daniels': 4213, 'Kevin Love': 326, 'Alec Burks': 84, 'Jimmy Butler': 86, 'Kyle Anderson': 18, 'Andrew Wiggins': 548},

"MIL": {'Delon Wright': 564, 'Bobby Portis': 431, 'Pat Connaughton': 115, 'Taurean Prince': 437, 'Anzejs Pasecniks': 2204, 'Kyle Kuzma': 820, 
         'Gary Trent Jr.': 1058, 'Terence Davis': 2168, 'Kevin Porter Jr.': 1888, 'Stanley Umude': 3790, 'MarJon Beauchamp': 3405, 
         'Ryan Rollins': 3484, 'A.J. Green': 3443, 'Chris Livingston': 3997, 'Liam Robbins': 4005, 'Andre Jr. Jackson': 4047, 'James Akinjo': 4139, 
         'AJ Johnson': 4140, 'Tyler Smith': 4141, 'Brook Lopez': 323, 'Damian Lillard': 319, 'Khris Middleton': 361, 'Giannis Antetokounmpo': 20},

"MIN": {'P.J. Dozier': 770, 'Keita Bates-Diop': 934, 'Donte DiVincenzo': 962, 'Nickeil Alexander-Walker': 1845, 'Naz Reid': 2146, 
           'Anthony Edwards': 2584, 'Jaden McDaniels': 2621, 'Daishen Nix': 3154, 'Luka Garza': 2807, 'Eugene Omoruyi': 2838, 'Josh Minott': 3470, 
           'Jaylen Clark': 4000, 'Leonard Miller': 4001, 'Tristen Newton': 4120, 'Rob Dillingham': 4142, 'Jesse Edwards': 4143, 
           'Terrence Jr. Shannon': 4144, 'Mike Conley': 114, 'Rudy Gobert': 192, 'Julius Randle': 441, 'Joe Ingles': 258},

"NOP": {'Brandon Ingram': 260, 'Dejounte Murray': 382, 'Daniel Theis': 886, 'Bruce Brown': 944, 'Zion Williamson': 1902, 'Jaylen Nowell': 1882, 
            'Javonte Green': 2404, 'Trhae Mitchell': 3717, 'Matt Ryan': 3195, 'Jeremiah Robinson-Earl': 2846, 'Brandon Boston Jr.': 2792, 
            'Herbert Jones': 2822, 'Trey Murphy III': 2837, 'Jalen Crutcher': 2990, 'Jose Alvarado': 2941, 'Malcolm Hill': 3380, 
            'Karlo Matkovic': 3467, 'Jamal Cain': 3424, 'Jordan Hawkins': 4002, 'Trey Jemison': 4003, 'Yves Missi': 4145, 'Antonio Reeves': 4146, 
            'J Oduro': 4203, 'K. Brooks': 4204, 'CJ McCollum': 347, 'Elfrid Payton': 418},

"NYK": {'Delon Wright': 564, 'Karl-Anthony Towns': 519, 'Cameron Payne': 417, 'O.G. Anunoby': 732, 'Josh Hart': 791, 'Mikal Bridges': 940, 
          'Jalen Brunson': 946, 'Landry Shamet': 1022, 'Chuma Okeke': 1883, 'Moses Brown': 2160, 'Precious Achiuwa': 2561, 'Matt Ryan': 3195, 
          'Miles McBride': 2832, 'Jericho Sims': 2849, 'Jacob Toppin': 4007, 'Pacome Dadiet': 4147, 'Ariel Hukporti': 4148, 'Tyler Kolek': 4149, 
          'T.J. Warren': 540},

"OKC": {'Alex Caruso': 631, 'Isaiah Hartenstein': 978, 'Shai Gilgeous-Alexander': 972, 'Kenrich Williams': 1044, 'Luguentz Dort': 2040, 
           'Isaiah Joe': 2604, 'Aaron Wiggins': 2863, 'Chet Holmgren': 3448, 'Jalen Williams': 3504, 'Jaylin Williams': 3505, 'Ousmane Dieng': 3432, 
           'Cason Wallace': 4009, 'A. Flagler': 4084, 'Alex Ducas': 4151, 'Dillon Jones': 4152, 'Ajay Mitchell': 4153, 'Branden Carlson': 4173, 
           'A. Reese': 4206, 'Miller Kopp': 4214, 'Malevy Leons': 4215, 'Cormac Ryan': 4216},

"ORL": {'Jonathan Isaac': 801, 'Wendell Carter Jr.': 950, 'Moritz Wagner': 1037, 'Goga Bitadze': 1848, 'Jarrett Culver': 1855, 'Cole Anthony': 2563, 
         'Trevelin Queen': 2671, 'Franz Wagner': 2858, 'Jalen Suggs': 2852, 'Javonte Smart': 2917, 'Mac McClung': 2833, 'Ethan Thompson': 3237, 
         'Paolo Banchero': 3414, 'Caleb Houstan': 3449, 'Anthony Black': 4010, 'Jett Howard': 4011, 'Jalen Slawson': 4021, 'Tristan Silva da': 4155, 
         'Cory Joseph': 287, 'Kentavious Caldwell-Pope': 89, 'Gary Harris': 220},

"PHI": {'Kelly Oubre Jr.': 407, 'Guerschon Yabusele': 904, 'Caleb Martin': 2242, 'Chuma Okeke': 1883, 'Quentin Grimes': 2811, 'Tyrese Maxey': 2619, 
          'Jared Butler': 2796, 'Kenyon Martin Jr.': 2617, 'Jeff Dowtin': 2878, 'Isaiah Mobley': 3472, 'Lester Quinones': 3480, 'Pete Nance': 3957, 
          'Ricky IV Council': 4049, 'Adem Bona': 4156, 'Jared McCain': 4159, 'Judah Mintz': 4160, 'Justin Edwards': 4217, 'Max Fiedler': 4218, 
          'Jordan Tucker': 4219, 'Kyle Lowry': 327, 'Eric Gordon': 196, 'Paul George': 189, 'Reggie Jackson': 264, 'Andre Drummond': 147, 
          'Joel Embiid': 159},

"PHX": {'Tyus Jones': 285, 'Frank Kaminsky': 290, 'Devin Booker': 64, "Royce ONeale": 851, 'Damion Lee': 599, 'Monte Morris': 845, 
        'Grayson Allen': 926, 'Josh Okogie': 1010, 'Mamadi Diakite': 2580, 'Bol Bol': 1849, 'Nick Richards': 2639, 'TyTy Washington Jr.': 3497, 
        'Collin Gillespie': 3441, 'Jalen Bridges': 4161, 'Ryan Dunn': 4162, 'Oso Ighodaro': 4163, 'M. Wood': 4208, 'Kevin Durant': 153, 
        'Bradley Beal': 45, 'Mason Plumlee': 426, 'Jusuf Nurkic': 398},

"POR": {"Devonte' Graham": 973, 'Anfernee Simons': 1023, 'Deandre Ayton': 930, 'Robert Williams III': 1045, 'Deni Avdija': 2564, 
           'Dalano Banton': 2788, 'Scoot Henderson': 3408, 'Shaedon Sharpe': 3487, 'Bryce McGowens': 3469, 'Jabari Walker': 3496, 
           'Justin Minaya': 3714, 'Toumani Camara': 4015, 'Kris Murray': 4017, 'Duop Reath': 4018, 'R. Rupert': 4069, 'Donovan Clingan': 4164, 
           'Jerami Grant': 200, 'Taze Moore': 3724},

"SAC": {'Trey Lyles': 331, 'Domantas Sabonis': 463, 'Skal Labissiere': 302, "DeAaron Fox": 776, 'Malik Monk': 842, 'Kevin Huerter': 980, 
         'Jordan McLaughlin': 997, 'Jalen McDaniels': 1880, 'Mason Jones': 2605, 'Brodric Thomas': 2654, 'Terry Taylor': 2853, 'Keegan Murray': 3475, 
         'Orlando Robinson': 3482, 'Keon Ellis': 3436, 'Jake LaRavia': 3460, 'Colby Jones': 4020, 'Devin Carter': 4165, 'Isaiah Crawford': 4166, 
         'Boogie Ellis': 4167, 'Isaac Jones': 4168, 'DeMar DeRozan': 136, 'Jonas Valanciunas': 525, 'Jae Crowder': 121, 'Alex Len': 313, 
         'Zach LaVine': 308, 'Doug McDermott': 351},

"SAS": {'Chris Paul': 415, "DeAaron Fox": 776, 'Zach Collins': 762, 'Jordan McLaughlin': 997, 'Keldon Johnson': 1872, 'Charles Bassey': 2790, 
         'Devin Vassell': 2661, 'Tre Jones': 2606, 'Malachi Flynn': 2587, 'Brandon Boston Jr.': 2792, 'David Duke Jr.': 2804, 'Sandro Mamukelashvili': 2830, 
         'Julian Champagnie': 3425, 'Malaki Branham': 3419, 'Blake Wesley': 3499, 'Jeremy Sochan': 3490, 'Nathan Mensah': 3949, 'Sidy Cissoko': 4024, 
         'Victor Wembanyama': 4026, 'Stephon Castle': 4169, 'Harrison Ingram': 4170, 'Riley Minix': 4171, 'Bismack Biyombo': 54, 'Harrison Barnes': 36},

"TOR": {'Jakob Poeltl': 428, 'Chris Boucher': 745, 'Bruce Brown': 944, 'Bruno Fernando': 1858, 'RJ Barrett': 1846, "Jahmi'us Ramsey": 2637, 
           'Immanuel Quickley': 2636, 'Ochai Agbaji': 3411, 'Davion Mitchell': 2834, 'Scottie Barnes': 2789, 'D.J. Carton': 2797, 'A.J. Lawson': 2890, 
           'Eugene Omoruyi': 2838, 'Orlando Robinson': 3482, 'Jared Rhoden': 3481, 'Gradey Dick': 4027, 'Jamison Battle': 4172, 'Branden Carlson': 4173, 
           'Ulrich Chomche': 4174, 'Jonathan Mogbo': 4175, 'Jamal Shead': 4176, "JaKobe Walter": 4177, 'Garrett Temple': 507, 'Kelly Olynyk': 404},

"UTA": {'Lauri Markkanen': 830, 'John Collins': 761, 'Svi Mykhailiuk': 1006, 'Collin Sexton': 1021, 'Drew Eubanks': 966, 'Johnny Juzang': 3454, 
        'Jason Preston': 2842, 'Micah Potter': 3358, 'Walker Kessler': 3457, 'Oscar Tshiebwe': 3980, 'Jalen HoodSchifino': 3990, 'Keyonte George': 4029, 
        'Taylor Hendricks': 4031, 'Brice Sensabaugh': 4034, 'EJ Harkless': 4124, 'Isaiah Collier': 4178, 'Kyle Filipowski': 4179, 'Cody Williams': 4181, 
        'Patty Mills': 365, 'Jordan Clarkson': 109},

"WAS": {'Richaun Holmes': 246, 'Malcolm Brogdon': 71, 'Kyle Kuzma': 820, 'Marvin Bagley III': 931, 'Jaylen Nowell': 1882, 'Jordan Poole': 1887, 
           'Kira Lewis Jr.': 2611, 'Jared Butler': 2796, 'Anthony Gill': 2590, 'Justin Champagnie': 2798, 'Corey Kispert': 2825, 'Johnny Davis': 3428, 
           'Patrick Baldwin Jr.': 3413, 'Bilal Coulibaly': 4036, 'T. Vukcevic': 4088, 'AJ Johnson': 4140, 'Carlton Carrington': 4182, 
           'Kyshawn George': 4183, 'Alex Sarr': 4184, 'T. Funk': 4235, 'Jonas Valanciunas': 525}

}