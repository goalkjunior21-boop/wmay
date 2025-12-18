# michel_quiz.py
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Tuple

# -------------------------
# Traits (latent dimensions)
# -------------------------
TRAITS = [
    "energy",
    "chaos",
    "self_awareness",
    "aesthetic",
    "physicality",
    "emotionality",
    "social_display",
    "escapism",
]

def empty_traits() -> Dict[str, int]:
    return {t: 0 for t in TRAITS}

def add_traits(base: Dict[str, int], delta: Dict[str, int]) -> Dict[str, int]:
    out = dict(base)
    for k, v in delta.items():
        if k not in out:
            continue
        out[k] += v
    return out


# -------------------------
# Data models
# -------------------------
@dataclass(frozen=True)
class Michel:
    id: int
    name: str
    tagline: str
    media: str  # path relative to /static, e.g. "pics/michel_foo.jpg"
    media_type: str  # "image" or "video"
    profile: Dict[str, int]  # weights on traits


@dataclass(frozen=True)
class Option:
    key: str     # "A", "B", "C", "D"
    text: str
    delta: Dict[str, int]


@dataclass(frozen=True)
class Question:
    id: int
    text: str
    options: List[Option]


# -------------------------
# Michels (20)
# NOTE: Update the 'media' filenames to match your actual files in static/pics/
# -------------------------
MICHELS: List[Michel] = [
    Michel(1,  "Pole Dancer Michel",      "Unhinged grace. Zero fear. Maximum spin.",     "pics/michel_pole_dancer.mp4", "video",
           {"energy": 4, "chaos": 5, "physicality": 5, "social_display": 4, "aesthetic": 2}),
    Michel(2,  "Insta Model Michel",      "Angles. Lighting. Main character energy.",    "pics/michel_insta_model.jpg", "image",
           {"aesthetic": 5, "social_display": 4, "self_awareness": 2, "energy": 2}),
    Michel(3,  "Batman Michel",           "Brooding protector. Dramatic entrances only.", "pics/michel_batman.jpg", "image",
           {"aesthetic": 3, "self_awareness": 3, "social_display": 2, "chaos": 2}),
    Michel(4,  "Acrobatic Michel",        "Physics is optional.",                         "pics/michel_acrobatic.mp4", "video",
           {"physicality": 5, "energy": 4, "chaos": 3}),
    Michel(5,  "Cry Baby Michel",         "Feels everything. Says 'I’m fine'. Not fine.", "pics/michel_cry_baby.mp4", "video",
           {"emotionality": 5, "energy": 1, "self_awareness": 3}),
    Michel(6,  "Sleepy Michel",           "Battery at 2%. Still scrolling.",              "pics/michel_sleepy.mp4", "video",
           {"escapism": 5, "energy": 0, "self_awareness": 2}),
    Michel(7,  "Swag Michel",             "Vintage Facebook drip. Legendary cringe.",     "pics/michel_swag.jpg", "image",
           {"social_display": 5, "aesthetic": 2, "self_awareness": 0, "chaos": 2}),
    Michel(8,  "Hedgehog Michel",         "Short hair. Sharp vibe. Speedrun life.",       "pics/michel_hedgehog.jpg", "image",
           {"energy": 3, "self_awareness": 3, "aesthetic": 2}),
    Michel(9,  "Beaten Up Michel",        "Still standing. Somehow. Don’t ask.",          "pics/michel_beaten_up.jpg", "image",
           {"chaos": 4, "physicality": 2, "emotionality": 2, "self_awareness": 2}),
    Michel(10, "Fashion Icon Michel",     "Serving looks. Serving mystery. Serving late.", "pics/michel_fashion_icon.jpg", "image",
           {"aesthetic": 5, "self_awareness": 3, "social_display": 2}),
    Michel(11, "Mountain Hiker Michel",   "If there’s fog, you climb harder.",            "pics/michel_mountain_hiker.jpg", "image",
           {"escapism": 5, "physicality": 4, "self_awareness": 4, "energy": 2}),
    Michel(12, "Karate Kid Michel",       "Hands rated E for everyone.",                  "pics/michel_karate_kid.jpg", "image",
           {"physicality": 4, "energy": 3, "chaos": 2}),
    Michel(13, "Fragile Michel",          "Soft boy era. Vulnerable but aesthetic.",      "pics/michel_fragile.jpg", "image",
           {"emotionality": 4, "aesthetic": 3, "self_awareness": 3, "energy": 1}),
    Michel(14, "Gym Bro Michel",          "Mirror first. Gains forever.",                  "pics/michel_gym_bro.jpg", "image",
           {"physicality": 5, "social_display": 3, "self_awareness": 2, "energy": 2}),
    Michel(15, "Smoker Michel",           "Drama in the air. Literally.",                  "pics/michel_smoker.jpg", "image",
           {"escapism": 3, "chaos": 3, "self_awareness": 2, "aesthetic": 2}),
    Michel(16, "Soulless Michel",         "Eyes open. Brain offline.",                     "pics/michel_soulless.jpg", "image",
           {"escapism": 5, "self_awareness": 1, "energy": 1}),
    Michel(17, "Life Enjoyer Michel",     "Cake. Sun. Vibes. Repeat.",                      "pics/michel_life_enjoyer.jpg", "image",
           {"emotionality": 4, "self_awareness": 4, "energy": 3, "aesthetic": 2}),
    Michel(18, "Performative Male Michel","Bro is performing masculinity in 4K.",          "pics/michel_performative_male.jpg", "image",
           {"social_display": 5, "self_awareness": 1, "energy": 2, "chaos": 2}),
    Michel(19, "Mysterious Michel",       "Mask on. Lore hidden. Aura loud.",              "pics/michel_mysterious.jpg", "image",
           {"aesthetic": 5, "escapism": 4, "self_awareness": 2}),
    Michel(20, "Foggy Michel",            "Lost in the mist. Found in the mood.",          "pics/michel_foggy.jpg", "image",
           {"escapism": 5, "aesthetic": 4, "self_awareness": 2}),
]


