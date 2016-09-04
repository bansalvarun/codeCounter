import random
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn import cluster

adj_users_tag = []
num_of_users = 1000
num_of_tags = 16

for user_no in xrange(0, num_of_users):
	tags = []
	for tag_no in xrange(0, num_of_tags):
		tags.append(0)
	adj_users_tag.append(tags)

for user_no in xrange(0, num_of_users):
	for tag_no in xrange(0, num_of_tags):
		if user_no < num_of_users/5:
			adj_users_tag[user_no][tag_no] = 1
		elif user_no < 2*num_of_users/5:
			adj_users_tag[user_no][tag_no] = 0
		elif user_no < 3*num_of_users/4:
			adj_users_tag[user_no][tag_no] = (1-tag_no)%2
		else:
			adj_users_tag[user_no][tag_no] = random.randint(0, 1)
	
model = TSNE(learning_rate = 200.0)
tsne_data = model.fit_transform(adj_users_tag)

def plot_cluster(point_label, window_title):
	orig = plt.figure(1)
	print "Points labels : " + str(point_label)
	plt.scatter(tsne_data[:,0], tsne_data[:,1], c = point_label)
	plt.title(window_title)
	# orig.show()
	# raw_input()
	orig.savefig(window_title + ".png")

sqrt_n = int(num_of_tags**0.5)
for sqrt_comp in xrange(0, num_of_tags, sqrt_n):
	cluster_dict = {}
	cluster_list = []
	user_label = [0 for i in xrange(0, num_of_users)]
	for user_no in xrange(0, num_of_users):
		bits = 0
		for tag_no in xrange(sqrt_comp, sqrt_comp + sqrt_n):
			bits = bits*10 + adj_users_tag[user_no][tag_no]
		if bits in cluster_dict:
			cluster_dict[bits].append(user_no)
		else:
			cluster_dict[bits] = []
			cluster_dict[bits].append(user_no)
			cluster_list.append(bits)
	ctr = 0
	for bits in cluster_list:
		for users in cluster_dict[bits]:
			user_label[users] = ctr
		ctr += 1

	plot_cluster(user_label, "Sqrt N chunks Cluster")
	break

sqrt_n = int(num_of_tags**0.5)
for sqrt_comp in xrange(0, num_of_tags, sqrt_n):
	cluster_dict = {}
	cluster_list = []
	user_label = [0 for i in xrange(0, num_of_users)]
	temp_user_tag = []
	for user_no in xrange(0, num_of_users):
		tags = []
		for tag_no in xrange(sqrt_comp, sqrt_comp + sqrt_n):
			tags.append(adj_users_tag[user_no][tag_no])
		temp_user_tag.append(tags)
	
	print temp_user_tag
	k_means = cluster.KMeans(n_clusters=4)
	k_means.fit(temp_user_tag) 
	print(k_means.labels_)

	plot_cluster(k_means.labels_, "K Means")
	break

sqrt_n = int(num_of_tags**0.5)
for sqrt_comp in xrange(0, num_of_tags, sqrt_n):
	cluster_dict = {}
	cluster_list = []
	user_label = [0 for i in xrange(0, num_of_users)]
	temp_user_tag = []
	for user_no in xrange(0, num_of_users):
		tags = []
		for tag_no in xrange(sqrt_comp, sqrt_comp + sqrt_n):
			tags.append(adj_users_tag[user_no][tag_no])
		temp_user_tag.append(tags)
	
	k_means = cluster.SpectralClustering(n_clusters=4)
	k_means.fit(temp_user_tag) 
	print(k_means.labels_)

	plot_cluster(k_means.labels_, "Spectral Clustering")
	break



