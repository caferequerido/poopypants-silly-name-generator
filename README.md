## Professor Poopypants Silly Name Generator
- This is just a simple python based class for generating a silly name from a first+last name using Professor Poopypants patented silly name generation process.
- See https://www.pilkey.com/userFiles/uploads/funstuff/RG_Scholastic_CUEK_NameChange.pdf

## How to use
```
from sillynamegenerator.pp_silly_name_generator import *


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

```
