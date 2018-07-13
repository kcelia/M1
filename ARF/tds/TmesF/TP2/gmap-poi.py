
import googlemaps as gmaps

APIKEY = "AIzaSyApwGnG4SariGsE0-mUDnLRQj6XJAcY2T8"

gm = gmaps.Client(APIKEY)

COORD = [(48.806,2.23),(48.916,2.48)]


DX = COORD[1][0]-COORD[0][0]
DY = COORD[1][1]-COORD[0][1]
TYPES = ["clothing_store", "bar","laundry","bakery", "lodging", "restaurant","cafe", "atm", "night_club","convenience_store","furniture_store","home_goods_store"]
cpt = 0

def get_list(typreq,totstep):
    res = dict()
    global cpt
    for i in range(totstep):
        for j in range(totstep):
            cpt+=1
            coord = (COORD[0][0]+i*DX*1./totstep,COORD[0][1]+j*DY*1./totstep)
            print(typreq,i,j,len(res),cpt)
            res.update([ (x['place_id'],(x['geometry']['location']['lat'],x['geometry']['location']['lng'])) for x in gm.places_radar(coord, 2000, type=typreq)['results']])
    return res

def treat_dic(d):
    global cpt
    for i,(k,v) in enumerate(d.items()):
        print(i,len(d),cpt)
        res=gm.place(k)['result']
        cpt+=1
        d[k]=(v,res.get('rating',-1),res.get('name',""),res.get('types',[]),res.get('price_level',-1))
    return d
res = dict()
for typreq in TYPES:
    res[typreq] = get_list(typreq,20)
    pickle.dump(res[typreq],open("res"+typreq+".pkl","wb"))

for typreq in TYPES:
    res[typreq]=treat_dic(res[typreq])
    pickle.dump(res[typreq],open("rescomplet"+typreq+".pkl","wb"))
pickle.dump(res,open("restotal.pkl","wb"))