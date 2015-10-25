import tweepy
import pickle
import json

class TwitterAPI:
    def __init__(self):

        consumer_key = "JFH6uEhcZ95ZKkbbIv4gGeiYy"
        consumer_secret = "wTdFmDtNEIVS0Myq746tL87OqN0QacxwAbMvQzmn0JVxvVS8Ec"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "3317294695-8aWgP3ZY3CUhW71TleLmvv1g5GEbVsf0YZAhH0c"
        access_token_secret = "g4VG5r3PJMmBthLf0N4ngr2NwvsV44ckXprKDBeYpTYJd"
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)



    def deleteSW(self, tweets):
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



    def commonWords(self, words):
        wordCounter = {}
        counted = []
        for word in words:
            if word not in counted:
                wordCounter[words.count(word)] = word
                counted.append(word)
        topTenWords = sorted(wordCounter.values(),reverse=True)[0:9]
        return topTenWords

    def description(self,id):
        newText=[]
        user = self.api.get_user(id)
        info = user.description

        for word in info.split(' '):
            if word not in depure:
                newText += word+' '
                return newText[:-1]

    def nFollowers(self, ID):
        user = self.api.get_user(ID)
        nFollows = user.followers_count
        return  nFollows


    def getTopFolllowed(self, users): #returns a dictinary containing the users that have more followers (over the average)
        average = 0
        cont=0
        topFollowed = {}
        for u in users:
            key=str(self.nFollowers(u))
            topFollowed[str(u)] = key
            average+=int(key)
            cont+=1
        average=average/cont
        filterTop = {}
        for element in topFollowed:
            if int(topFollowed[element]) >= average:
                filterTop[element] = topFollowed[element]
        return filterTop

    def getRetweetCount(self, userID):
        file_name = "alltweets_%s.p"%userID
        count = 0
        states = []
        statuses = pickle.load(open(file_name, "rb"))
        for status in statuses:
            stat = status.id
            if stat is not None:
                count = count + status.retweet_count
        return count

    def getTweets(self, userID):
        file_name = "alltweets_%s.p"%userID
        tweets = []
        statuses = pickle.load(open(file_name, "rb"))
        for status in statuses:
            if status is not None:
                stat = status.text
                tweets.append(stat);
        return tweets

    def getFavCount(self, userID):
        user = self.api.get_user(userID)
        fav = user.favourites_count
        return fav


    #def specialize(self, userID):



if __name__ == "__main__":
    twitter = TwitterAPI()
    users = pickle.load(open("usersWithTweetsFlor.p", "rb"))
    print "The top-ten word from your users :"
    topFollowed = twitter.getTopFolllowed(users)
    count = 0
    data = {}
    for user in topFollowed:
        #print user + " with " +str(topFollowed[user]) + " followers "

        #print "             " + str(twitter.getRetweetCount(user)) + " retweets."

        #print "             " + str(twitter.getFavCount(user)) + " favourites "
        print user
        topTenWords = twitter.commonWords(twitter.deleteSW(twitter.getTweets(user)))
        print "     " + str(topTenWords)
        print  "    " + str(topFollowed[user])
        data[user] = { "ranking" : topFollowed[user] , "topTen" : topTenWords }


    with open('topTenWords.json', 'w') as f:
        json.dump(data,f)
