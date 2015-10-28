import pickle
import operator
import json
import random
import tweepy

users = pickle.load (open ("usersWithTweetsFlor.p","rb"))


class TwitterAPI:
     def __init__(self):

        consumer_key = "JFH6uEhcZ95ZKkbbIv4gGeiYy"
        consumer_secret = "wTdFmDtNEIVS0Myq746tL87OqN0QacxwAbMvQzmn0JVxvVS8Ec"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "3317294695-8aWgP3ZY3CUhW71TleLmvv1g5GEbVsf0YZAhH0c"
        access_token_secret = "g4VG5r3PJMmBthLf0N4ngr2NwvsV44ckXprKDBeYpTYJd"
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)




     def nFollowers(self, ID):
        user = self.api.get_user(ID)
        nFollows = user.followers_count
        return  nFollows


     def getFolllowers(self,users): #returns a dictinary containing the users that have more followers (over the average)
        topFollowed = {}
        #For each user get the number of followers
        for u in users:
            key=str(self.nFollowers(u))
            topFollowed[str(u)] = key
        return topFollowed

     def commonWords(self, words):
        #Gets the top words of the tweets of each user
        wordCounter = {}
        counted = []
        for word in words:
            if word not in counted:
                wordCounter[words.count(word)] = word
                counted.append(word)
        topTenWords = sorted(wordCounter.values(),reverse=True)[0:9]
        return topTenWords

     def deleteSW(self, tweets):
        #Deletes the stopwords
        formatedTweets = []
        splitTweets = []
        for tweet in tweets:
             words = tweet.split()
             for word in words:
                 splitTweets.append(word)
        stopwords = ["1","2","3","4","5","6","7","8","9","10",":",";",".","!","#","@","un","de","no","se","me","a","al","que","han","y", "una", "unas", "unos", "uno", "sobre", "todo", "tambien", "tras", "otro", "algun", "alguno","alguna", "algunos", "algunas", "ser", "es", "soy", "eres", "somos", "sois", "estoy", "esta", "estamos", "estais", "estan", "como", "en", "para", "atras", "porque", "por que", "estado", "estaba", "ante", "antes", "siendo", "ambos", "pero", "por", "poder", "puede", "puedo", "podemos", "podeis", "pueden", "fui", "fue", "fuimos", "fueron", "hacer", "hago", "hace", "hacemos", "haceis", "hacen", "cada", "fin", "incluso", "primero", "desde", "conseguir", "consigo", "consigue", "consigues", "conseguimos", "consiguen", "ir", "voy", "va", "vamos", "vais", "van", "vaya", "gueno", "ha", "tener", "tengo", "tiene", "tenemos", "teneis", "tienen", "el", "la", "lo", "las", "los", "su", "aqui", "mio", "tuyo", "ellos", "ellas", "nos", "nosotros", "vosotros", "vosotras", "si", "dentro", "solo", "solamente", "saber", "sabes", "sabe", "sabemos", "sabeis", "saben", "ultimo", "largo", "bastante", "haces", "muchos", "aquellos", "aquellas", "sus", "entonces", "tiempo", "verdad", "verdadero", "verdadera", "cierto", "ciertos", "cierta", "ciertas", "intentar", "intento", "intenta", "intentas", "intentamos", "intentais", "intentan", "dos", "bajo", "arriba", "encima", "usar", "uso", "usas", "usa", "usamos", "usais", "usan", "emplear", "empleo", "empleas", "emplean", "ampleamos", "empleais", "valor", "muy", "era", "eras", "eramos", "eran", "modo", "bien", "cual", "cuando", "donde", "mientras", "quien", "con", "entre", "sin", "trabajo", "trabajar", "trabajas", "trabaja", "trabajamos", "trabajais", "trabajan", "podria", "podrias", "podriamos", "podrian", "podriais", "yo", "aquel"]
        for word in splitTweets:
            if word.lower() not in stopwords:
                formatedTweets.append(word)
        return formatedTweets

     def getTweets(self, userID):
        file_name = "alltweets_%s.p"%userID
        tweets = []
        statuses = pickle.load(open(file_name, "rb"))
        for status in statuses:
            if status is not None:
                stat = status.text
                tweets.append(stat);
        return tweets