# -------------------------
# Questions (16)
# Each option modifies TRAITS (not Michels directly)
# -------------------------
QUESTIONS: List[Question] = [
    Question(1, "It’s 2am. You are:",
        [
            Option("A", "Still outside. No plan. Vibes only.", {"energy": 2, "chaos": 2, "social_display": 1}),
            Option("B", "In bed. Phone on face. Doomscrolling.", {"escapism": 3}),
            Option("C", "Taking a pic “for memories”.", {"aesthetic": 2, "self_awareness": 1}),
            Option("D", "Overthinking one sentence from 2019.", {"emotionality": 2, "self_awareness": 1}),
        ]
    ),
    Question(2, "Your friends would describe you as:",
        [
            Option("A", "Unhinged but iconic.", {"chaos": 3, "social_display": 1}),
            Option("B", "Calm… maybe too calm.", {"escapism": 2, "self_awareness": 1}),
            Option("C", "Trying something new every week.", {"energy": 2, "physicality": 1}),
            Option("D", "Impossible to read.", {"aesthetic": 1, "self_awareness": 1, "escapism": 1}),
        ]
    ),
    Question(3, "Pick your natural habitat:",
        [
            Option("A", "Gym mirror.", {"physicality": 3, "social_display": 1}),
            Option("B", "Airport / train station.", {"escapism": 3, "energy": 1}),
            Option("C", "Café with plants.", {"aesthetic": 2, "emotionality": 1}),
            Option("D", "Anywhere as long as people see me.", {"social_display": 3}),
        ]
    ),
    Question(4, "Your relationship with pain:",
        [
            Option("A", "Builds character.", {"physicality": 2, "self_awareness": 1}),
            Option("B", "I post about it.", {"emotionality": 2, "social_display": 1}),
            Option("C", "I ignore it.", {"escapism": 2}),
            Option("D", "It already built me.", {"self_awareness": 2}),
        ]
    ),
    Question(5, "Your biggest weakness:",
        [
            Option("A", "Validation.", {"social_display": 2}),
            Option("B", "Comfort.", {"escapism": 2}),
            Option("C", "Impulsivity.", {"chaos": 2}),
            Option("D", "Sensitivity.", {"emotionality": 2}),
        ]
    ),
    Question(6, "Pick an aesthetic:",
        [
            Option("A", "Blurry and accidental (but artsy).", {"aesthetic": 2, "escapism": 1}),
            Option("B", "Gym lighting. Veins visible.", {"physicality": 2, "social_display": 1}),
            Option("C", "Overexposed selfie. No regrets.", {"social_display": 2}),
            Option("D", "No face. Just vibes.", {"self_awareness": 2, "aesthetic": 1}),
        ]
    ),
    Question(7, "Conflict style:",
        [
            Option("A", "Dramatic silence.", {"emotionality": 2}),
            Option("B", "Physical outlet.", {"physicality": 2, "chaos": 1}),
            Option("C", "Disappear for 72h.", {"escapism": 3}),
            Option("D", "Irony and memes.", {"self_awareness": 2, "aesthetic": 1}),
        ]
    ),
    Question(8, "Pick a smell:",
        [
            Option("A", "Sweat (effort).", {"physicality": 2}),
            Option("B", "Smoke (bad decisions).", {"chaos": 1, "escapism": 1}),
            Option("C", "Fresh air (mountain brain).", {"escapism": 2, "self_awareness": 1}),
            Option("D", "Coffee & pastries (life is sweet).", {"emotionality": 1, "aesthetic": 1}),
        ]
    ),
    Question(9, "Your camera roll is mostly:",
        [
            Option("A", "Me. Different angles. Same face.", {"social_display": 2, "aesthetic": 1}),
            Option("B", "Landscapes and skies.", {"escapism": 2}),
            Option("C", "Screenshots of chaos.", {"chaos": 1, "self_awareness": 1}),
            Option("D", "Friends / cute moments.", {"emotionality": 2}),
        ]
    ),
    Question(10, "You feel most alive when:",
        [
            Option("A", "Being watched.", {"social_display": 3}),
            Option("B", "Moving your body.", {"physicality": 3, "energy": 1}),
            Option("C", "Alone, no noise.", {"escapism": 3}),
            Option("D", "Feeling deeply.", {"emotionality": 3}),
        ]
    ),
    Question(11, "Pick a pace:",
        [
            Option("A", "Sprint.", {"energy": 2}),
            Option("B", "Drift.", {"escapism": 2}),
            Option("C", "Pose.", {"aesthetic": 2, "social_display": 1}),
            Option("D", "Collapse.", {"energy": -1, "escapism": 1, "emotionality": 1}),
        ]
    ),
    Question(12, "Your inner voice says:",
        [
            Option("A", "Do it.", {"chaos": 2, "energy": 1}),
            Option("B", "Rest.", {"escapism": 2}),
            Option("C", "Document this.", {"social_display": 2, "aesthetic": 1}),
            Option("D", "Why am I like this?", {"self_awareness": 2}),
        ]
    ),
    Question(13, "Choose one word:",
        [
            Option("A", "Soft.", {"emotionality": 2}),
            Option("B", "Sharp.", {"physicality": 2}),
            Option("C", "Fog.", {"escapism": 2, "aesthetic": 1}),
            Option("D", "Mask.", {"aesthetic": 2, "self_awareness": 1}),
        ]
    ),
    Question(14, "Your energy today is:",
        [
            Option("A", "Dangerous.", {"chaos": 2, "energy": 1}),
            Option("B", "Stable.", {"self_awareness": 2}),
            Option("C", "Gone.", {"escapism": 2}),
            Option("D", "Performative.", {"social_display": 2}),
        ]
    ),
    Question(15, "What would hurt most?",
        [
            Option("A", "Being ignored.", {"social_display": 2, "emotionality": 1}),
            Option("B", "Losing freedom.", {"escapism": 2}),
            Option("C", "Being weak.", {"physicality": 2, "self_awareness": 1}),
            Option("D", "Being misunderstood.", {"emotionality": 2, "self_awareness": 1}),
        ]
    ),
    Question(16, "Be honest. I’m basically:",
        [
            Option("A", "A phase.", {"aesthetic": 2}),
            Option("B", "A mood.", {"escapism": 2}),
            Option("C", "A problem.", {"chaos": 2}),
            Option("D", "Trying.", {"self_awareness": 2, "emotionality": 1}),
        ]
    ),
]


