import requests
import json
import time

# -------------------------
# Jinja2
# -------------------------

from jinja2 import Environment, FileSystemLoader
template_dir = 'Templates/'
env = Environment(loader=FileSystemLoader(template_dir))
allDogs_template = env.get_template('allDogs.j2')

# -------------------------
# Headers
# -------------------------
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
}

# -------------------------
# All People
# -------------------------

dog_template = env.get_template('dog.j2')
dogs = requests.request("GET", "https://dog.ceo/api/breeds/list/all", headers=headers)
dogsJSON = dogs.json()
dogsList = dogsJSON['message']
subDogList = []
# -------------------------
# Single Dog
# -------------------------
for dog,value in dogsList.items():
    singleDog = dog
    subDog = value

# -------------------------
# Photos
# -------------------------
    dogPhotos = requests.request("GET", f"https://dog.ceo/api/breed/{ dog }/images", headers=headers)
    dogPhotosJSON = dogPhotos.json()
    dogsPhotoList = dogPhotosJSON['message']

# -------------------------
# Dog Template
# -------------------------

    parsed_all_output = dog_template.render(
        singleDog = singleDog,
        subDog = subDog,
        dogsPhotoList = dogsPhotoList,
        )

# -------------------------
# Save Dog File
# -------------------------

    with open(f"DogCEO/{ singleDog }.md", "w") as fh:
        fh.write(parsed_all_output)                
        fh.close()

# -------------------------
# All Dogs Template
# -------------------------

parsed_all_output = allDogs_template.render(
        dogsList = dogsList,
        photos = dogsPhotoList,
        dogsPhotoList = dogsPhotoList,
    )

# -------------------------
# Save Star Wars File
# -------------------------

with open("All Dogs.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()