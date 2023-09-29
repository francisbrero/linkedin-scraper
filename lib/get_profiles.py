try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

# Create the output csv file and create headers
f = open('./data/connection_scrape.csv', 'w+')
f.write('"name", "title", "url" \n')

# Open file and parse
with open('./data/connections.html', 'rb') as file:
    soup = BeautifulSoup(file,"html.parser")

cnt = 0
err = 0

# Find all member DOM elements
elements = soup.find_all("div", class_="entity-result__item".split())
print("there are " + str(len(elements)) + " elements")

# Process them
for member in elements:
    # Get the name of the user
    name_el = member.find("div", class_="mb1")
    name_sp = name_el.find("span", attrs={"aria-hidden": "true"})
    name = name_sp.get_text()

    # Get the linkedin URL of the user
    url_el = name_el.find("a", class_="app-aware-link")
    url= url_el.get('href').split("?",1)[0]

    # Get the title of the user
    title_el = member.find("div", class_="entity-result__primary-subtitle t-14 t-black t-normal")
    title = title_el.get_text().strip()
	
	# Return results
    try:
        f.write('"' + name + '", "' + title + '", "' + url + '" \n')
        cnt =+1
    except:
        print("error with user " + name)
        err =+1
message = "inserted " + str(cnt) + " successfully records into the file, there were " + str(err) + " errors"
print(message)