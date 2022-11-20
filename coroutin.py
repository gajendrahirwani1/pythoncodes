def searcher():
    import time
    #some 4 sec time consuming task
    book = "this is a book on Gajendra Hirwani and code by Gajendra Hirwani"
    time.sleep(4)

    while True:
        text = (yield )
        if text in book:
            print("your text is in the book")
        else:
            print("Text is not in the book ")

search = searcher()
print("search started")
next(search)
print("next method run")
search.send("Gajendra")
search.close()                                              #this is used to close file
search.send("Hirwani")                                      #this line is not run becouse of close
