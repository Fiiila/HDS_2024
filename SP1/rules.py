# Rules for phonetic translation based on phonetic alphabet EPA

# Vowels and diphthongs (samohlasky a dvojhlasky)
# 'a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú/ů'
VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# 'ou', 'au', 'eu'
DIPHTHONGS = ['y', 'Y', 'F']
V = VOWELS + DIPHTHONGS

# Voiced paired consonants (Znele parove souhlasky)
# 'b', 'd', 'ď', 'g', 'v', 'z', 'ž', 'h', 'dz', 'dž', 'ř'
ZPK = ['b', 'd', 'D', 'g', 'v', 'z', 'Z', 'h', 'w', 'W', 'R']

# Unvoiced paired consonants (Neznele parove souhlasky)
# 'p', 't', 'ť', 'k', 'f', 's', 'š', 'ch', 'c', 'č', 'ř'
NPK = ['p', 't', 'T', 'k', 'f', 's', 'S', 'x', 'c', 'C', 'Q']

# Unique consonants (Jedinecne souhlasky)
# 'm', 'n', 'ň', 'l', 'r', 'j'
JK = ['m', 'n', 'J', 'l', 'r', 'j']

# Consonants (souhlasky)
K = ZPK + NPK + JK

# Voiced to unvoiced consonant pairs (pary znela-neznela souhlaska)
VOICED_TO_UNVOICED_CONSONANT_PAIRS = {
    'b': 'p',
    'd': 't',
    'D': 'T',
    'g': 'k',
    'v': 'f',
    'z': 's',
    'Z': 'S',
    'h': 'x',
    'w': 'c',
    'W': 'C',
    'R': 'Q'
}

# Unvoiced to voiced consonant pairs (pary neznela-znela souhlaska)
UNVOICED_TO_VOICED_CONSONANT_PAIRS = {
    'p': 'b',
    't': 'd',
    'T': 'D',
    'k': 'g',
    'f': 'v',
    's': 'z',
    'S': 'Z',
    'x': 'h',
    'c': 'w',
    'C': 'W',
    'Q': 'R'
}

# Nonsyllabic prepositions (neslabicne predlozky)
NP = ['k', 's', 'v', 'z']

# monosyllabic prepositions ending with voiced consonant (jednoslabicne predlozky koncici znelou souhlaskou)
# 'bez', 'nad', 'od', 'od', 'pod', 'před'
JPZ = ['bez', 'nad', 'od', 'od', 'pod', 'před']

# Long pause at the start and end of the sentence (dlouha pauza na zacatku a konci vety)
PAUSE_LONG = '$'

# Short pause between word (kratka pauza mezi slovy)
PAUSE_SHORT = '#'

