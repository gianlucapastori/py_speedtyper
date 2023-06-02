import curses 

class Keys:
    # reference for ascii table: https://theasciicode.com.ar/
    # useful arrays.
    alphabet = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122] 

    # keys.
    space = 32
    esc = 27
    backspace = [8, 127, curses.KEY_BACKSPACE]

    num_1 = 49
    num_2 = 50
    num_3 = 51
    num_4 = 52

class Data:
    br_words = ["alquimista", "herdar", "violento", "marcapasso", "saque", "aferir", "demografia", "aquilo", "perecer", "transigir", "pastorear", "bastar", "ataxia", "debilidade", "aliás", "legar", "abstração", "mente", "formal", "glicerina", "chinesa", "cor", "sufocar", "lugarejo", "stalker", "peixe", "segurava", "acuidade", "desnudar", "desfalcar", "rasante", "inadimplência", "estancar", "debilidade", "jipe", "bochechudo", "alpendre", "grelhado", "outrem", "atoalhado", "funicular", "zebu", "adágio", "bilionário", "cinza", "jardim", "achada", "manducar", "Havaí", "fundar", "minerva", "evaporar", "musculação", "comissionamento", "cruz", "ociosidade", "rock", "reconsiderar", "cádmio", "presidencial", "pélvica", "filológico", "expressionismo", "sarcófago", "arranha-céu", "monóculo", "desacatado", "tipificação", "inculpar", "mecânica"]
    en_words = ["episode", "rainbow", "popular", "bargain", "bucket", "fall", "painter", "sacred", "vat", "collection", "revenge", "world", "assessment", "assembly", "credibility", "welfare", "relax", "like", "permanent", "shed", "skin", "rebellion", "traffic", "captivate", "program", "roll", "absorb", "elapse", "global", "herb", "snow", "assertive", "bay", "presidency", "network", "conspiracy", "laboratory", "brain", "quote", "kill", "elite", "twist", "room", "ignite", "important", "missile", "mechanism", "astonishing", "concept", "harmful", "liberal", "act", "rear", "extraterrestrial", "deposit", "passive", "recruit", "talkative", "salmon", "circumstance", "joystick", "confusion", "dialogue", "shelter", "bacon", "tray", "protest", "concentrate", "diagram", "mill", "passage", "conductor", "spine", "pound", "ladder", "elephant", "retired", "privilege", "trouble", "force", "in", "donor", "abnormal", "fling", "gloom", "communist", "neglect", "smile", "concern", "cathedral", "worth", "school", "magnitude", "creep", "tumour", "tournament", "healthy", "shell", "witness", "doll", "provoke", "undress", "publish", "participate", "cereal", "hit", "site", "deadly", "wreck", "alive", "recycle", "glasses", "cheese", "printer", "soul", "bind", "novel", "rule", "tumour", "know", "response", "stand", "trouser", "lead", "retreat", "choose", "perceive", "price", "vague", "garage", "vigorous", "transition", "ballet", "combine", "boy", "pursuit", "execution", "folk", "correspond", "handy", "mainstream", "suburb", "bald", "stomach", "trip", "palace", "costume", "forge", "permission", "bat"]
