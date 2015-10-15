import pickle

users = pickle.load (open ("usersWithTweetsFlor.p","rb"))
es una lista

#this function returns the values of hashtag
def find_between( s, first, last ):
    try:
        #find the hashtag
		# in this case len always could be 1, cause is the len of symbol # to start after 
		start = s.index( first ) + len( first )
        #read after of hashtag until the end
		end = s.index( last, start )
        return s[start:end]
    except ValueError:
		return ""


#dictionary
frecuency = {}


for u in users:
    #list
	tweets = users[u]
    hashtags = []
	
    for t in tweets:
        str = find_between( t.text, "#", " " )
        #if hash has value
		if str != "" :
            #save in hashtags
			hashtags.append(str);
			

    #save only the unique values
	hashtags_set = list(set(hashtags))
    for h_s in hashtags_set:
        repeat = 0
        for h in hashtags:
            if ¨h_s == h :
                repeat = repeat + 1
        if repeat > 1:
            frecuency[h_s] = repeat

#sort the outcome 
for w in sorted(frecuency, key=frecuency.get, reverse=True):
    print w, frecuency[w]

print "\n"
print "Numero de usarios: ",len(users)
print "Numero de tweets analizados: ", len(tweets)
print "Numero de hashtags encontrados: ", len(hashtags)
	
