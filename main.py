from sillynamegenerator.sillynamegenerator import *


def main():
    # Example usage:
    silly_name_gen = PoopypantsSillyNameGenerator()

    # collect normal name
    firstname = "Dav"
    lastname = "Pilkey"

    # Perform patented lookups to generate silly name
    sillyname = silly_name_gen.lookup(firstname, lastname)
    print(f"{firstname} {lastname}'s silly name is {sillyname}")
    # Laugh hysterically

if __name__ == "__main__":
    main()
