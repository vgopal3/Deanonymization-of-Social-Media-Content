from random import randint
import math

# Graph - Defines the users in the network. Key indicates the user and value indicates his followers
graph = {'A': ['B', 'C'],'B': ['C', 'D'],'C': ['D','H'],'D': ['C'],'E': ['F'],'F': ['C','G'],'G':['H','B','C'],'H':['I','A'],'I':['J','K'],'K':['E']}

history = []

# Generate Random numbers and consider them as the entire availed history
for i in range(0,100):
	history.append(str(i))

# Find shortest path between 2 nodes
def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None

# Create a recommendatino list for every user
def create_reco_list(n):
	reco_list = []
	for i in range(0,n):
		reco_list.append(str(randint(0,99)))
	
	return reco_list
	
# Find all paths between 2 nodes
def find_all_paths(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
	    return [path]
	if not graph.has_key(start):
	    return []
	paths = []
	for node in graph[start]:
	    if node not in path:
		newpaths = find_all_paths(graph, node, end, path)
		for newpath in newpaths:
		    paths.append(newpath)
	return paths


def main():
	print " \n Finding a sinle path"
	print find_path(graph, 'A','K')
	print " \n Printing all pathts "
	print find_all_paths(graph,'A','K')
	
	print "\nPrinting complete user information"
	for keys in graph:
		print "\n############"
		print "\nUsername : ", keys
		print "\nFollowers list: ", graph[keys]
		print "\n NUmber of followers : ", len(graph[keys])

	print " \n Complete History \n"
	print history
	len_count = []
	for i in range(0,10):
		len_count.append(0)
	# Avail recommendation list for every user
	complete_reco_list = []
	no_of_followers = []
	for key in graph:
		complete_reco_list.append(create_reco_list(randint(0,25)))
		no_of_followers.append(len(graph[key]))

	print "\n Complete Recommendation List : "
	len_count = []
	print complete_reco_list
	
	for j in range(0,len(complete_reco_list)):
		len_count.append( set(history).intersection(complete_reco_list[j]))
	
	lambda_value = 0.005
	array_intersection = []
	final_R_value = []
	lambda_each_user = []

	for i in range(0,len(len_count)):
		z = len(len_count[i])
		
		array_intersection.append(float(z)/100)
	

	for i in range(0,len(array_intersection)):
		lambda_each_user.append(no_of_followers[i] * lambda_value)


	# Evaluation of final values, pR and qR
	for i in range(0,10):
		
		x = array_intersection[i] * (math.log10((float(array_intersection[i]))/(lambda_each_user[i])))
		y = (1 - array_intersection[i]) * (math.log10((1 - array_intersection[i])/(1 - lambda_each_user[i])))
		final_R_value.append(x + y)

	print " \n R value for all users : ", final_R_value
	print " Maximum R value : ", max(final_R_value)

	
if __name__ == "__main__":
  main()

