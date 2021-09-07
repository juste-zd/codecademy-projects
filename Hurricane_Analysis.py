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

# Changed the numbering to match task numbering
# Most prints are commented out to not spam the terminal

# 2
# Update Recorded Damages
def damages_to_float(damages_list):
  conversion = {"M": 1000000,
              "B": 1000000000}
  updated_damages = []
  for record in damages_list:
    if record == "Damages not recorded":
      updated_damages.append(record)
      continue
    updated_damages.append(float(record[:-1]) * conversion[record[-1]])
  return updated_damages

# test function by updating damages
updated_damages = damages_to_float(damages)
# unquote to see updated_damages in a readable format:
"""
for entry in updated_damages:
  if isinstance(entry, float):
    print("{0:,}".format(entry))
  else:
    print(entry)
"""

# 3 
# Create and view the hurricanes dictionary
#   I decided to use global variables directly here, 
#   since I don't think this function will be used for anything else
def organize_hurricane_data():
  hurricane_data = {}
  for index in range(len(names)):
    hurricane_data[names[index]] = {'Name': names[index], 'Month': months[index], 'Year': years[index], 'Max Sustained Wind': max_sustained_winds[index], 'Areas Affected': areas_affected[index], 'Damage': updated_damages[index], 'Deaths': deaths[index]}
  return hurricane_data

hurricane_data = organize_hurricane_data()
# print(hurricane_data.items()) # <--test

# 4
# Organizing by Year
# create a new dictionary of hurricanes with year as key
def organize_hurricanes_by_year(hurricanes_dict):
  hurricanes_by_year = {}
  for entry in hurricanes_dict.values():
    if entry["Year"] in hurricanes_by_year:
      hurricanes_by_year[entry["Year"]].append(entry)
    else:
      hurricanes_by_year[entry["Year"]] = [entry]
  return hurricanes_by_year

hurricanes_by_year = organize_hurricanes_by_year(hurricane_data)
# print(hurricanes_by_year[1932]) # <--test

# 5
# Counting Damaged Areas
# create dictionary of areas to store the number of hurricanes that affected them

def count_hurricanes_by_area(hurricanes_dict):
  hurricane_count_by_area = {}
  for entry in hurricanes_dict.values():
    for area in entry["Areas Affected"]:
      if area in hurricane_count_by_area:
        hurricane_count_by_area[area] += 1
      else: 
        hurricane_count_by_area[area] = 1
  return hurricane_count_by_area

hurricane_count_by_area = count_hurricanes_by_area(hurricane_data)
# print(hurricane_count_by_area.items()) # <--test

# 6 
# Calculating Maximum Hurricane Count
# find most frequently affected area and the number of hurricanes involved in
def find_area_w_max_hurricanes(count_by_area_dict):
  max_num_hurricanes = 0
  for area, num_hurricanes in count_by_area_dict.items():
    if num_hurricanes > max_num_hurricanes:
      max_num_hurricanes = num_hurricanes
      max_area = area
  print("{area} is the most affected area, with a hurricane count of {number}".format(area = max_area, number = max_num_hurricanes))
  for area, num_hurricanes in count_by_area_dict.items():
    if num_hurricanes == max_num_hurricanes and not area == area:
      print("{area} is also one of the most affected, with a hurricane count of {number}".format(area = area, number = num_hurricanes))
  return max_area, max_num_hurricanes

max_area, max_num_hurricanes = find_area_w_max_hurricanes(hurricane_count_by_area) # <--test


# 7
# Calculating the Deadliest Hurricane
# find highest mortality hurricane and the number of deaths
def find_hurricane_w_max_deaths(hurricanes_dict):
  max_deaths = 0
  for entry in hurricanes_dict.values():
     if entry["Deaths"] > max_deaths:
      max_deaths = entry["Deaths"]
      deadliest_hurricane = entry["Name"]
  print("{hurricane} is the deadliest hurricane, with a death count of {number}".format(hurricane = deadliest_hurricane, number = max_deaths))
  for entry in hurricanes_dict.values():
     if entry["Deaths"] == max_deaths and not entry["Name"] == deadliest_hurricane:
      print("{hurricane} is also one of the deadliest hurricanes, with a death count of {number}".format(hurricane = entry["Name"], number = entry["Deaths"]))
  return deadliest_hurricane, max_deaths

deadliest_hurricane, max_deaths = find_hurricane_w_max_deaths(hurricane_data) # <--test

# 8
# Rating Hurricanes by Mortality
# categorize hurricanes in new dictionary with mortality severity as key
def rate_hurricanes_by_mortality(hurricanes_dict):
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  hurricanes_by_mortality = {}
  for entry in hurricanes_dict.values():
    rating = 0
    for index in range(5, 0, -1):
      if entry["Deaths"] > mortality_scale[index - 1]:
        rating = index
        break
    if rating in hurricanes_by_mortality:
      hurricanes_by_mortality[rating].append(entry)
    else:
      hurricanes_by_mortality[rating] = [entry]
  return hurricanes_by_mortality

hurricanes_by_mortality = rate_hurricanes_by_mortality(hurricane_data)
# print(hurricanes_by_mortality)  # <--test

# 9 Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost
def find_hurricane_w_max_damage(hurricanes_dict):
  max_damage = 0
  for entry in hurricanes_dict.values():
    if entry["Damage"] == "Damages not recorded":
      continue
    elif entry["Damage"] > max_damage:
      max_damage = entry["Damage"]
      most_damaging_hurricane = entry["Name"]
  print("{hurricane} is the hurricane with the highest damage, with a damage estimate of ${number: ,}".format(hurricane = most_damaging_hurricane, number = max_damage))
  for entry in hurricanes_dict.values():
     if entry["Damage"] == max_damage and not entry["Name"] == most_damaging_hurricane:
      print("{hurricane} is also one of the highest damage hurricanes, with a damage estimate of ${number: ,}".format(hurricane = entry["Name"], number = entry["Damage"]))
  return most_damaging_hurricane, max_damage

most_damaging_hurricane, max_damage = find_hurricane_w_max_damage(hurricane_data) # <--test

# 10
# Rating Hurricanes by Damage
# categorize hurricanes in new dictionary with damage severity as key
def rate_hurricanes_by_damage(hurricanes_dict):
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  hurricanes_by_damage = {}
  for entry in hurricanes_dict.values():
    if entry["Damage"] == "Damages not recorded":
      rating = "Damages not recorded"
    else:
      rating = 0
      for index in range(5, 0, -1):
        if entry["Damage"] > damage_scale[index - 1]:
          rating = index
          break
    if rating in hurricanes_by_damage:
      hurricanes_by_damage[rating].append(entry)
    else:
      hurricanes_by_damage[rating] = [entry]
  return hurricanes_by_damage

hurricanes_by_damage = rate_hurricanes_by_damage(hurricane_data)
# print(hurricanes_by_damage)  # <--test