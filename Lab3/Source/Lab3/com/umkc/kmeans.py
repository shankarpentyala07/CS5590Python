import matplotlib.pyplot as plt1
import pandas as pd
from sklearn.cluster import KMeans
# load the dataset
custdata = pd.read_csv('Customers.csv')
X = custdata.iloc[:, [3, 4]].values
# Apply K-Means to the dataset
kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 10)
y_kmeans = kmeans.fit_predict(X)
# clusters
plt1.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'blue', label = 'Cluster 1')
plt1.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'red', label = 'Cluster 2')
plt1.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt1.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt1.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt1.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt1.title('Clusters of customers')
plt1.xlabel('Annual Income (k$)')
plt1.ylabel('Spending Score (1-100)')
plt1.legend()
plt1.show()