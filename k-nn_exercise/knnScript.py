from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imutils import paths
import argparse

from preprocessing import simplepreprocessor as spimport
from datasets import simpledatasetloader as sdimport

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help = "path to input dataset")
ap.add_argument("-k", "--neighbors", type=int, default=1, help = "# of nearest neighbors for classification")
ap.add_argument("-j", "--jobs", type=int, default=1, help = "# of jobs for k-NN distance (-1 uses all available cores)")
args = vars(ap.parse_args())

print("[INFO] loading images...")
imagePaths = list(paths.list_images(args["dataset"]))

#print(paths.list_images(args["dataset"])) #debuggy
#print("imagePaths: " + str(imagePaths)) #debuggy
                  
sp = spimport.SimplePreProcessor(32, 32)
sdl = sdimport.SimpleDataSetLoader(preprocessors=[sp])
(data, labels) = sdl.load(imagePaths, verbose = 500) 
data = data.reshape((data.shape[0], 3072))

print("what is this")
print("[INFO] features matrix: {:.1f}MB".format(data.nbytes / (1024 * 1024.0)))

le = LabelEncoder()
labels = le.fit_transform(labels)

(TrainX, TestX, TrainY, TestY) = train_test_split(data, labels, test_size=0.25, random_state=42)

model = KNeighborsClassifier(n_neighbors=args["neighbors"], n_jobs=args["jobs"])
model.fit(TrainX, TrainY)
print(classification_report(TestY, model.predict(TestX), target_names=le.classes_))