class read_stream:
     # Read the stream from the files with the twitter data
     users = pickle.load(open("usersWithTweetsFlor.p", "rb"))
     print ("The top-ten word from your users :")
     twitter = TwitterAPI()
     Followers = twitter.getFolllowers(users)
     print("Printing values")
     max = 0
     valor = []
     for key, valuex in Followers.items() :
         print(key, valuex)
         value = int(valuex)
         valor.append(value)
         if value >= max:
            max = value
     print("Valor")
     print(valor)
     print("Max Value")
     print(max)

     def topWords(self):

         data = {}
         for user in self.Followers:
            #print user + " with " +str(topFollowed[user]) + " followers "
            #print "             " + str(twitter.getRetweetCount(user)) + " retweets."
            #print "             " + str(twitter.getFavCount(user)) + " favourites "
            #print (user)
            topTenWords = self.twitter.commonWords(self.twitter.deleteSW(self.twitter.getTweets(user)))
            #print ("     " + str(topTenWords))
            #print ( "    " + str(Followers[user]))
            data[user] = { "Socialinfluence" : self.Followers[user] , "topTen" : topTenWords }

         print("data")
         #First dictionary that needs to be merged
         #print(data)

         with open('topTenWords.json', 'w') as f:
            json.dump(data,f)
         return data



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
        #Looks for hashtags in tweets of users
        for t in tweets:
            str = find_between( t.text, "#", " " )
            str=str.lower()
            if str != "" :
                for sw in stopwords:
                    if str.find(sw) >= 0:
                        str.replace(sw, "")
                hashtags.append(str);

        #print ("\n\nUsuario: ", u)

        #print ("Numero de tweets: ", len(tweets))
        #print ("Numero de hashtags encontrados: ", len(hashtags))
        #print (hashtags)

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
            #print ("Analisis para: ", topic)
            keywords = topics[topic]
            #print("Keywords")
            #print(keywords)
            for kw in keywords:
                for fr in frecuency:
                    if fr.find(kw) >= 0:
                        fr_kw = fr_kw + frecuency[fr]
            #print ("Hashtags relativos al tema: ", fr_kw)
            #p = float(fr_kw) / len(tweets)
            p=float(fr_kw)
            biggestFrequencyTopic.setdefault(topic,0)
            if p>biggestFrequencyTopic[topic]:
                 biggestFrequencyTopic[topic]=p

        #    print ("Probabilidad: %.5f" %p)
            usersVectors[u][topic]=p


    print ("\n\nNumero de usarios: ",len(users))
    for topic in  biggestFrequencyTopic:
        valueTopic=biggestFrequencyTopic[topic]
        for u in usersVectors:

            valueUserTopic=usersVectors[u][topic]
            if not valueTopic==0:
                valueUserTopic=float(float(valueUserTopic)/float(valueTopic))
            usersVectors[u][topic]=valueUserTopic


        #print "Topic:"+topic
        #print biggestFrequencyTopic[topic]

    return usersVectors


#------------------------------------------------------------------------------------------#


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
        usersVectorsClean[u][topicInfluence]=0


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


    #with open('clustersColaborators.json', 'w') as outfile:
    #    json.dump(clusters, outfile)


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

    return clusters


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
vectores=getClustersParticipants(userCategoriesUnited)


datos = read_stream()

datos_r = datos.topWords()
print(datos_r)

print("imprimiendo ranking")
maxi=0
for key in datos_r:
    datos_r[key]["Socialinfluence"]=float(datos_r[key]["Socialinfluence"])
    print(datos_r[key]["Socialinfluence"])
    if datos_r[key]["Socialinfluence"] >= maxi:
        maxi = datos_r[key]["Socialinfluence"]

print("Mi valor maximo final")
print(maxi)
        #print "NO found!"+u
    #else:
    #    print "not found:"+u
    #print u
    #userCategoriesUnited[u]
   # tema=usersVectorsClean[u]
   # for t in tema:
    #    print t+","+str(tema[t])
print("imprimiendo comparacion")
#for topic,u in datos_r.iteritems():
    #print("imprimiendo topics")
    #print(datos_r[topic])
print("vectores")
print(vectores)

for majorkey, subdict in datos_r.iteritems():
    print("mayor key")
    print (majorkey)
    for subkey, value in subdict.iteritems():
            print("subkey")
            #print (subkey, value)
            print(datos_r[majorkey]['Socialinfluence'])
    for majorkeyv, subdictv in vectores.iteritems():
        #print("printing value of v")
        #print(majorkeyv)
        for subkeyv, valuev in subdictv.iteritems():
            print("subkey user value of v social")
            print (subkeyv)

            for subsubkeyv, subvaluev in valuev.iteritems():
                #print("subkey value of v social")
                #print (subsubkeyv)
                if subsubkeyv == "topicsUserFinal":
                    #print("holAAAAAAAAAAAAAAAAAAAAa")
                    #print(valuev["topicsUserFinal"])
                    for subsubsubkeyv, subsubvaluev in subvaluev.iteritems():
                        #print("subkey value of getting social")
                        #print (subsubsubkeyv)
                        if subsubsubkeyv == "Socialinfluence":
                            print("social influence")
                            print(subsubsubkeyv,subsubvaluev)
                            print(subvaluev["Socialinfluence"])
                            print("mayor key first array")
                            print (majorkey)
                #print(subvaluev)
                #print(valuev[subsubkeyv]['topicsUserFinal'])
                        if majorkey == subkeyv:
                            print("Son iguales")
                            print(majorkey)
                            print(datos_r[majorkey]['Socialinfluence'])
                            datos_r[majorkey]['Socialinfluence'] = float(datos_r[majorkey]['Socialinfluence'])
                            print(type(datos_r[majorkey]['Socialinfluence']))
                            print(subkeyv)
                            print(subvaluev["Socialinfluence"])
                            subvaluev["Socialinfluence"] = float(subvaluev["Socialinfluence"])
                            print(type(subvaluev["Socialinfluence"]))
                            subvaluev["Socialinfluence"] = datos_r[majorkey]['Socialinfluence']/maxi
                            print(subvaluev["Socialinfluence"])
                            #print(u)
                            #print(datos_r[u]["Socialinfluence"])

                            #datos_r[u]["Socialinfluence"] = float(datos_r[u]["Socialinfluence"])
                            #print(type(datos_r[u]['ranking']))
                            #print("imprimiendo comparacion2")
                            #print(v)
                            #print(vectores[v]["Socialinfluence"])
                            #print(type(vectores[v]['ranking']))
                            #vectores[v]["Socialinfluence"] = (datos_r[u]["Socialinfluence"])/float(maxi)
                            #print("el ranking original")
                            #print(datos_r[u]["Socialinfluence"])
                            #print("el maxi ranking")
                            #print(float(maxi))
                            #print(type(vectores[v]['ranking']))
                            #print("nuevo ranking ya normalizado")
                            #print(vectores[v]["Socialinfluence"])

print("imprimiendo vectores final")
#print(vectores)

with open('clustersColaborators.json', 'w') as outfile:
       json.dump(vectores, outfile)