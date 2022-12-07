from pandas import read_csv
from PIL import Image
from glob import glob


# this was a lot more complicated, but i simplified it a lot
def load_cluster_data():
    # I want to store different objects, so i had to convert the nparray to list.
    cluster_stats = read_csv('resources/cluster_data.csv').values.tolist()

    # this loads in all the file names, and sorts them
    bloon_pics = sorted(glob('resources/media/bloons/*.webp'))

    print(bloon_pics)
    print(type(bloon_pics[10]))
    print(len(bloon_pics[10]))

    print("cluster_stats type ,len", type(cluster_stats), len(cluster_stats))
    print("bloon_pics type ,len", type(bloon_pics), len(bloon_pics))


    for i, cluster in enumerate(cluster_stats):
        bloon_id = str(i).zfill(3)
        cluster_stats[i].append(bloon_pics[i])


    print("bruh")

    # Below is how I was previously opening the file, and save the image OBJECT, rather than just the file location
    # This is beacuse with the glob package, it is super easy to load files. # actually, now that I think about it
    # I am using the


    # for i, pic in enumerate(bloon_pics):
    #     bloon_id = str(i).zfill(3)
    #
    #     print(i)
    #     image = Image.open(bloon_pics[i])
    #     cluster_stats.append(image)
    #
    #     image.close()
    #
    return cluster_stats


def load_round_data():
    return read_csv('resources/round_data.csv').values

# def load_monkey_data():
#     # An array that contains BloonSend objects pulled from the CSV
#     monkey_data = read_csv('resources/tower_data.csv').values
#     monkeys = []
#
#     # Takes the bloon resources and converts it in BloonSend objects.
#     for monkey in monkey_data:
#         bloon = BloonSend(traits[0], traits[1], traits[2], traits[3], traits[7])
#         towers.append(bloon)
#
#     return towers