# Basic rules
BASIC_RULES = {
    # joining consonants and vowels (spojeni souhlasek a samohlasek)
    'bě': 'bje',
    'pě': 'pje',
    'vě': 'vje',

    'di': 'Di', 'dí': 'DI',
    'ti': 'Ti', 'tí': 'TI',
    'ni': 'Ji', 'ní': 'JI',

    'dě': 'De',
    'tě': 'Te',
    'ně': 'Je',
    'mě': 'mJe',

    'js': 's',

    # vowels (vokaly)
    'i': 'i',
    'e': 'e',
    'a': 'a',
    'o': 'o',
    'u': 'u',
    'í': 'I',
    r'é': 'E',
    'á': 'A',
    'ó': 'O',
    'ú|ů': 'U',

    # replacement of y/ý
    'y': 'i',
    'ý': 'I',

    # diphthongs (diftongy)
    'ou': 'y',
    'au': 'Y',
    'eu': 'F',

    # replacement of x
    r'x\s[b, d, ď, g, v, z, ž, h, dz, dž, ř]': lambda x: x.group().replace("x", "gz"),
    'x': 'ks',

    # fricatives (frikativy)
    'f': 'f',
    'v': 'v',
    's': 's',
    'z': 'z',
    'š': 'S',
    'ž': 'Z',
    'ch': 'x',
    'h': 'h',
    'l': 'l',
    'r': 'r',
    'ř': 'R',
    'j': 'j',

    # plosives (plozivy)
    'p': 'p',
    'b': 'b',
    't': 't',
    'd': 'd',
    'ť': 'T',
    'ď': 'D',
    'k': 'k',
    'g': 'g',

    # nasals (nazaly)
    'm': 'm',
    'n': 'n',
    'ň': 'J',

    # africals (afrikaly)
    'c': 'c',
    'č': 'C',
    'dz': 'w',
    'dZ': 'W',

    # important allophones
    # ?
    'n[k,g]': lambda x: x.group().replace("n", "N"),
    'm[v,f]': lambda x: x.group().replace("m", "M"),
    'x|': lambda x: x.group().replace("x", "G"),
    '[p,t,T,k,f,s,S,x,c,C,Q]R': lambda x: x.group().replace("R", "Q"),
    f'[{",".join(K)}]r[{",".join(K)}|\\|]': lambda x: x.group().replace("r", "P"),
    f'[{",".join(K)}]l[{",".join(K)}|\\|]': lambda x: x.group().replace("l", "L"),
    f'[{",".join(K)}]m[{",".join([k for k in K if not k in ["r","l"]])}|\\|]': lambda x: x.group().replace("m", "H"),

    # interpunction
    r',\s|,\s': '#',
    r'\| \|': '|',
    r'[\.?!]': '$',

    # voiced paired consonants ZPK-NPK
    # f'[{",".join(ZPK)}][\\|[{",".join(NPK)},{",".join(JK)},{",".join(V),"!", "#"}]|[{",".join(NPK)}]]': lambda x: x.group().replace(x.group()[0], VOICED_TO_UNVOICED_CONSONANT_PAIRS[x.group()[0]]),
    # f'[{",".join(ZPK)}]\\|[{",".join(NPK)},{",".join(JK)},{",".join(V)},!,#]': lambda x: x.group().replace(x.group()[0], VOICED_TO_UNVOICED_CONSONANT_PAIRS[x.group()[0]]),
    f'[{",".join(ZPK)}]\\|[{",".join(NPK)}]': lambda x: x.group().replace(x.group()[0], VOICED_TO_UNVOICED_CONSONANT_PAIRS[x.group()[0]]),
    f'[{",".join(ZPK)}]\\|[[{",".join(JK)}]]': lambda x: x.group().replace(x.group()[0], VOICED_TO_UNVOICED_CONSONANT_PAIRS[x.group()[0]]),
    f'[{",".join(ZPK)}]\\|[{",".join(V)}]': lambda x: x.group().replace(x.group()[0], VOICED_TO_UNVOICED_CONSONANT_PAIRS[x.group()[0]]),
    f'[{",".join(ZPK)}]\\|[!,#]': lambda x: x.group().replace(x.group()[0], VOICED_TO_UNVOICED_CONSONANT_PAIRS[x.group()[0]]),
    f'[{",".join(ZPK)}][{",".join(NPK)}]]': lambda x: x.group().replace(x.group()[0], VOICED_TO_UNVOICED_CONSONANT_PAIRS[x.group()[0]]),

    # unvoiced paired consonants NPK-ZPK
    f'[{",".join(NPK)}][\\|[{",".join(ZPK)}]|[{",".join(ZPK)}]]': lambda x: x.group().replace(x.group()[0], UNVOICED_TO_VOICED_CONSONANT_PAIRS[x.group()[0]]),

    # other assimilation rules
    f'v[{",".join(NPK)}]': lambda x: x.group().replace('v', 'f'),
    # f'[{",".join(ZPK)}][\\|v]': lambda x: x.group().replace('v', 'f'),

    # impact use (pouziti razu)
    f'\\|[{",".join(VOWELS)}]': lambda x: x.group().replace("|", "|!"),
    f'#[|][{",".join(V)}]': lambda x: x.group().replace("|", "|!"),
    f'[|][{",".join(NP)}][|][{",".join(V)}]': lambda x: x.group()[:-1] + x.group()[-1].replace("|", "|!"),
}