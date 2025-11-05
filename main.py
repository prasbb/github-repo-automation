import argparse 

from utils import create_repository

def main(): 
    parser = argparse.ArgumentParser(description="Create GitHub repositories from the command line.")
    parser.add_argument("name", help="Repository name")
    parser.add_argument("-d", "--description", help="Repository description")
    parser.add_argument("--private", action="store_true", help="Sets repository to be private")
    args = parser.parse_args()
    create_repository(args.name, args.private, args.description)
