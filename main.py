import sys
import argparse
import logging

from gerardverbeek.faceRecognition import face_creator

parser = argparse.ArgumentParser()

parser.add_argument('path', type=str,
                    help='Path to image folder')

parser.add_argument(
    '--debug',
    help="Print lots of debugging statements",
    action="store_const", dest="loglevel", const=logging.DEBUG,
    default=logging.WARNING,
)
parser.add_argument(
    '--verbose',
    help="Be verbose",
    action="store_const", dest="loglevel", const=logging.INFO,
)


args = parser.parse_args()
logging.basicConfig(level=args.loglevel)


# Start
face_creator.createFacesInFolder(args.path)




