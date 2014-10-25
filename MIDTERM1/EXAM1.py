def generateForm(story, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    story: a string containing sentences
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs

    For each word in story that is in one of the lists,
    * replace it with the string '[ADJ]' if the word is in listOfAdjs
    * replace it with the string '[VERB]' if the word is in listOfVerbs
    * replace it with the string '[NOUN]' if the word is in listOfNouns

    returns: string, A Mad-Libs form of the story. 
    """
    words = story.split()
    story = ''
    for i in range(len(words)):
        if words[i] in listOfAdjs:
            words[i] = '[ADJ]'
        elif words[i] in listOfNouns:
            words[i] = '[NOUN]'
        elif words[i] in listOfVerbs:
            words[i] = '[VERB]'

    for word in words:
        story += word
        story += ' '
    return story

def generateTemplates(madLibsForm):
    """ 
    madLibsForm: string, in a Mad-Lib form. See output of `generateForm`

    returns: a list of '[ADJ]', '[VERB]', and '[NOUN]' strings, in
    the order they appear in the madLibsForm.             
    """
    words = madLibsForm.split()
    print words
    res = []
    print len(words)
    for i in range(len(words)):
        print words[i]
        if words[i] == '[ADJ]' or words[i] == '[NOUN]' or words[i] == '[VERB]':
            res.append(words[i])
    return res

def verifyWord(userWord, madTemplate, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    userWord: a string, the word the user inputted
    madTemplate: string, the type of word the user was supposed to input
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs):

    returns: Boolean, whether or not the word is valid
    """
    if madTemplate == '[ADJ]':
        return userWord in listOfAdjs
    elif madTemplate == '[NOUN]':
        return userWord in listOfNouns
    elif madTemplate == '[VERB]':
        return userWord in listOfVerbs

def numPens(n):
    """
    n is a non-negative integer

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """
    if n < 5:
        return False
    elif n%5 == 0 or n%8 == 0:
        return True
    else:
        return numPens(n-8)
        
            
    
