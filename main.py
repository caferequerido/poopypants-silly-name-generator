from sillynamegenerator.pp_silly_name_generator import *


def main():
    # Example usage:
    silly_name_gen = PoopypantsSillyNameGenerator()

    # Define keys to look up in each dictionary
    firstname = "Dav"
    lastname = "Pilkey"

    # Perform the lookups and get the results
    sillyname = silly_name_gen.lookup(firstname, lastname)
    print(f"{firstname} {lastname}'s silly name is {sillyname}")


if __name__ == "__main__":
    main()
