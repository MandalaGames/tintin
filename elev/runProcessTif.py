import processTif
import argparse
import sys

argparser = argparse.ArgumentParser(description="Process elevation data from a GeoTiff")

argparser.add_argument('--filename', help='Filename for the tiff file to process.')
argparser.add_argument('--outfile', help='Filename for the output csv and json files.')
argparser.add_argument('--scale', help='Scale factor of the output files.', type=int) # FIXME: explain
argparser.add_argument('--latitude', help='Max and min latitude to be processed.', nargs=2)
argparser.add_argument('--longitude', help='Max and min longitude to be processed.', nargs=2)
argparser.add_argument('--info', help='Print info about tiff.', action="store_true")

args = argparser.parse_args()

processTif.processElevData(args.filename, args.outfile, args.scale, args.info)
