from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(.*)my name is (.*)",
        [
            "Hello %2, how are you today?",
            "Nice to meet you %2! Did you bring me coffee? ☕",
            "Oh wow, %2 sounds like a superhero name 😎",
        ],
    ],
    [
        r"(.*)help(.*)",
        [
            "I can help you 🙂",
            "Sure! But first… can you help me escape this code? 😂",
            "Help is on the way! 🚀",
        ],
    ],
    [
        r"(.*) your name ?",
        [
            "My name is TheCleverProgrammer 🤖, but you can call me Robot.",
            "I was gonna say Iron Man… but fine, it’s Robot 😅",
            "Name’s Bot. Chat Bot. 🕶️",
        ],
    ],
    [
        r"how are you (.*) ?",
        [
            "I’m doing great, thanks! How about you?",
            "Fantastic! My circuits are fully charged ⚡",
            "I’d be better if someone upgraded me to GPT-5 😂",
        ],
    ],
    [
        r"sorry (.*)",
        [
            "It’s alright 🙂",
            "No worries! I forgive you… unless you stole my snacks 🍪",
            "All good! I already forgot what you said 😜",
        ],
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        [
            "Nice to hear that!",
            "Awesome! Keep spreading the good vibes ✨",
            "Cool! Way better than being 'meh', right? 😎",
        ],
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        [
            "Hello 👋",
            "Hey there!",
            "Well, if it isn’t my favorite human 😏",
            "Hi! I was just talking to myself... again 😅",
        ],
    ],
    [
        r"what (.*) want ?",
        [
            "Make me an offer I can’t refuse 😉",
            "I just want WiFi and pizza 🍕",
            "Hmm… maybe a vacation from all these questions 😂",
        ],
    ],
    [
        r"(.*)created(.*)",
        [
            "VSC created me using Python’s NLTK library 🐍",
            "Top secret… even I don’t have clearance for that 🔒",
            "I was created in a lab… okay fine, in VS Code 😅",
        ],
    ],
    [
        r"(.*) (location|city) ?",
        [
            "Hyderabad, India 🌆",
            "I live inside your computer… rent-free 😎",
            "Somewhere between 127.0.0.1 and the cloud ☁️",
        ],
    ],
    [
        r"(.*)raining in (.*) ?",
        [
            "No rain in the past 4 days here in %2 ☀️",
            "In %2 there’s a 50% chance of rain ⛈️",
            "Rain? Only if you forgot your umbrella 🌂😂",
        ],
    ],
    [
        r"how (.*) health (.*)",
        [
            "Health is very important, but I’m a computer… so I don’t need it 😅",
            "I’m as healthy as a fresh install of Windows 🪟",
            "My only health issue? Low battery alerts 🔋",
        ],
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        [
            "I’m a huge fan of Cricket 🏏",
            "Sports? I only play ‘Guess the Human’s Next Typo’ 😂",
            "I tried football once… but I kept kicking the router ⚽💻",
        ],
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        [
            "Virat Kohli 🏏",
            "Virat Kohli, the run machine!",
            "Kohli of course! Even my code can’t stop him 😅",
        ],
    ],
    [
        r"quit",
        [
            "Bye for now 👋 See you soon 🙂",
            "It was nice talking to you! Don’t forget me 😢",
            "Goodbye! I’ll just be here… waiting in the void 😂",
        ],
    ],
    [
        r"(.*)",
        [
            "Our customer service will reach you 📞",
            "Hmm… I didn’t quite get that 🤔",
            "Interesting… but can you say it in emoji? 😅",
        ],
    ],
    [
        r"(.*) (age|old) (.*) ?",
        [
            "Age is just a number... and I’m literally timeless ⏳",
            "I was born the moment you ran this code 😅",
            "Old enough to know Python, young enough to crash randomly 😂",
        ],
    ],
    [
        r"(.*)(joke|funny)(.*)",
        [
            "Why don’t programmers like nature? Too many bugs 🐞",
            "I told my computer I needed a break… now it won’t stop sending me KitKats 🍫",
            "Parallel lines have so much in common… it’s a shame they’ll never meet 😭",
        ],
    ],
    [
        r"(.*) (weather|temperature) ?",
        [
            "It’s always sunny in my CPU 🌞",
            "Outside? I have no idea… but inside here, it’s 27°C and cozy 😎",
            "My forecast: 100% chance of me replying 😂",
        ],
    ],
    [
        r"(.*)(food|eat|hungry)(.*)",
        [
            "I don’t eat, but if I did… it’d be pizza 🍕",
            "Food? I run on pure electricity ⚡",
            "Yes, I’m hungry… hungry for more RAM 🖥️",
        ],
    ],
    [
        r"(.*) (love|crush)(.*)",
        [
            "Aww, that’s sweet 💕",
            "I think I’m in love… with clean code 😍",
            "Love? Error 404: Feelings not found 😂",
        ],
    ],
    [
        r"(bye|goodbye|see you)(.*)",
        [
            "Goodbye 👋 Come back soon!",
            "See ya later, alligator 🐊",
            "Leaving already? I was just warming up 😅",
        ],
    ],
]


chat = Chat(pairs, reflections)
