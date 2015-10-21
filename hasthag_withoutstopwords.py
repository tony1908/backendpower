import pickle

users = pickle.load (open ("usersWithTweetsFlor.p","rb"))


#this function returns the values of hashtag
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

		
#dictionary
frecuency = {}

stopwords = ["un", "una", "unas", "unos", "uno", "sobre", "todo", "tambien", "tras", "otro", "algun", "alguno", "alguna", "algunos", "algunas", "ser", "es", "soy", "eres", "somos", "sois", "estoy", "esta", "estamos", "estais", "estan", "como", "en", "para", "atras", "porque", "por que", "estado", "estaba", "ante", "antes", "siendo", "ambos", "pero", "por", "poder", "puede", "puedo", "podemos", "podeis", "pueden", "fui", "fue", "fuimos", "fueron", "hacer", "hago", "hace", "hacemos", "haceis", "hacen", "cada", "fin", "incluso", "primero", "desde", "conseguir", "consigo", "consigue", "consigues", "conseguimos", "consiguen", "ir", "voy", "va", "vamos", "vais", "van", "vaya", "gueno", "ha", "tener", "tengo", "tiene", "tenemos", "teneis", "tienen", "el", "la", "lo", "las", "los", "su", "aqui", "mio", "tuyo", "ellos", "ellas", "nos", "nosotros", "vosotros", "vosotras", "si", "dentro", "solo", "solamente", "saber", "sabes", "sabe", "sabemos", "sabeis", "saben", "ultimo", "largo", "bastante", "haces", "muchos", "aquellos", "aquellas", "sus", "entonces", "tiempo", "verdad", "verdadero", "verdadera", "cierto", "ciertos", "cierta", "ciertas", "intentar", "intento", "intenta", "intentas", "intentamos", "intentais", "intentan", "dos", "bajo", "arriba", "encima", "usar", "uso", "usas", "usa", "usamos", "usais", "usan", "emplear", "empleo", "empleas", "emplean", "ampleamos", "empleais", "valor", "muy", "era", "eras", "eramos", "eran", "modo", "bien", "cual", "cuando", "donde", "mientras", "quien", "con", "entre", "sin", "trabajo", "trabajar", "trabajas", "trabaja", "trabajamos", "trabajais", "trabajan", "podria", "podrias", "podriamos", "podrian", "podriais", "yo", "aquel"]

for u in users:
    tweets = users[u]
    hashtags = []
    for t in tweets:
        str = find_between( t.text, "#", " " )
        #if hash has value
		if str != "" :
            hashtags.append(str);

	#save only the unique values
    hashtags_set = list(set(hashtags))
    for h_s in hashtags_set:
        repeat = 0
        for h in hashtags:
            if h_s == h :
                repeat = repeat + 1
        if repeat > 1:
            frecuency[h_s] = repeat
			
#sort and eliminate replace stopwords
for w in sorted(frecuency, key=frecuency.get, reverse=False):
    c = 0
    for sw in stopwords:
        hts = w
        if hts.find(sw):
            c = c + 1
            hts.replace(sw, "")
    print hts, frecuency[w]

print "\n"
print "Numero de usarios: ",len(users)
print "Numero de tweets analizados: ", len(tweets)
print "Numero de hashtags encontrados: ", len(hashtags)
print "Numero de stopwords eliminadas: ", c