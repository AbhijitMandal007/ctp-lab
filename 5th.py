class FreqCounter:
    def __init__(self,text):
        self.text=text

    def countChar(self):
        s={}
        for ch in self.text:
            if ch!=" ":
                s[ch]=s.get(ch,0)+1

        print(f"Frequency of characters in is : {s}")

    def countWordFreq(self):
        s={}
        words=self.text.split()
        for word in words:
            s[word]=s.get(word,0)+1

        print(f"Frequency of words is : {s}")
    def totalCharCount(self):
        count =0
        for ch in self.text:
            if ch!=" ":
                count=count+1

        print("Total no of characters : ",count)
sent=input("Enter a text string : ")
str=FreqCounter(sent)
str.countChar()
str.countWordFreq()
str.totalCharCount()


    