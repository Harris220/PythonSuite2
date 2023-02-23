import requests
import csv
from bs4 import BeautifulSoup

class McTrades:
    def __init__(self):
        self.baseUrl = "https://mctrades.org/"
        self.uri = "forums/alts/page-"
        self.urls = []
        self.fiches = []
    
    def addBaseUrl(self,links):
        for link in links:
            self.urls.append({'link':self.baseUrl+link})
    
    def swoup(self,url,process):
        if isinstance(url,(int)):
            response = requests.get(self.baseUrl + self.uri + str(url))
        else:
            response = requests.get(url)
        
        if response.ok:
            soup = BeautifulSoup(response.text,'html.parser')
            try:
                return process(soup)
            except Exception:
                print("Erreur cant process soup")
                return False
        else:
            print("Failed to connect")
            return False
    
    def getEndpoints(self,soup):
        links = []
        aa = soup.findAll('a',{'class':'PreviewTooltip'})
        for a in aa:
            try: 
                    links.append(a['href'])
            except:
                pass
        return links
        
    def getLinks(self):
        for i in range(0,int(input("nombre de pages à traiter : "))):					    			
        	self.addBaseUrl(self.swoup(i,self.getEndpoints))
    
    def getInfoByPage(self,soup):  
        fiches = []
        divs = soup.findAll('div', {'class':'uix_userTextInner'})
        i = 0
        for div in divs:
            a = div.find('a',{'class':'username'})
            span = a.find('span')
            div2 = soup.find('div', {'class':'media__body'})
            h = div2.find('h1')
            span4 = h.find('span')
            span2 = soup.find('span',{'class':'DateTime'})
            if span2 is None:
                abbr = soup.find('abbr',{'class':'DateTime'})
                date = abbr.text
            else:
                date = span2.text
            span3 = soup.find('span',{'class':'dark_postrating_positive'})
            if span is not None:
                fiche = {
                    "name": span.text,
                    "title": h.text.strip(),
                    "date": date,
                    "rating":span3.text,
                    "type":span4.text
                }
            else:
                fiche = {
                    "name": a.text,
                    "title": h.text.strip(),
                    "date" : date,
                    "rating":span3.text,
                    "type":span4.text
                }
            fiches.append(fiche)
            return fiches
            
    def writeLinks(self):
        with open('links.csv', "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["link"])
            writer.writeheader()
            for url in self.urls:
                writer.writerow(url)
    
    def readLinks(self): 
        with open("links.csv", 'r', encoding="UTF8") as f:
            reader = csv.DictReader(f, delimiter= '\n')
            for row in reader:
                print(row["link"])	 		
                self.fiches.extend(self.swoup(row["link"],self.getInfoByPage))
        
            
    def writeOffers(self):
        with open('Offres.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["name","title","date","rating","type"])
            writer.writeheader()
            writer.writerows(self.fiches)
 
        