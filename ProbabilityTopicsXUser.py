import pickle

users = pickle.load (open ("usersWithTweetsFlor.p","rb"))

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

frecuency = {}

stopwords = ["un", "una", "unas", "unos", "uno", "sobre", "todo", "tambien", "tras", "otro", "algun", "alguno", "alguna", "algunos", "algunas", "ser", "es", "soy", "eres", "somos", "sois", "estoy", "esta", "estamos", "estais", "estan", "como", "en", "para", "atras", "porque", "por que", "estado", "estaba", "ante", "antes", "siendo", "ambos", "pero", "por", "poder", "puede", "puedo", "podemos", "podeis", "pueden", "fui", "fue", "fuimos", "fueron", "hacer", "hago", "hace", "hacemos", "haceis", "hacen", "cada", "fin", "incluso", "primero", "desde", "conseguir", "consigo", "consigue", "consigues", "conseguimos", "consiguen", "ir", "voy", "va", "vamos", "vais", "van", "vaya", "gueno", "ha", "tener", "tengo", "tiene", "tenemos", "teneis", "tienen", "el", "la", "lo", "las", "los", "su", "aqui", "mio", "tuyo", "ellos", "ellas", "nos", "nosotros", "vosotros", "vosotras", "si", "dentro", "solo", "solamente", "saber", "sabes", "sabe", "sabemos", "sabeis", "saben", "ultimo", "largo", "bastante", "haces", "muchos", "aquellos", "aquellas", "sus", "entonces", "tiempo", "verdad", "verdadero", "verdadera", "cierto", "ciertos", "cierta", "ciertas", "intentar", "intento", "intenta", "intentas", "intentamos", "intentais", "intentan", "dos", "bajo", "arriba", "encima", "usar", "uso", "usas", "usa", "usamos", "usais", "usan", "emplear", "empleo", "empleas", "emplean", "ampleamos", "empleais", "valor", "muy", "era", "eras", "eramos", "eran", "modo", "bien", "cual", "cuando", "donde", "mientras", "quien", "con", "entre", "sin", "trabajo", "trabajar", "trabajas", "trabaja", "trabajamos", "trabajais", "trabajan", "podria", "podrias", "podriamos", "podrian", "podriais", "yo", "aquel"]

topics = {"Politics" : ["impunidad", "Aristegui", "Bronco", "Gobierno",  "Autonomia", "Autoridad", "Ayotzinapa", "2deOctubre", "justicia"], 
		  "Feminism" : ["Feminicidios", "genero", "Feminismo", "Feminista", "Mujer", "revolucion", "dignidad", "igualdad", "activismo"], 
		  "Technology" : ["Informatica", "ingenieria", "tecnologia", "Nanotecnologia", "Tech"], 
		  "Health" : ["Alimentacion", "Medicina", "Salud", "sano", "fitness", "gym", "nutricion", "ejercicio", "higiene", "energia"]}

for u in users:
    tweets = users[u]
    hashtags = []
    c = 0
    for t in tweets:
        str = find_between( t.text, "#", " " )
        if str != "" :
            for sw in stopwords:
                if str.find(sw) >= 0:
                    str.replace(sw, "")
            hashtags.append(str);

    print "\n\nUsuario: ", u
    #print hashtags
    print "Numero de tweets: ", len(tweets)
    print "Numero de hashtags encontrados: ", len(hashtags)

    hashtags_set = list(set(hashtags))
    for h_s in hashtags_set:
        repeat = 0
        for h in hashtags:
            if h_s == h :
                repeat = repeat + 1
        if repeat > 1:
            frecuency[h_s] = repeat

    for topic in topics:
        fr_kw = 0
        print "Analisis para: ", topic
        keywords = topics[topic]
        for kw in keywords:
            for fr in frecuency:
                if fr.find(kw) >= 0:
                    fr_kw = fr_kw + frecuency[fr]
        print "Hashtags relativos al tema: ", fr_kw
        p = float(fr_kw) / len(tweets)
        print "Probabilidad: %.5f" %p


print "\n\nNumero de usarios: ",len(users)