# Face-detection-using-openCV
Face detection task is to identify the human faces in the given image. This task is performed by
using classifiers. The classifier decides whether a given image has a face or not respectively
positive or negative. This is performed by a set of weak classifiers which combine with their
respective weightsto produce a final classifier. This is known as Boosting Algorithm. Initially every
classifier is initialized with equal weights, then taking set of filters on every part of the image
(equal to the window size), the weights get updated based on the threshold for each filter. Then
we need to select best filter and threshold combination. This is know as the Cascade classification
because it rejects the non-face region saving the computation time.
