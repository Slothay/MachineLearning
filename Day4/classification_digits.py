from matplotlib import pyplot as plt
import numpy as np

from sklearn import datasets
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import train_test_split

# the digits dataset stores grayscale images of size 8x8 pixels
digits = datasets.load_digits()
# If we try printing the dataset we can see that it is actually a dictionary
#print(digits) # FROM HERE TO
# And by accessing the key data and the first index of that value we can find the first digit
#print(digits['data'][0])

# if we shape this into a matrice of 8 x 8 pixels, we can display the image:
# To further enhance the image we can switch to a grayscale color-map using cmap=plt.cm.gray_r (there are lots of color maps)
image = np.array(digits['data'][0]).reshape(8,8)
#print(image)
plt.imshow(image, cmap=plt.cm.gray_r)
# So here we have the number 0 (one of them)
plt.show()
# There are 1797 images in the dataset
print(len(digits['data']))
# HERE CAN BE COMMENTED OUT

# The underscore is used to ignore a parameter (we don't need the figure) 
# Underscore is used in the interpreter to save the last value
_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
# The zip-function acts like a zipper, so it will take one value from axes, digits.images and digits.target and join as a new Tuple
for ax, image, label in zip(axes, digits.images, digits.target):
    # Make sure we don't have x,y axis
    ax.set_axis_off()
    # Prepare the image (we don't show it yet)
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    # Set the title for this subplot. The %i is substituted by an integer (label) which is the number that the image represents
    ax.set_title('Training: %i' % label)
# can show plot
# plt.show()

# In order to train this model we have to have a one-dimensionel array of each image, so we are going to flatten them
# Find number of images
n_samples = len(digits.images)
# reshape so that every row contains a separate image
data = digits.images.reshape((n_samples, -1))

# Now it's time to create a support vector classifier
# kernel, gamma, C and degree are parameters that can be tweaked
classifier = svm.SVC(kernel="poly",gamma=0.0001,C=10,degree=4)

X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.2, shuffle=False)

# Learn the digits on the train subset
# Fits the classifier
classifier.fit(X_train, y_train)

# Now we have a trained model, and we're going to try it on the test-set
# Predict the value of the digit on the test subset
predicted = classifier.predict(X_test)

# Let's display the results
_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, prediction in zip(axes, X_test, predicted):
    ax.set_axis_off()
    # We have to reshape the images again to show them
    image = image.reshape(8, 8)
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    ax.set_title(f'Prediction: {prediction}')
 

print(f"Statistics for classifier {classifier}:\n"
      f"{metrics.classification_report(y_test, predicted)}\n")


