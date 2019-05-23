#My implementation of the stable marriage problem
from itertools import permutations


def isStable(matches, pref_men, pref_women, n):
    #print "New Perm"
    #print matches
    flag = True
    higher_pref_men = {} #a dict in which key will be name of man and value will be a list containing higher preferences of that man
    higher_pref_women = {}
    for man in matches:
        matched_woman = matches[man]
        higher_pref_of_this_man = (pref_men[man])[ : (pref_men[man]).index(matched_woman)] # do list slicing of the list containing prefernces of man upto and excluding the matched woman
        higher_pref_men[man] = higher_pref_of_this_man
        
    inv_matches = {v: k for k, v in matches.iteritems()} #swap keys and values. Refer Stackoverflow
    for woman in inv_matches:
        matched_man = inv_matches[woman]
        higher_pref_of_this_woman = (pref_women[woman])[ : (pref_women[woman]).index(matched_man)]
        higher_pref_women[woman] = higher_pref_of_this_woman

    #print higher_pref_men, higher_pref_women
    #In higher_pref_men array, iterate through each woman and check if that man appears in the array higher_pref_women for that particular woman.
    #If yes, then the marriage is unstable because these two characters would want to elope
    for man in higher_pref_men:
        for woman in higher_pref_men[man]:
            if man in higher_pref_women[woman]:
                return False          
        
    return flag


print 'Enter number of couples possible'
n = int(raw_input())
#We'll create a dictionary, wherein key will contain name of the person and value will be the list of prefernces for that particular person
pref_men = {}
pref_women = {}
men = []
women = []
matches = {}
print "One by one, enter the name of all men"
for i in range(n):
    men.append(raw_input())
    pref_men[men[i]] = []
for man in men:
    print "Enter preferences of %s from highest to lowest" %man
    pref_men[man] = raw_input().split()

print "One by one, enter the name of all women"
for i in range(n):
    women.append(raw_input())
    pref_women[women[i]] = []
for woman in women:
    print "Enter preferences of %s from highest to lowest" %woman
    pref_women[woman] = raw_input().split()
#These are sample test data in case you don't want to input values repeatedly to test
##men = ["M1", "M2", "M3"]
##women = ["W1", "W2", "W3"]
##pref_men = {"M1":["W2", "W3", "W1"], "M2":["W2", "W1", "W3"], "M3":["W1", "W2", "W3"]}
##pref_women = {"W1":["M1", "M2", "M3"], "W2":["M1", "M3", "M2"], "W3":["M3", "M2", "M1"]}
print "The Stable Matchig(s) are\nMAN\tWOMAN\n"
for perm in permutations(women):
    matches = dict(zip(men, perm))
    if(isStable(matches, pref_men, pref_women, n)):
        for key in matches:
            print key + " <<---->> " + matches[key]
        print "\n\n"



    

  
