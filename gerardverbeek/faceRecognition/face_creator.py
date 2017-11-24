from PIL import Image
from os import listdir
from os.path import isfile, join

import face_recognition
import logging
import os
import uuid
import imghdr
import shutil


VALID_EXTENSIONS = ["jpg", "jpeg"]

def createFacesInFolder(folderPath):
    logging.info("Looking for images in: %s ", folderPath)
    # Create folder for the faces, inside the image folder.
    FACES_LOCATION = folderPath+"/faces"
    createFolder(FACES_LOCATION)
    filesInFolder = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]
    for file in filesInFolder:
        # Check if the file has the right extension
        if vaildateImage(folderPath+"/"+file):
            facesFromImage = getFacesFromImage(folderPath+"/"+file)
            # Save all the faces
            for face in facesFromImage:
                face.save(FACES_LOCATION+"/"+str(uuid.uuid4())+'.jpg', 'JPEG')


def getFacesFromImage(imageUri):
    image = face_recognition.load_image_file(imageUri)
    face_locations = face_recognition.face_locations(image)

    faces =[]
    for face_location in face_locations:
        top, right, bottom, left = face_location
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        faces.append(pil_image)
    logging.info("Found %s faces in image: %s", len(faces), imageUri)
    return faces

#
def vaildateImage(file):
    if os.path.isfile(file):
        extension = imghdr.what(file)
        if extension is not None:
            if any(extension in s for s in VALID_EXTENSIONS):
                return True

    logging.error("file: %s is not valid", file)
    return False


#
def createFolder(folderPath):
    try:
        if not os.path.exists(folderPath):
            os.makedirs(folderPath)
        else:
            shutil.rmtree(folderPath)
            os.makedirs(folderPath)
    except OSError:
        logging.error("Could not make folder: %s", folderPath)
        pass
