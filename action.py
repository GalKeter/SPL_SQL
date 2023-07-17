from persistence import *

import sys

def main(args : list):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            #TODO: apply the action (and insert to the table) if possible
            _product_id = splittedline[0]
            _quantity = int(splittedline[1])
            curr_quantity = repo.products.find(id=_product_id)[0].quantity
            if(_quantity!=0 and curr_quantity+_quantity>=0):
                repo.products.update(quantity=_quantity+curr_quantity, id=_product_id)
                repo.activities.insert(Activitie(*splittedline))

if __name__ == '__main__':
    main(sys.argv)