"""
The format of the input file is as such

n NAME OF ADVOCATE
l LINK
p CLIENT NAME
p CLIENT NAME
el 
l LINK
p CLIENT NAME
el
en
n NAME

etc...

el is the closing tag for l, same with en and n

The output in website.txt will be an HTML table with the proper clients linked to
"""

def span(text):
    """
    Wraps text around formatting tag
    (That's how the web editor handles font sizes for some reason)
    """
    return '''<span style="font-size: 16px;">'''+text+"</span>"

def ahref(text,link):
    """
    Wraps text around an <a href=X> tag
    """
    return "<a href='"+link+"'>"+text+"</a>"

import sys
links = open("links.txt").read().splitlines()
linknumber = 0

sys.stdout = open('website.txt', 'w') # Saves HTML to text file


lobby = open("template.txt").read().splitlines() #Opens the "lobby" file with the info
number_of_lobbyists = 0

for line in lobby:
    #Counts number of lobbyists (they start with n)
    if line.startswith('n '):
        number_of_lobbyists+=1

lobby = iter(lobby) #Iterator of all the lines
print("<table border='1'>") #start table

#Title of table
print('''<tr><td style="text-align: center;">'''+'<b>'+span("Advocate Name")+'</b>'+'''</td>''')
print ('''<td style="text-align: center;">'''+'<b>'+span("Client Name")+'</b>'+"</td></tr>")
      
for i in range(number_of_lobbyists): #For each lobbyist
    print ("<tr><td>")
    print span(next(lobby)[2:]) #print their name
    print "</td><td>"
    linebreak = False
    br = ""
    print '''<ul style="line-height:1.4;">'''
    while True: #Before the 'en' tag
        link = next(lobby)
        if link.startswith("l "): #If it's a link (so not an endlink tag)
            if linebreak: 
                br=''
            
            
            while True:
                
                client = next(lobby)
                if client.startswith('p '): #If the next token isn't the el tag
                    print "<li>"                   
                    print span(ahref(br+client[2:],link[2:])) #list the user
                    # linebreak: print "<br />"
                    print "</li>"
                    linebreak = True
                    
                else: #If it is the el tag
                    #break out of the loop
                    #linebreak = False
                    #linknumber+=1
                    break
        else: #If it's the en tag
            print "</ul>"
            print ("</td></tr>") #end the row and break
            linebreak = False
            br=""
            break
print ("</table>") #After all the lobbyists end the table tag
sys.stdout = sys.__stdout__        
