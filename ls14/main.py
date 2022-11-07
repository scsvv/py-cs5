class BanWord(Exception): 
    """
    """
    message : str = "Please, don't use banned word"

    def __init__(self, message=None):
        if message: 
            self.message = message
    
    def __str__(self):
        return self.message 


try: 
    
    banned_word = "cat"
    sentance = "cat is cat but isnt dog"
    sentance = sentance.split()

    if sentance.count(banned_word) != 0: 
        raise BanWord() 
except BanWord as e:
    print(e)

        