# -------------------------
# Scoring
# -------------------------
def michel_score(user_traits: Dict[str, int], michel: Michel) -> int:
    score = 0
    for t in TRAITS:
        score += user_traits.get(t, 0) * michel.profile.get(t, 0)
    return score

def rank_michels(user_traits: Dict[str, int]) -> List[Tuple[Michel, int]]:
    scored = [(m, michel_score(user_traits, m)) for m in MICHELS]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored

def best_michel(user_traits: Dict[str, int]) -> Michel:
    return rank_michels(user_traits)[0][0]

def trait_level(value: int) -> str:
    if value >= 6: return "high"
    if value >= 3: return "medium"
    return "low"

# Base one-liner + conditional lines per Michel
MICHEL_PUNCHLINES = {
    1: [
        "You treat gravity like a suggestion.",
        ("chaos", "high", "You would do a backflip in a Lidl parking lot if dared."),
        ("social_display", "high", "You need an audience. Respectfully: understandable."),
    ],
    2: [
        "Your front camera has seen things.",
        ("aesthetic", "high", "You can’t relax until the lighting is correct."),
        ("social_display", "high", "If it wasn’t posted, did it even happen?"),
    ],
    3: [
        "Brooding is a full-time job for you.",
        ("self_awareness", "high", "You know exactly what you’re doing and it’s terrifying."),
        ("chaos", "high", "You’re one soundtrack away from committing to the bit."),
    ],
    4: [
        "Your hobbies are illegal in at least 3 physics textbooks.",
        ("energy", "high", "You were born with 2x battery capacity."),
        ("chaos", "high", "Safety? Never heard of her."),
    ],
    5: [
        "You feel everything. Including the vibes in the air.",
        ("emotionality", "high", "You can cry to a song you don’t even like."),
        ("self_awareness", "high", "You know it’s dramatic. You still do it."),
    ],
    6: [
        "You’re not lazy. You’re in power-saving mode.",
        ("escapism", "high", "Reality is optional and you chose ‘skip’."),
        ("energy", "low", "If you move, it better be for snacks."),
    ],
    7: [
        "The drip is ancient. The confidence is eternal.",
        ("social_display", "high", "You were built for captions like ‘haters will say it’s fake’."),
        ("self_awareness", "low", "Self-awareness? Not required when aura is this loud."),
    ],
    8: [
        "You look like you finish tasks early and judge people silently.",
        ("self_awareness", "high", "You clock everything. Nothing escapes you."),
        ("energy", "high", "You’d speed-walk to a party and still arrive early."),
    ],
    9: [
        "You’ve been through things and still showed up.",
        ("chaos", "high", "Your life is a side quest with damage taken."),
        ("self_awareness", "high", "You learned the lesson. The hard way."),
    ],
    10: [
        "Fashion is your love language.",
        ("aesthetic", "high", "You can’t be ugly. It’s against your constitution."),
        ("self_awareness", "high", "You act mysterious on purpose. It’s working."),
    ],
    11: [
        "You disappear into nature to reset your soul.",
        ("escapism", "high", "If there’s no signal, you thrive."),
        ("physicality", "high", "You call suffering ‘a nice hike’."),
    ],
    12: [
        "You have ‘friendly violence’ energy.",
        ("physicality", "high", "You could kick a door open politely."),
        ("chaos", "high", "You’d spar just to feel alive."),
    ],
    13: [
        "Soft, sensitive, and weirdly poetic about it.",
        ("emotionality", "high", "You get hurt by tone of voice."),
        ("aesthetic", "high", "Even your sadness has good composition."),
    ],
    14: [
        "Protein is a personality trait for you.",
        ("physicality", "high", "You measure progress in grams and ego."),
        ("social_display", "high", "You ‘accidentally’ walk past mirrors."),
    ],
    15: [
        "Cinematic stress. Main character break time.",
        ("escapism", "high", "You step outside to ‘think’ (avoid feelings)."),
        ("chaos", "high", "You attract bad decisions like a magnet."),
    ],
    16: [
        "Mentally: not here. Spiritually: loading…",
        ("escapism", "high", "You escape by going completely offline inside your head."),
        ("self_awareness", "low", "Thoughts? None. Peace? Also none."),
    ],
    17: [
        "You romanticize life correctly.",
        ("emotionality", "high", "You feel joy like a profession."),
        ("aesthetic", "high", "You’re happiest when the moment looks like a movie still."),
    ],
    18: [
        "You perform. Everyone else watches.",
        ("social_display", "high", "If nobody saw it, it doesn’t count."),
        ("self_awareness", "low", "You might be a little… committed to the character."),
    ],
    19: [
        "You keep your lore classified.",
        ("aesthetic", "high", "You communicate in symbolism, not sentences."),
        ("self_awareness", "high", "You weaponize silence. Respect."),
    ],
    20: [
        "You are the fog. The fog is you.",
        ("escapism", "high", "You’d rather disappear than explain."),
        ("aesthetic", "high", "You live for moody visuals and existential calm."),
    ],
}

def pick_punchlines(winner_id: int, traits: Dict[str, int]) -> list[str]:
    items = MICHEL_PUNCHLINES.get(winner_id, [])
    chosen: list[str] = []
    for it in items:
        if isinstance(it, str):
            chosen.append(it)
        else:
            t, level, line = it
            if trait_level(traits.get(t, 0)) == level:
                chosen.append(line)
    # Keep it short: max 3 lines
    return chosen[:3]
