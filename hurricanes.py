# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

updated_damages = []
def updated_damages_function(damages):
  for damage in damages:
    if damage.startswith("D"):
      updated_damages.append(damage)
    else:
      if damage[-1] == "B":
        ndamage = damage[:-1]
        exact_damage = float(ndamage)
        exact_damage = exact_damage * 1000000000
        updated_damages.append(exact_damage)
      elif damage[-1] == "M":
        ndamage = damage[:-1]
        exact_damage = float(ndamage)
        exact_damage = exact_damage * 1000000
        updated_damages.append(exact_damage)
  return updated_damages

updated_damages_function(damages)
#print(updated_damages)

everything = list(zip(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths))
#print(everything)



def remake_dictionary(names, months, years, max_sustained_winds, areas_affected, updatedamage, deaths):
  hurricane_dictionary = {}
  dicts = {}
  for i in range(0, len(names)):
    key = names[i]
    value = {}
    value.update({"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": updated_damages[i], "Deaths": deaths[i]})
    hurricane_dictionary.update({key:value})
  return hurricane_dictionary
  for name in names:
    for x in hurricane_dictionary:
        dicts[name] = x
  return dicts

#print(remake_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths))
hurricanenames = (remake_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths))
#print(hurricanenames)

def hurricane_by_year(hurricanenames):
    hurricane_year = {}
    for cane in hurricanenames:
        current_year = hurricanenames[cane]['Year']
        current_cane = hurricanenames[cane]
        if current_year not in hurricanenames:
            hurricane_year[current_year] = [current_cane]
        else:
            hurricane_year[current_year].append(current_cane)
    return hurricane_year

hurricaneyears = hurricane_by_year(hurricanenames)
#print(hurricaneyears)

def countareas(areas_affected):
    areaCount = {}
    for manyplaces in areas_affected:
        for specific_area in manyplaces:
            if specific_area not in areaCount:
                areaCount[specific_area] = 1
            else:
                areaCount[specific_area] += 1
    return areaCount

dict_area_count = countareas(areas_affected)
#print(dict_area_count)

def most_hit(dict_area_count):
    max_area = "Central America"
    max_area_count = 0
    for area in dict_area_count:
        if max_area_count < dict_area_count[area]:
            max_area_count = dict_area_count[area]
            max_area = area 
    return max_area, max_area_count

most_hit_place = most_hit(dict_area_count)
#print(most_hit_place)

def most_deaths(hurricanenames):
    max_deaths = "Cuba I"
    max_death_count = 0
    for death in hurricanenames:
        if hurricanenames[death]["Deaths"] > max_death_count:
            max_deaths = death
            max_death_count = hurricanenames[death]["Deaths"] 
    return max_deaths, max_death_count

max_deaths, max_death_count = most_deaths(hurricanenames)
#print(max_deaths, max_death_count)

#print(hurricanenames.keys())

def hurricanes_mortality(hurricanenames):
    mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
    hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for death in hurricanenames:
        mortality = hurricanenames[death]["Deaths"]
        if mortality == mortality_scale[0]:
            hurricanes_by_mortality[0].append(hurricanenames[death])
        elif mortality > mortality_scale[0] and mortality <= mortality_scale[1]:
            hurricanes_by_mortality[1].append(hurricanenames[death])
        elif mortality > mortality_scale[1] and mortality <= mortality_scale[2]:
            hurricanes_by_mortality[2].append(hurricanenames[death])
        elif mortality > mortality_scale[2] and mortality <= mortality_scale[3]:
            hurricanes_by_mortality[3].append(hurricanenames[death])
        elif mortality > mortality_scale[3] and mortality <= mortality_scale[4]:
            hurricanes_by_mortality[4].append(hurricanenames[death])
        elif mortality > mortality_scale[4]:
            hurricanes_by_mortality[5].append(hurricanenames[death])
    return hurricanes_by_mortality

hurricanes_by_mortality = hurricanes_mortality(hurricanenames)
#print(hurricanes_by_mortality)

def biggestdamage(hurricanenames):
    biggestdamage = 0
    for somuchstuff in hurricanenames:
        for damage in somuchstuff:
            damage = hurricanenames[somuchstuff]['Damage']
            if hurricanenames[somuchstuff]['Damage'] == 'Damages not recorded':
                pass
            else:
                if damage > biggestdamage:
                    biggestdamage = damage
                    return hurricanenames[somuchstuff]["Name"], biggestdamage

bigdamage = biggestdamage(hurricanenames)
#print(bigdamage)

def hurricanes_damages(hurricanenames):
    damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
    hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for fuckmylife in hurricanenames:
        for damage in fuckmylife:
            damage = hurricanenames[fuckmylife]["Damage"]
            if hurricanenames[fuckmylife]['Damage'] == 'Damages not recorded':
                pass
            elif damage == damage_scale[0]:
                hurricanes_by_damage[0].append(hurricanenames[fuckmylife])
            elif damage > damage_scale[0] and damage <= damage_scale[1]:
                hurricanes_by_damage[1].append(hurricanenames[fuckmylife])
            elif damage > damage_scale[1] and damage <= damage_scale[2]:
                hurricanes_by_damage[2].append(hurricanenames[fuckmylife])
            elif damage > damage_scale[2] and damage <= damage_scale[3]:
                hurricanes_by_damage[3].append(hurricanenames[fuckmylife])
            elif damage > damage_scale[3] and damage <= damage_scale[4]:
                hurricanes_by_damage[4].append(hurricanenames[fuckmylife])
            elif damage > damage_scale[4]:
                hurricanes_by_damage[5].append(hurricanenames[fuckmylife])
    return hurricanes_by_damage

hurricanes_by_damages = hurricanes_damages(hurricanenames)
print(hurricanes_by_damages)