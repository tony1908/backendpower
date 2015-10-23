import pickle
import operator
import json

users = pickle.load (open ("usersWithTweetsFlor.p","rb"))

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def findVectorsUsers():
    usersVectors={}
    frecuency = {}

    stopwords = ["un", "una", "unas", "unos", "uno", "sobre", "todo", "tambien", "tras", "otro", "algun", "alguno", "alguna", "algunos", "algunas", "ser", "es", "soy", "eres", "somos", "sois", "estoy", "esta", "estamos", "estais", "estan", "como", "en", "para", "atras", "porque", "por que", "estado", "estaba", "ante", "antes", "siendo", "ambos", "pero", "por", "poder", "puede", "puedo", "podemos", "podeis", "pueden", "fui", "fue", "fuimos", "fueron", "hacer", "hago", "hace", "hacemos", "haceis", "hacen", "cada", "fin", "incluso", "primero", "desde", "conseguir", "consigo", "consigue", "consigues", "conseguimos", "consiguen", "ir", "voy", "va", "vamos", "vais", "van", "vaya", "gueno", "ha", "tener", "tengo", "tiene", "tenemos", "teneis", "tienen", "el", "la", "lo", "las", "los", "su", "aqui", "mio", "tuyo", "ellos", "ellas", "nos", "nosotros", "vosotros", "vosotras", "si", "dentro", "solo", "solamente", "saber", "sabes", "sabe", "sabemos", "sabeis", "saben", "ultimo", "largo", "bastante", "haces", "muchos", "aquellos", "aquellas", "sus", "entonces", "tiempo", "verdad", "verdadero", "verdadera", "cierto", "ciertos", "cierta", "ciertas", "intentar", "intento", "intenta", "intentas", "intentamos", "intentais", "intentan", "dos", "bajo", "arriba", "encima", "usar", "uso", "usas", "usa", "usamos", "usais", "usan", "emplear", "empleo", "empleas", "emplean", "ampleamos", "empleais", "valor", "muy", "era", "eras", "eramos", "eran", "modo", "bien", "cual", "cuando", "donde", "mientras", "quien", "con", "entre", "sin", "trabajo", "trabajar", "trabajas", "trabaja", "trabajamos", "trabajais", "trabajan", "podria", "podrias", "podriamos", "podrian", "podriais", "yo", "aquel"]

    topics = {"Politics" : ["impunidad", "aristegui", "bronco", "gobierno",  "autonomia", "autoridad", "ayotzinapa", "2deoctubre", "justicia"], 
		  "Feminism" : ["feminicidios", "genero", "feminismo", "feminista", "mujer", "revolucion", "dignidad", "igualdad", "activismo"], 
		  "Technology" : ["informatica", "ingenieria", "tecnologia", "nanotecnologia", "tech"], 
		  "Health" : ["alimentacion", "medicina", "salud", "sano", "fitness", "gym", "nutricion", "ejercicio", "higiene", "energia"]}

    for u in users:
        usersVectors.setdefault(u,{})
        tweets = users[u]
        hashtags = []
        c = 0
        for t in tweets:
            str = find_between( t.text, "#", " " )
            str=str.lower()
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
            usersVectors[u][topic]=p


    print "\n\nNumero de usarios: ",len(users)
    return usersVectors



#x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

def getClustersParticipants():

    usersVectors=findVectorsUsers()
    clusters={}
    for u in usersVectors:
        print "User:"+u
        topics=usersVectors[u]
        sorted_topics = sorted(topics.items(), key=operator.itemgetter(1),reverse=True)
        for t,v in sorted_topics:
            print t +","+str(v)
            clusters.setdefault(t,{})
            clusters[t][u]=topics
            break
    print 
    print


    with open('clustersColaborators.json', 'w') as outfile:
        json.dump(clusters, outfile)

    for c in clusters:
    
        people=clusters[c]
        print "Cluster:"+c+","+str(len(clusters[c]))
        for p in people:
            print p
        print 

getClustersParticipants()