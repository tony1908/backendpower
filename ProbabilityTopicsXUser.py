import pickle
import operator
import json
import random

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
    biggestFrequencyTopic={}
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
            #p = float(fr_kw) / len(tweets)
            p=float(fr_kw)
            biggestFrequencyTopic.setdefault(topic,0)
            if p>biggestFrequencyTopic[topic]:
                 biggestFrequencyTopic[topic]=p

            print "Probabilidad: %.5f" %p
            usersVectors[u][topic]=p


    print "\n\nNumero de usarios: ",len(users)
    for topic in  biggestFrequencyTopic:
        valueTopic=biggestFrequencyTopic[topic]
        for u in usersVectors:

            valueUserTopic=usersVectors[u][topic]
            if not valueTopic==0:
                valueUserTopic=float(float(valueUserTopic)/float(valueTopic))
            usersVectors[u][topic]=valueUserTopic
    usersVectorsClean=usersVectors
    for u in usersVectors:
        topicInfluence="Socialinfluence"
        randomInt=random.randint(0,10)
        randomInt=randomInt*.1
        print randomInt
        usersVectorsClean[u][topicInfluence]=randomInt


        #print "Topic:"+topic
        #print biggestFrequencyTopic[topic]
    return usersVectors,usersVectorsClean



#x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

def getClustersParticipants(userCategoriesUnitedClean):

    valueUserTopic,usersVectorsClean=findVectorsUsers()
    clusters={}
    for u in valueUserTopic:
        print "User:"+u
        topics=valueUserTopic[u]
        sorted_topics = sorted(topics.items(), key=operator.itemgetter(1),reverse=True)
        biggestTopicUserValue=0
        biggestTopicUser="None"

        for t,v in sorted_topics:
            if not "Socialinfluence" in t:
               
                if float(v)>biggestTopicUserValue:
                    biggestTopicUserValue=v
                    biggestTopicUser=t
                if float(v)==biggestTopicUserValue:
                    if v>0:
                        if not t=="Technology":
                            biggestTopicUserValue=v
                            biggestTopicUser=t

                print "topic:"+t +","+str(v)
                print "BIGGEST:"+biggestTopicUser+","+str(biggestTopicUserValue)
            
        print
        print "BIGGEST:"+biggestTopicUser+","+str(biggestTopicUserValue)
        print
        clusters.setdefault(biggestTopicUser,{})
        topicsClean=valueUserTopic[u]
        clusters[biggestTopicUser][u]={}
        clusters[biggestTopicUser][u]["topicsUserFinal"]=topicsClean
        clusters[biggestTopicUser][u]["contributionsUserFinal"]=userCategoriesUnitedClean[u]


                #print t +","+str(v)
            #    clusters.setdefault(t,{})
            #    topicsClean=valueUserTopic[u]
            #    clusters[t][u]={}
            #    clusters[t][u]["topicsUserFinal"]=topicsClean
                #if not u in userCategoriesUnitedClean:
                #    print "not found:"+u
                #else:
                #    print "foun"
            #    clusters[t][u]["contributionsUserFinal"]=userCategoriesUnitedClean[u]
            
                #userCategoriesUnitedClean
            #    break
    #print 
    #print


    with open('clustersColaborators.json', 'w') as outfile:
        json.dump(clusters, outfile)

    for c in clusters:
        print "Cluster:"+c
    #    people=clusters[c]
        print "Cluster:"+c+","+str(len(clusters[c]))
        people=clusters[c]
        for p in people:
            print "people:"+p
            temas=people[p]["topicsUserFinal"]
            contribuciones=people[p]["contributionsUserFinal"]["contribuitions"]
            tipo=people[p]["contributionsUserFinal"]["typeOfContribuitor"]
            print tipo

           # Category:topicsUserFinal
#Politics
#Socialinfluence
#Technology
#Feminism
#Health
#Category:contributionsUserFinal
#contribuitions
#typeOfContribuitor
    #        print 
            #categorias=people[p]
            #for c in categorias:
            #    print "Category:"+c
            #    detalles=categorias[c]
            #    for d in detalles:
            #        print d

    #        print

    #    print

    topics = {"Politics" : ["impunidad", "aristegui", "bronco", "gobierno",  "autonomia", "autoridad", "ayotzinapa", "2deoctubre", "justicia"], 
          "Feminism" : ["feminicidios", "genero", "feminismo", "feminista", "mujer", "revolucion", "dignidad", "igualdad", "activismo"], 
          "Technology" : ["informatica", "ingenieria", "tecnologia", "nanotecnologia", "tech"], 
          "Health" : ["alimentacion", "medicina", "salud", "sano", "fitness", "gym", "nutricion", "ejercicio", "higiene", "energia"]}

    #for t in topics:
     #   print t
      #  words=topics[t]
       # for w in words:
        #    print w
    with open('topics.json', 'w') as outfile:
        json.dump(topics, outfile)


def getUsersCategories():
    categorizedUsers = pickle.load (open ("categorizedContribuitores_Mujeres__Fem.p","rb"))
    userCategoriesUnited={}
    for bot in categorizedUsers:
        print bot
        users=categorizedUsers[bot]
        for u in users:
            userCategoriesUnited[u]={}
            userCategoriesUnited[u]["typeOfContribuitor"]=bot
            userCategoriesUnited[u]["contribuitions"]=users[u]
    for u in userCategoriesUnited:
        print u
        print "type:"+userCategoriesUnited[u]["typeOfContribuitor"]
        tweets=userCategoriesUnited[u]["contribuitions"]
        for t in tweets:
            print t
    return userCategoriesUnited



        #    print u
            #+","+str(users[u])

    #categorizedContribuitores_Mujeres__Fem.p
userCategoriesUnited=getUsersCategories()
userCategoriesUnitedClean={}
#
valueUserTopic,usersVectorsClean=findVectorsUsers()
for u in usersVectorsClean:
    if not u in userCategoriesUnited:
        userCategoriesUnited[u]={}
        userCategoriesUnited[u]["typeOfContribuitor"]="None"
        userCategoriesUnited[u]["contribuitions"]="None"

        #userCategoriesUnitedClean[u]=userCategoriesUnited[u]
getClustersParticipants(userCategoriesUnited)


        #print "NO found!"+u
    #else:
    #    print "not found:"+u
    #print u
    #userCategoriesUnited[u]
   # tema=usersVectorsClean[u]
   # for t in tema:
    #    print t+","+str(tema[t])