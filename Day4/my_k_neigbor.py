import numpy as np

x = [1,2,3,6,7,8]
y = [1,2,3,6,7,8]
category = ['A','A','A','B','B','B']
k = 3


def distance(x1,y1,x2,y2):
    # https://www.shiksha.com/online-courses/articles/wp-content/uploads/sites/11/2022/12/image-11.png
    dist = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    return dist


# The x- and y-coordinates where our new dot is:
point_x = 6.5
point_y = 4.2

all_distances = []
all_distances_sorted = [] # We add a second list so we can sort this without disrupting the original
for i in range(len(x)):
    dist = distance(x[i],y[i],point_x,point_y)
    all_distances.append(dist)
    all_distances_sorted.append(dist)

all_distances_sorted.sort()
nr_of_category = []
for i in range(k):
    nr_of_category.append(category[all_distances.index(all_distances_sorted[i])])

print(f"The {k} nearest neighbors have the category:", *nr_of_category)
print('So this point is: ', end="")
if(nr_of_category.count('A')) > nr_of_category.count('B'):
    print('A')
else:
    print('B')
