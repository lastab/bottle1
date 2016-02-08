import MySQLdb

def openDatabase():
    #open database connection
    db=MySQLdb.connect("localhost","batsal","a","wn_pro_mysql")
    return db;


def getGlossory(word):
    db=openDatabase()
    cursor=db.cursor()
    
    sqlQuery="""SELECT 
                    w.synset_id,
                    w.word,
                    w.ss_type, 
                    g.gloss,
                    (SELECT GROUP_CONCAT(w1.word) FROM wn_similar s,wn_synset w1 where s.synset_id_2=w1.synset_id and s.synset_id_1=w.synset_id) as 'Similar',
                    (SELECT GROUP_CONCAT(w1.word) FROM wn_antonym s,wn_synset w1 where s.synset_id_2=w1.synset_id and s.synset_id_1=w.synset_id) as 'Antonym',
                    (SELECT GROUP_CONCAT(w1.word) FROM wn_see_also s,wn_synset w1 where s.synset_id_2=w1.synset_id and s.synset_id_1=w.synset_id) as 'see also'
                FROM 
                    wn_synset w JOIN wn_gloss g on w.synset_id=g.synset_id  
                WHERE 
                    w.word='%s'
                ORDER BY w.ss_type""" % word.replace(" ","_")
    try:
        cursor.execute(sqlQuery)
        results=cursor.fetchall()
        wordMeanings=[]
        
        
        
        for row in results:
            wordMeaning=[]
            wordMeaning.append(row[0])
            wordMeaning.append ( row[2])
            wordMeaning.append ( row[3])
             
            wordMeaning.append ( row[4])
            wordMeaning.append ( row[5])
            wordMeaning.append ( row[6])
            wordMeanings.append(wordMeaning)
        db.close()
        
        return (wordMeanings);
    except:
        print "Error: unable to fetch data"
        db.close()
        return ;
    
    
    

'''wordMeanings=getGlossory('paper')
# Now print fetched result
print "%s :" % 'rock'

print " %s" % \
        (wordMeanings )
'''
      


'''
#for testing the  codes
db=openDatabase()
#prepare a cursor object using cursor() method
cursor=db.cursor()

#SQL query
sql= "SELECT w.word,g.gloss,w.ss_type from wn_synset w, wn_gloss g where w.synset_id=g.synset_id and w.word='test' "

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()

   print "%s :" % 'test'
   for row in results:
      word = row[0]
      gloss = row[1]
      wtype = row[2]
      # Now print fetched result
      print "(%s) %s" % \
             (wtype, gloss )
except:
   print "Error: unable to fecth data"
db=closeDatabase(db)
'''