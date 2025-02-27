from sillynamegenerator.sillynamegenerator import *


def print_poopy_name(firstname, lastname):
    silly_name_gen = PoopypantsSillyNameGenerator()

    print(f"{firstname} {lastname}'s silly name is {silly_name_gen.lookup(firstname, lastname)}")


def main():
    # Example usage:

    print_poopy_name('Dav', 'Pilkey')
    print_poopy_name('Lionel', 'Messi')
    print_poopy_name('Cristiano', 'Rolaldo')
    print_poopy_name('Albert', 'Einstein')

    # Laugh hysterically

if __name__ == "__main__":
    main()
