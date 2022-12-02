from pandas import read_csv
from BloonEntity import BloonEntity
from GroupSend import GroupSend


def run():
    bloon_data = read_csv('bloon_data.csv').values

    bloon_types = []

    # Takes the bloon data and converts it in BloonEntity objects.
    for trait in bloon_data:
        bloon_type = BloonEntity(trait[0], trait[1], trait[2], trait[3], trait[4], trait[5], trait[6], trait[7])
        bloon_types.append(bloon_type)

    print(bloon_types[1].eco_sec)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()


