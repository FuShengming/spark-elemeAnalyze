import pandas as pd
from yellowbrick.text import UMAPVisualizer,FreqDistVisualizer,TSNEVisualizer
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from collections import defaultdict
data=pd.read_csv('C:/Users/Admin/Desktop/Mllib/Training.txt',header=0)
tfidf=TfidfVectorizer(min_df=3,smooth_idf=True)

x=tfidf.fit_transform(data["Comment"])
y=data["Category"]

tsne=TSNEVisualizer(labels=["口味","卫生","份量","配餐","配送"])
tsne.fit(x,y)
tsne.show()

# umap=UMAPVisualizer(metric='cosine')
# umap.fit(x,y)
# umap.show()

# vectorizer = CountVectorizer()
# dict=defaultdict(list)
# for text, label in zip(data["Comment"], data["Category"]):
#     dict[label].append(text)
#
# comments=vectorizer.fit_transform(text for text in dict['配送'])
# features=vectorizer.get_feature_names()
#
# visualizer = FreqDistVisualizer(features=features, orient='v')
# visualizer.fit(comments)
# visualizer.show()