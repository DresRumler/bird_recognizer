from bs4 import BeautifulSoup
import requests
import socket

def get_valid_urls():
    URL_1 = "https://www.gettyimages.dk/photos/pigeon?mediatype=photography&phrase=pigeon&sort=mostpopular"
    URL_2_99_START = "https://www.gettyimages.dk/photos/pigeon?mediatype=photography&page=" 
    URL_2_99_END = "&phrase=pigeon&sort=mostpopular"
    
    r = []
    r.append(URL_1)
    
    
    for i in range(2, 101):
        print("Working on url {}".format(i), end='\r')
        current_url = URL_2_99_START + str(i) + URL_2_99_END
        
        # TODO improve on this, it is technically not checking whether
        # the url it finds has images on it.
        try: 
            request = requests.get(current_url)
            r.append(current_url)
            
        except Exception:
            print("Couldn't open webpage {}".format(i))
        
    return r
    
def open_soup(URL):
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    return soup

def scrape_image_paths(soup):
    
    images = soup.find_all("img")
    
    r = []
    
    for i, image in enumerate(images):
        try:
            src = image["src"]
            
            if "media.gettyimages.com" in src: 
                r.append(src)
            
        except KeyError as e:
            
#             print("Failed on image {}".format(i))
    
    return r

if __name__=="__main__":
    all_image_urls = []

    for url in valid_urls: 
        soup = open_soup(URL)
        image_paths = scrape_image_paths(soup)
        
        all_urls.append(image_paths)

    for i, url_batch in enumerate(all_urls):
        for j, url in enumerate(url_batch):
            response = requests.get(url)
            
            file = open("../../../Pictures/pigeons/pigeon_{}{}.jpeg".format(i,j), "wb")
            file.write(response.content)
            file.close()
            
# valid_urls = get_valid_urls()


