import requests
import pypokedex

print("POKÉMON SPRITE DOWNLOADER")
initial = int(input("From (dex number): "))
final = int(input("To (dex number): "))

if(initial <= final):
    n = initial
    while(n <= final):
        if n < 10:
            s = '000' + str(n)
        elif n < 100:
            s = '00' + str(n)
        elif n < 1000:
            s = '0' + str(n)
        else:
            s = str(n)

        
        url = "https://projectpokemon.org/images/sprites-models/sv-sprites-home/" + s + ".png"
        r = requests.get(url)
        if(r.status_code != 404): 
            print("Downloading " + s + " (" + pypokedex.get(dex=n).name + ")")
            open(s + "-" + pypokedex.get(dex=n).name + ".png", 'wb').write(r.content)

        url = "https://projectpokemon.org/images/sprites-models/sv-sprites-home/" + s + "_01" + ".png"
        r = requests.get(url)
        if(r.status_code != 404):
            print("Downloading " + s + " (" + pypokedex.get(dex=n).name + ")")
            open(s + "_01" + "-"+ pypokedex.get(dex=n).name  + ".png", 'wb').write(r.content)
            m = 2
            while(requests.get(url).status_code != 404):
                url = "https://projectpokemon.org/images/sprites-models/sv-sprites-home/" + s + "_0" + str(m) + ".png"
                r = requests.get(url)
                if(r.status_code != 404): 
                    open(s + "_0" + str(m) + "-"+ pypokedex.get(dex=n).name  + ".png", 'wb').write(r.content)
                m = m + 1
        n = n+1
else:
    print("Yo wtf goofy ass")
print("Finished.")
