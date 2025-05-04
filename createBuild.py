# "name": "GaymersPack",
#     "version_number": "1.2.0",
#     "website_url": "https://github.com/alexporter7/gaymers-repo-pack",
#     "description": 

import json

NAME = "GaymersPack"
WEBSITE = "https://github.com/alexporter7/gaymers-repo-pack"
DESCRIPTION = "Modpack made to play with some friends"

releaseManifest = {
    "name": NAME,
    "version_number": "",
    "website_url": WEBSITE,
    "description": DESCRIPTION,
    "dependencies": []
}


def parseDependencies():
    depFile = open('dependencies', 'r').read()
    dependencies = depFile.split("\n")
    for dep in dependencies:
        releaseManifest["dependencies"].append(dep)


def exportManifest():
    manifestFile = open('manifest.json', 'w')
    manifestFile.write(json.dumps(releaseManifest))


releaseManifest["version_number"] = input("Release Version> ")
parseDependencies()
exportManifest()

