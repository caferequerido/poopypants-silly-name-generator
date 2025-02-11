"""Module that takes a normal first and last name and returns a silly first and last name."""


class PoopypantsSillyNameGenerator:
    """Class for storing silly name generation logic. """

    def __init__(self):

        self.first_name_dict = {
            "a": "Stinky",
            "b": "Lumpy",
            "c": "Buttercup",
            "d": "Gidget",
            "e": "Crusty",
            "f": "Greasy",
            "g": "Fluffy",
            "h": "Cheeseball",
            "i": "Chim-chim",
            "j": "Poopsie",
            "k": "Flunky",
            "l": "Booger",
            "m": "Pinky",
            "n": "Zippy",
            "o": "Goober",
            "p": "Doofus",
            "q": "Slimy",
            "r": "Loopy",
            "s": "Snotty",
            "t": "Falafel",
            "u": "Dorkey",
            "v": "Squeezit",
            "w": "Oprah",
            "x": "Skipper",
            "y": "Dinky",
            "z": "Zsa-zsa",
        }
        self.last_name_dict_1 = {
            "a": "Diaper",
            "b": "Toilet",
            "c": "Giggle",
            "d": "Bubble",
            "e": "Girdle",
            "f": "Barf",
            "g": "Lizard",
            "h": "Waffle",
            "i": "Cootie",
            "j": "Monkey",
            "k": "Potty",
            "l": "Liver",
            "m": "Banana",
            "n": "Rhino",
            "o": "Burger",
            "p": "Hamster",
            "q": "Toad",
            "r": "Gizzard",
            "s": "Pizza",
            "t": "Gerbil",
            "u": "Chicken",
            "v": "Pickle",
            "w": "Chuckle",
            "x": "Tofu",
            "y": "Gorilla",
            "z": "Stinker",
        }
        self.last_name_dict_2 = {
            "a": "head",
            "b": "mouth",
            "c": "face",
            "d": "nose",
            "e": "tush",
            "f": "breath",
            "g": "pants",
            "h": "shorts",
            "i": "lips",
            "j": "honker",
            "k": "butt",
            "l": "brain",
            "m": "tushie",
            "n": "chunks",
            "o": "hiney",
            "p": "biscuits",
            "q": "toes",
            "r": "buns",
            "s": "fanny",
            "t": "sniffer",
            "u": "sprinkles",
            "v": "kisser",
            "w": "squirt",
            "x": "humperdinck",
            "y": "brains",
            "z": "juice",
        }

    def lookup(self, firstname, lastname):
        """
        Take firstname and lastname and return sillyname
        Args:
            firstname (str): firstname
            lastname (str): lastname

        Returns:
            str: A single string with silly name.
        """
        first_name_first_letter = firstname[0]
        last_name_first_letter = lastname[0]
        last_name_last_character = lastname[-1]

        print(f"{firstname} --> {first_name_first_letter}")
        print(f"{lastname} --> {last_name_first_letter}..{last_name_last_character}")

        lookup1 = self.first_name_dict.get(str.lower(first_name_first_letter))
        lookup2 = self.last_name_dict_1.get(str.lower(last_name_first_letter))
        lookup3 = self.last_name_dict_2.get(str.lower(last_name_last_character))

        sillyname = f"{lookup1} {lookup2}{lookup3}"

        return sillyname

    def print_generator_lookups(self):
        """
        Returns the dictionaries used for silly name generation.
        """
        print(f"First name lookup with first letter of first name: {self.first_name_dict}")
        print(f"Last name part 1 lookup with first letter of last name: {self.last_name_dict_1}")
        print(f"Last name part 2 lookup with last letter of last name: {self.last_name_dict_2}")
