# "name": "GaymersPack",
#     "version_number": "1.2.0",
#     "website_url": "https://github.com/alexporter7/gaymers-repo-pack",
#     "description": 

import json
import os
import zipfile

NAME = "GaymersPack"
WEBSITE = "https://github.com/alexporter7/gaymers-repo-pack"
DESCRIPTION = "Modpack made to play with some friends"

PACK_FILES = ["manifest.json", "README.md", "CHANGELOG.md", "icon.png"]

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


def createZipFile():
    packZip = zipfile.ZipFile(NAME + ".zip", 'w')
    for packFile in PACK_FILES:
        if os.path.exists(packFile):
            packZip.write(packFile, os.path.basename(packFile))
        else:
            print(f"File not found: {packFile}")


releaseManifest["version_number"] = input("Release Version> ")
parseDependencies()
exportManifest()
createZipFile()

